# 🧠 Knowledge-base Search Engine (RAG)
### Retrieval-Augmented Generation Demo — Built with Streamlit + OpenAI + FAISS

This project implements a **Knowledge-base Search Engine** that can **search across uploaded documents** and **generate synthesized answers** using a Large Language Model (LLM) and vector-based retrieval.

---

## 🚀 Key Features
✅ Upload multiple PDF / TXT documents  
✅ Automatic document chunking & embedding (SentenceTransformers)  
✅ FAISS vector store for fast retrieval  
✅ Retrieval-Augmented Generation (RAG) using OpenAI API  
✅ Streamlit web interface for interactive queries  
✅ Fallback mode without API key (extractive search only)

---

## 🧩 Architecture Overview
1. **Document Ingestion:** Extracts text, splits into chunks, and embeds using `all-MiniLM-L6-v2`.
2. **Vector Store:** Stores embeddings in a **FAISS** index for similarity search.
3. **Query Stage:** Retrieves top-matching chunks for a user query.
4. **Answer Generation:** Synthesizes a final answer using OpenAI (or fallback to extractive output).

```bash
User Query ➜ Vector Search (FAISS) ➜ Retrieved Context ➜ OpenAI LLM ➜ Synthesized Answer
```

---

## 🧰 Tech Stack
- **Frontend:** Streamlit  
- **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)  
- **Vector Store:** FAISS  
- **LLM API:** OpenAI GPT-4o-mini  
- **Language:** Python 3.10+  

---

## 🧠 How to Run Locally

### 1️⃣ Setup Environment
```bash
git clone https://github.com/<your-username>/kb-search-rag-demo.git
cd kb-search-rag-demo
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2️⃣ (Optional) Add OpenAI Key
```bash
export OPENAI_API_KEY="sk-..."
# or Windows PowerShell: setx OPENAI_API_KEY "sk-..."
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

---

## 💡 Example Queries
| Sample Document | Example Query | Expected Answer |
|-----------------|----------------|----------------|
| `sample1.txt` | What does Acme Corporation do? | Acme makes widgets and provides services. |
| `sample2.txt` | What does the PDF say about RAG? | It explains building a retrieval-augmented generation system. |

---

## 📸 Demo (Recommended for Submission)
Record your demo using the included script:
```bash
python demo_record.py
```
This generates a **demo.mp4** file you can upload along with your GitHub repository.

---

## 📦 Repository Structure
```
kb_search_engine_streamlit/
├── app.py
├── backend/
│   ├── ingest.py
│   ├── rag.py
│   ├── utils.py
├── sample_docs/
│   ├── sample1.txt
│   ├── sample2.txt
├── demo_record.py
├── README.md
├── requirements.txt
├── GITHUB_UPLOAD.md
└── .gitignore
```

---

## 🧾 Evaluation Focus
| Criteria | Description |
|-----------|-------------|
| Retrieval Accuracy | Uses FAISS + MiniLM for semantic similarity |
| Synthesis Quality | GPT-based summarization of retrieved chunks |
| Code Structure | Modular backend + clear frontend separation |
| LLM Integration | Context-aware prompting & fallback handling |

---

## 🧠 Future Enhancements
- Add Pinecone or Weaviate as cloud vector store  
- Add source citation highlighting  
- Support CSV / DOCX ingestion  
- Deploy on Streamlit Cloud for public demo  

---

### 👩‍💻 Author
**Sudha Lahari Ganti**  
_22BCE8427, VIT-AP University_  
Built for company assessment — **Knowledge-base Search Engine (RAG)**

---

📺 _“Empowering knowledge discovery through intelligent retrieval and synthesis.”_
