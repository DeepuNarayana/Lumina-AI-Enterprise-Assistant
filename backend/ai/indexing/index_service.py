from ai.document_processor import DocumentProcessor
from ai.chunking.chunk_service import ChunkService
from ai.embedding_service import EmbeddingService
from ai.vectorstore.chromadb import ChromaDBService
import uuid

class IndexService:

    def __init__(self):
        self.processor = DocumentProcessor()

        self.chunker = ChunkService()

        self.embedding_service = EmbeddingService()

        self.vector_db = ChromaDBService()

    def index_document(self, file_path: str):

        print("Extracting Text....")

        text = self.processor.extract_text(file_path)

        print("Chunking Text....")

        chunks = self.chunker.split_text(text)

        print(f"Chunks Created:{len(chunks)}")

        print("Generating Embeddings...")

        embeddings = self.embedding_service.generate_embeddings(chunks)

        print("Storing in ChromaDB....")

        document_id = str(uuid.uuid4())

        # index_service.index_document(
        #     document_id
        # )

        self.vector_db.store_documents(
            document_id=document_id,
            chunks=chunks,
            embeddings=embeddings
        )

        print("Indexing Completed...")

