from ai.chunking.chunk_service import ChunkService


def test_chunking():

    service = ChunkService()

    text = (
        "Python is a programming language. " * 300
    )

    chunks = service.split_text(text)

    print(f"Total Chunks: {len(chunks)}")

    assert len(chunks) > 1

    assert len(chunks[0]) <= 1200