from rag.retriever import get_retriever

retriever = get_retriever()


class KnowledgeService:

    def search(self, query: str):

        docs = retriever.invoke(query)

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )


knowledge_service = KnowledgeService()