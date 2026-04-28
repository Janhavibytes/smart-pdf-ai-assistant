import streamlit as st
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="Smart PDF AI Assistant", layout="wide")

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}
.sub-text {
    text-align: center;
    font-size: 14px;
    color: gray;
    margin-bottom: 30px;
}
.upload-box {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Smart PDF AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Janhavi Rathod</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if "db" not in st.session_state:
    st.session_state.db = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if not os.path.exists("uploads"):
    os.makedirs("uploads")

if uploaded_files:
    all_docs = []

    with st.spinner("Processing documents..."):
        for file in uploaded_files:
            path = os.path.join("uploads", file.name)
            with open(path, "wb") as f:
                f.write(file.read())

            loader = PyPDFLoader(path)
            docs = loader.load()

            for d in docs:
                d.metadata["source"] = file.name

            all_docs.extend(docs)

        splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
        chunks = splitter.split_documents(all_docs)

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        st.session_state.db = FAISS.from_documents(chunks, embeddings)

    st.success("Documents ready")

query = st.chat_input("Ask something from your document...")

def generate_answer(query, db):
    results = db.similarity_search(query, k=5)

    if not results:
        return "No relevant information found."

    content = []
    for r in results:
        text = r.page_content.strip()
        if text and text not in content:
            content.append(text)

    combined = "\n\n".join(content)

    if len(combined) > 1200:
        combined = combined[:1200] + "..."

    answer = combined.replace("\n", " ").strip()

    return answer

if query and st.session_state.db:
    with st.spinner("Searching..."):
        answer = generate_answer(query, st.session_state.db)

        st.session_state.chat_history.append(("user", query))
        st.session_state.chat_history.append(("assistant", answer))

for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(msg)