from langchain_ollama import OllamaEmbeddings

# =========================
# LOAD EMBEDDING MODEL
# =========================

def get_embedding_model():

    embeddings = OllamaEmbeddings(

        # Embedding model
        model="nomic-embed-text",

        # FIXED Windows localhost issue
        base_url="http://127.0.0.1:11434"

    )

    return embeddings