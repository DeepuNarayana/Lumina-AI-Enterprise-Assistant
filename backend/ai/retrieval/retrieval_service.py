from ai.embedding_service import EmbeddingService
from ai.vectorstore.chromadb import ChromaDBService

class RetrievalService:
    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_db = ChromaDBService()

    def retrieve(
        self,
        query: str,
        top_k: int= 5
    ):
        print("Generating Querry Embedding....")

        query_embedding = self.embedding_service.generate_embedding(query)

        print("Searching ChromaDB.....")

        results = self.vector_db.search(
            embedding = query_embedding,
            top_k=top_k
        )

        return results


