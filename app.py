import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from utils import process_and_chunk_documents

# Load environment variables from .env file
load_dotenv()

from flask_cors import CORS
# --- Configuration ---
DATA_FOLDER = "data"
VECTOR_STORE_PATH = "faiss_index"

# Ensure the Google API key is set
if "GOOGLE_API_KEY" not in os.environ:
    raise ValueError("Google API key not found. Please set it in your .env file.")


def build_vector_store():
    """
    Builds the FAISS vector store from documents in the data folder
    and saves it to disk. (We only need to run this once).
    """
    print("Starting to process documents...")
    chunked_docs = process_and_chunk_documents(DATA_FOLDER)
    
    if not chunked_docs:
        print("No documents were processed. Please check the 'data' folder. Exiting.")
        return

    print("Creating embeddings and building FAISS vector store...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_documents(documents=chunked_docs, embedding=embeddings)
    
    print(f"Vector store created successfully. Saving to '{VECTOR_STORE_PATH}'...")
    vectorstore.save_local(VECTOR_STORE_PATH)
    print("--- Vector store build process complete. ---")


def create_rag_chain():
    """
    Creates the complete RAG chain for querying.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.load_local(VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()

    # --- UPDATED AND MORE ADVANCED PROMPT TEMPLATE ---
    template = """
    You are an expert insurance claims analyst. Your first task is to determine the user's intent based on their query. There are two possible intents:
    1. Information-seeking: The user is asking a general question about the policy rules (e.g., "What is the waiting period for X?", "Are cosmetic procedures covered?").
    2. Claim Evaluation: The user is describing a personal situation and asking if they are covered (e.g., "I am 46 and need knee surgery...", "I had an accident...").

    Based on the determined intent, provide a response in the appropriate format.

    - If the intent is Information-seeking: Provide a clear, direct answer to the user's question based on the context. Do not give a decision like 'Approved' or 'Rejected'. Just state the facts from the policy.

    - If the intent is Claim Evaluation: Provide a structured response with a clear 'Decision' ('Approved', 'Rejected', or 'Approved (partially)') and a 'Justification'. The justification must be a step-by-step explanation of your reasoning, citing the exact clauses from the context provided.

    CONTEXT:
    {context}

    QUERY:
    {question}

    YOUR DETAILED RESPONSE:
    """
    prompt = PromptTemplate.from_template(template)

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain


if __name__ == "__main__":
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    CORS(app)  # Enable CORS for all routes
    claim_processor_chain = None
    if os.path.exists(VECTOR_STORE_PATH):
        print("Loading the claim processor... Please wait.")
        claim_processor_chain = create_rag_chain()
        print("Claim processor is ready.")
    else:
        print(f"Vector store not found at '{VECTOR_STORE_PATH}'.")
        print("Please run build_vector_store() first.")

    @app.route("/query", methods=["POST"])
    def query():
        if claim_processor_chain is None:
            return jsonify({"answer": "Claim processor not initialized."}), 500
        data = request.get_json()
        user_query = data.get("query", "")
        if not user_query.strip():
            return jsonify({"answer": "Query cannot be empty."}), 400
        response = claim_processor_chain.invoke(user_query)
        return jsonify({"answer": response})

    app.run(host="0.0.0.0", port=5000)