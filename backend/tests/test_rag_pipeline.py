from ai.rag.rag_pipeline import RAGPipeline


def test_rag_pipeline():

    pipeline = RAGPipeline()

    response = pipeline.ask(
        "How many casual leaves do employees get?"
    )

    print(response)

    assert "FAKE LLM RESPONSE" in response