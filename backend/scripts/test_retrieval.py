import os
import sys

print("Current Working Directory:", os.getcwd())
print("Python Executable:", sys.executable)
print("sys.path:", sys.path)

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from app.rag.retrieval import RetrievalService

retriever = RetrievalService()

results = retriever.search(
    query="What is Leave Poilicy"
)

print("Retrieved Chunks")
print("-" * 40)

print(f"Total Results: {len(results)}")

for index, doc in enumerate(results):
    print(f"\n Chunk {index+1}")
    print(doc.page_content)