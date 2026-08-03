from app.services.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

embedding = embedding_service.generate_embedding(
    "Hello Deepu"
)

print(type(embedding))

print(len(embedding))

print(embedding[:10])