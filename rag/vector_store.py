from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def create_vector_store(docs):
    """"
    docs: List of Lngchain Document objects
    """
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store