import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Knowledge Assistant")

# -----------------------------
# Clear Chat
# -----------------------------
if st.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.divider()

# -----------------------------
# Upload PDFs
# -----------------------------
st.subheader("📄 Upload PDF Documents")

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("🚀 Process Documents"):

    if uploaded_files:

        files = [
            (
                "files",
                (
                    file.name,
                    file,
                    "application/pdf"
                )
            )
            for file in uploaded_files
        ]

        with st.spinner("Processing documents..."):

            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

        if response.status_code == 200:
            st.success("Documents processed successfully!")
        else:
            st.error("Failed to process documents.")

    else:
        st.warning("Please select PDF files.")

st.divider()

# -----------------------------
# Knowledge Base
# -----------------------------
st.subheader("📚 Knowledge Base")

try:

    response = requests.get(
        f"{API_URL}/documents"
    )

    documents = response.json()["documents"]

    if documents:

        for document in documents:
            st.markdown(f"✅ {document}")

    else:

        st.info("No PDF documents available.")

except Exception:

    st.error("Unable to load documents.")

st.divider()

st.markdown("""
Ask questions from your knowledge base.

### Features

- 📄 Multi-PDF Search
- 🔍 FAISS Vector Search
- 🧠 CrossEncoder Reranking
- 🤖 Gemini LLM
- 📚 Source Citations
""")

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
if prompt := st.chat_input("Ask a question..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        with st.spinner("Searching knowledge base..."):

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "question": prompt
                },
                timeout=60
            )

            answer = response.json()["answer"]

    except Exception as e:

        answer = f"Error: {e}"

    with st.chat_message("assistant"):

        if "Sources:" in answer:
 
            response_text, sources = answer.split("Sources:", 1)

            st.markdown(response_text)

            st.markdown("---")
            st.subheader("📚 Sources")

            for source in sources.strip().split("\n"):
                if source.strip():
                    st.markdown(f"📄 {source.replace('•', '').strip()}")

        else:

            st.markdown(answer)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )