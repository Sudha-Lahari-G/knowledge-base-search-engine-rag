# How to upload this project to GitHub (exact commands)

1. Create a new repository on GitHub (e.g., `kb-search-rag-demo`). Do NOT initialize with README or .gitignore on GitHub if you will push an existing local repo.

2. From the project directory, run:
```bash
cd path/to/kb_search_engine_streamlit
git init
git add .
git commit -m "Initial commit — Knowledge-base Search Engine (Streamlit + RAG)"
# replace <YOUR_REMOTE_URL> with the HTTPS git URL from GitHub, e.g. https://github.com/youruser/kb-search-rag-demo.git
git remote add origin <YOUR_REMOTE_URL>
git branch -M main
git push -u origin main
```

3. Verify on GitHub that files are present.

4. (Optional) Create a release or upload demo video under Releases.
