import chromadb

class ChromaDBService:
    def __init__(self):

        self.client = chromadb.PersistentClient(
            path = "./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name = "documents"
        )

    def store_documents(
        self,
        document_id,
        chunks,
        embeddings
    ):
        ids = []

        metadatas = []

        documents = []

        for index, chunk in enumerate(chunks):
            ids.append(f"{document_id}_{index}")
            metadatas.append({
                "document_id": document_id,
                "chunk": index
            })

            documents.append(chunk)

        self.collection.add(
            ids=ids,
            embeddings = embeddings,
            metadatas = metadatas,
            documents = documents
        )
