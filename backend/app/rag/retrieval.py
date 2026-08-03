from langchain_chroma import Chroma
#from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings

class RetrievalService:

    def __init__(self):

        # self.embedding_model= SentenceTransformer(
        #     "sentence-transformers/all-MiniLM-L6-V2"
        # )
        embeddings = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/all-MiniLM-L6-V2"
        )

        self.vector_store = Chroma(
            persist_directory = "chroma_db",
            embedding_function = embeddings
        )

    def search(
        self,
        query: str,
        k:int =3
    ):
        results = self.vector_store.similarity_search(
            query=query,
            k=k
        )
        return results
