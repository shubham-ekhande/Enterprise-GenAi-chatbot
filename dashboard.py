import streamlit as st
import pandas as pd

st.title("📊 AI Analytics Dashboard")

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

# CHARTS


st.subheader("📈 Question Types")

mode_counts = df["mode"].value_counts()

st.bar_chart(mode_counts)


# RESPONSE TIME


st.subheader("⚡ Response Time")

st.line_chart(
    df["response_time"]
)


# RECENT QUESTIONS


st.subheader("💬 Recent Questions")

st.dataframe(df.tail(10))