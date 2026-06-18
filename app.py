import streamlit as st
import time
import pandas as pd

from langchain_ollama import OllamaLLM

from chatbot.pdf_loader import load_pdf
from chatbot.text_splitter import split_documents
from chatbot.embeddings import get_embedding_model
from chatbot.vector_store import create_vector_store
from chatbot.rag_pipeline import create_rag_chain
from chatbot.utils import save_uploaded_file

from analytics.logger import log_chat


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Enterprise AI Chatbot",
    layout="wide"
)

# =========================
# TITLE
# =========================

st.title("🤖 Enterprise Generative AI Chatbot")

st.write(
    "Ask general questions or upload PDF for document Q&A."
)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("📄 Upload Company PDF")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# =========================
# LOAD FAST LLM
# =========================

general_llm = OllamaLLM(
    model="llama3.2:1b",
    base_url="http://127.0.0.1:11434"
)

# =========================
# CACHE PDF PROCESSING
# =========================

@st.cache_resource
def process_pdf(save_path):

    documents = load_pdf(save_path)

    chunks = split_documents(documents)

    embeddings = get_embedding_model()

    vectorstore = create_vector_store(
        chunks,
        embeddings
    )

    qa_chain = create_rag_chain(
        vectorstore
    )

    return qa_chain


# =========================
# USER INPUT
# =========================

user_question = st.text_input(
    "Ask Anything"
)

# =========================
# PDF MODE
# =========================

if uploaded_file is not None:

    try:

        save_path = save_uploaded_file(
            uploaded_file
        )

        st.success(
            "✅ PDF Uploaded Successfully"
        )

        # Process PDF ONLY ONCE
        qa_chain = process_pdf(
            save_path
        )

        if user_question:

            with st.spinner(
                "Generating PDF Answer..."
            ):

                start = time.time()

                # SHORT ANSWER PROMPT
                short_prompt = f"""
                Give a short and concise answer
                in 3 to 5 lines only.

                Question:
                {user_question}
                """

                answer = qa_chain(
                    short_prompt
                )

                end = time.time()

                response_time = round(
                    end - start,
                    2
                )

                # Save logs
                log_chat(
                    user_question,
                    "PDF",
                    response_time
                )

                st.subheader(
                    "🤖 PDF AI Response"
                )

                st.write(answer)

                st.info(
                    f"⚡ Response Time: {response_time} sec"
                )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

# =========================
# GENERAL AI MODE
# =========================

else:

    if user_question:

        with st.spinner(
            "Generating AI Response..."
        ):

            try:

                start = time.time()

                # SHORT ANSWER PROMPT
                prompt = f"""
                You are a helpful AI assistant.

                Give short, clear, and concise answers.

                Keep answer within 3 to 5 lines only.

                Question:
                {user_question}
                """

                answer = general_llm.invoke(
                    prompt
                )

                end = time.time()

                response_time = round(
                    end - start,
                    2
                )

                # Save logs
                log_chat(
                    user_question,
                    "General",
                    response_time
                )

                st.subheader(
                    "🤖 General AI Response"
                )

                st.write(answer)

                st.info(
                    f"⚡ Response Time: {response_time} sec"
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

# =========================
# ANALYTICS DASHBOARD
# =========================

st.divider()

st.title("📊 AI Analytics Dashboard")

try:

    df = pd.read_csv(
        "analytics/chat_logs.csv"
    )

    total_questions = len(df)

    avg_response = round(
        df["response_time"].mean(),
        2
    )

    pdf_questions = len(
        df[df["mode"] == "PDF"]
    )

    general_questions = len(
        df[df["mode"] == "General"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Questions",
        total_questions
    )

    col2.metric(
        "PDF Questions",
        pdf_questions
    )

    col3.metric(
        "General Questions",
        general_questions
    )

    col4.metric(
        "Avg Response Time",
        f"{avg_response} sec"
    )

    st.subheader(
        "📈 Question Types"
    )

    mode_counts = df[
        "mode"
    ].value_counts()

    st.bar_chart(
        mode_counts
    )

    st.subheader(
        "⚡ Response Time"
    )

    st.line_chart(
        df["response_time"]
    )

    st.subheader(
        "💬 Recent Questions"
    )

    st.dataframe(
        df.tail(10)
    )

except:

    st.info(
        "No analytics data available yet."
    )