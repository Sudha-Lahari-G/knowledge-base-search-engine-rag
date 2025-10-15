import streamlit as st
from backend.ingest import ingest_documents, load_vectorstore, save_vectorstore
from backend.rag import answer_query
import os

st.set_page_config(page_title="Knowledge-base Search (RAG)", layout="wide")

st.title("Knowledge-base Search Engine — RAG demo")
st.markdown(
    """Upload PDF / TXT documents, build a vector store (FAISS) using sentence-transformers embeddings,
    then ask questions — answers are synthesized via OpenAI (ChatCompletion) using retrieved context.
    **Requirements:** Set environment variable `OPENAI_API_KEY` before running the app.
    """
)

with st.sidebar:
    st.header("1) Ingest documents")
    uploaded = st.file_uploader("Upload PDF or TXT files (multiple)", accept_multiple_files=True, type=['pdf','txt'])
    chunk_size = st.number_input("Chunk size (chars)", min_value=200, max_value=5000, value=1200, step=100)
    chunk_overlap = st.number_input("Chunk overlap (chars)", min_value=0, max_value=500, value=200, step=10)
    if st.button("Ingest uploaded files"):
        if not uploaded:
            st.warning("Please upload at least one PDF or TXT file.")
        else:
            docs = []
            for f in uploaded:
                # save to sample_docs
                save_path = os.path.join("sample_docs", f.name)
                with open(save_path, "wb") as out:
                    out.write(f.getbuffer())
                docs.append(save_path)
            st.info(f"Saved {len(docs)} files to sample_docs/ and starting ingestion...")
            vs = ingest_documents(docs, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            save_vectorstore(vs)
            st.success("Ingestion complete and vector store saved.")

    st.header("2) Vector store")
    if st.button("Load existing vector store (if any)"):
        vs = load_vectorstore()
        if vs is None:
            st.warning("No saved vectorstore found. Ingest documents first.")
        else:
            st.success("Vectorstore loaded.")

st.header("Ask a question")
query = st.text_input("Enter your question here")
top_k = st.slider("Number of retrieved chunks (k)", 1, 10, 4)
if st.button("Get Answer"):
    if not query:
        st.warning("Please type a question.")
    else:
        try:
            answer, sources = answer_query(query, top_k=top_k)
            st.subheader("Answer")
            st.write(answer)
            st.subheader("Retrieved source chunks")
            for i, s in enumerate(sources, 1):
                st.markdown(f"**Chunk {i} — source:** {s['source']}")
                st.text(s['text'][:1000] + ("..." if len(s['text'])>1000 else ""))
        except Exception as e:
            st.error(f"Error during query: {e}")
