# LLM-Powered-Intelligent-Query-Retreival-System

This project is an AI-powered system designed to answer natural language queries based on the content of large, unstructured documents like policy manuals or contracts. It uses a Retrieval-Augmented Generation (RAG) architecture to provide accurate, context-aware, and explainable answers.

## Features

* **Natural Language Queries:** Ask questions in plain English.
* **Multi-Format Document Support:** Ingests and processes PDF and DOCX files.
* **Intelligent Reasoning:** Uses a Large Language Model (LLM) to understand context and apply policy rules based on user intent.
* **Explainable AI:** Provides justifications for its decisions by citing the specific clauses used.
* **Interactive CLI:** A command-line interface to ask multiple questions in a single session.

## Tech Stack

* **Language:** Python
* **Core Libraries:** LangChain, Google Generative AI
* **Vector Store:** FAISS (for local semantic search)
* **Document Processing:** PyPDF, Unstructured

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/tahermadraswala/LLM-Powered-Intelligent-Query-Retreival-System.git](https://github.com/tahermadraswala/LLM-Powered-Intelligent-Query-Retreival-System.git)
    cd LLM-Powered-Intelligent-Query-Retreival-System
    ```
2.  **Install dependencies:**
    *(It's recommended to create a virtual environment first)*
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: To create the `requirements.txt` file, run `pip freeze > requirements.txt` in your terminal).*

3.  **Set up environment variables:**
    * Create a file named `.env` in the root directory.
    * Add your Google API key to the file:
        ```
        GOOGLE_API_KEY="YOUR_SECRET_API_KEY"
        ```

## How to Run

1.  **Add Documents:** Place your `.pdf` or `.docx` files into the `data/` folder.
2.  **Build the Knowledge Base (Run Once):**
    * In `app.py`, uncomment the `build_vector_store()` line.
    * Run `python app.py`. This will create a `faiss_index` folder.
3.  **Query the System:**
    * Comment out the `build_vector_store()` line in `app.py` again.
    * Run `python app.py` to start the interactive session and ask questions.

## Contributors

This project was a collaborative effort.

* **Atharva Mali:** Lead development, core logic implementation, and RAG pipeline architecture.
* **Taher Madraswala:** Project management, testing, and GitHub administration.

