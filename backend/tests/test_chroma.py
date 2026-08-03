from ai.vectorstore.chromadb import ChromaService

service = ChromaService()

chunks = [
    "Hello Deepu",
    "Lumina AI Assistant"
]

embeddings = [
    [0.1] * 384,

    [0.2] * 384
]

service.store_document(
    document_id="123",

    chunks = chunks,

    embeddings= embeddings
)

print("Stored Successfully")