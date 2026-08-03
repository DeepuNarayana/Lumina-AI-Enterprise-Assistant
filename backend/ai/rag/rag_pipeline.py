from ai.embedding_service import EmbeddingService
from ai.vectorstore.chromadb import ChromaDBService
from ai.prompts.prompt_builder import PromptBuilder
from ai.llm.fake_llm import FakeLLM

class RAGPipeline:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_db = ChromaDBService()

        self.prompt_builder = PromptBuilder()

        self.llm = FakeLLM()

    def ask(
        self,
        query: str
    ):

        print("Step 1: Generating query Embedding...")

        querry_embedding = self.embedding_service.generate_embedding(query)

        print("step 2: Retreieving Relevent chunks...")

        results = self.vector_db.search(
            embedding = querry_embedding,
            top_k=5
        )

        retrieved_chunks = results["documents"][0]

        print(f"Retrieved {len(retrieved_chunks)}chunks")

        print("Step3: Building Prompt")

        prompt = self.prompt_builder.build_prompt(
            query=query,
            retrieved_chunks=retrieved_chunks
        )

        print("Step 4 : Calling Fake LLM...")

        response = self.llm.generate_response(prompt)

        return response