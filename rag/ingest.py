import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.vector_store import create_vector_store

KNOWLEDGE_PATH = "knowledge_base"

def load_documents():
    documents = []

    for root, _, files in os.walk(KNOWLEDGE_PATH):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                loader = TextLoader(path, encoding="utf-8")
                documents.extend(loader.load())

    return documents

def build_vector_db():
    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    vectorstore = create_vector_store(chunks)

    vectorstore.save_local("faiss_index")

    print("FAISS index created successfully!")


if __name__ == "__main__":
    build_vector_db()
