from langchain_ollama import OllamaLLM

# =========================
# CREATE RAG CHAIN
# =========================

def create_rag_chain(vectorstore):

    # Load local LLM
    llm = OllamaLLM(

        model="llama3.2:1b",

        base_url="http://127.0.0.1:11434"
    )

    # Retriever
    retriever = vectorstore.as_retriever()

    # Simple custom RAG function
    def qa_chain(question):

        # Retrieve relevant docs
        docs = retriever.invoke(question)

        # Combine context
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # Prompt
        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        # Generate answer
        response = llm.invoke(prompt)

        return response

    return qa_chain