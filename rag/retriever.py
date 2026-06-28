from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
	model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_retriever():
	vectorstore = FAISS.load_local(
		"faiss_index",
		embeddings,
		allow_dangerous_deserialization=True,
	)

	return vectorstore.as_retriever(search_kwargs={"k": 3})
