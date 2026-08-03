from sentence_transformers import SentenceTransformer

class EmbeddingService:

    def __init__(self):
        #Load model once

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def generate_embedding(
        self,
        text: str
    ):
        """
        Generating Embedding for one chunk.
        """

        embedding = self.model.encode(
            text
        )

        return embedding.tolist()


    def generate_embeddings(
        self,
        chunks: list[str]
    ):
        """
        Generating embeddings for all chunks
        """

        embeddings = self.model.encode(
            chunks
        )

        return embeddings.tolist()
