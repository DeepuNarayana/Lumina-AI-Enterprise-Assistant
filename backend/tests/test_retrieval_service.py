from ai.retrieval.retrieval_service import RetrievalService

def test_retrieval():

    retriever = RetrievalService()

    results = retriever.retrieve(
        "How many casual leaves do employee get?"
    )

    assert len(results["documents"][0]) > 0

    print(results["documents"])
