from app.services.document_processor import DocumentProcessor

processor = DocumentProcessor()

text = processor.extract_text("sample.pdf")

chunks = processor.chunk_text(text)

print(f"total chunks:{len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n------chunk{i+1}-------")

    print(chunk)
