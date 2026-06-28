from rag.retriever import get_retriever

retriever = get_retriever()

query = "When should I use microservices architecture?"

docs = retriever.invoke(query)

for i, doc in enumerate(docs):
	print(f"\n--- Result {i+1} ---\n")
	print(doc.page_content)
