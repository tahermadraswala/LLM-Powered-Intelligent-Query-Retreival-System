
# LLM-Powered Intelligent Query Retrieval System

A powerful AI system that leverages Large Language Models (LLMs) to understand natural language queries and retrieve relevant information from unstructured documents like policy files, contracts, and emails.

## 🔍 Features

- 📄 Upload documents (PDFs, DOCs, etc.)
- 🤖 Ask natural language questions
- 🧠 Get precise answers with contextual information
- ⚡ Fast retrieval using vector databases and embeddings
- 🔐 Authentication and secure document access

## 🛠️ Tech Stack

**Frontend**
- React.js
- Tailwind CSS

**Backend**
- Flask
- Langchain
- OpenAI / LlamaIndex
- FAISS (Vector DB)

**Others**
- Pinecone / ChromaDB (Optional)
- Docker (Optional)
- GitHub Actions (Optional CI/CD)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/tahermadraswala/LLM-Powered-Intelligent-Query-Retreival-System.git
cd LLM-Powered-Intelligent-Query-Retreival-System
2. Setup the Backend
bash
Always show details

Copy
cd backend
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\\Scripts\\activate         # For Windows

pip install -r requirements.txt
uvicorn main:app --reload
Note: Make sure to configure .env with your API keys (e.g., OpenAI).

3. Setup the Frontend
bash
Always show details

Copy
cd frontend-app/my-app
npm install
npm run dev
App will be live at: http://localhost:5173/

📁 Folder Structure
graphql
Always show details

Copy
LLM-Powered-Intelligent-Query-Retreival-System/
├── backend/               # FastAPI backend with LLM logic
├── frontend-app/my-app/   # React frontend
├── requirements.txt
└── README.md
📌 To Do / Upcoming
 Add user authentication

 Multi-language support

 Plug-and-play document types

 Analytics dashboard

👨‍💻 Contributors
Atharva Sachidanand Mali
Taher Madraswala

📄 License
MIT License. See LICENSE file.
"""



Save PDF
pdf_path = "/mnt/data/LLM_Query_Retrieval_README.pdf"
pdf.output(pdf_path)

pdf_path

