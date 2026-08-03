import fitz

class DocumentProcessor:
    def extract_text(self, file_path: str)->str:

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    def chunk_text(
        self,
        text: str,
        chunk_size: int=500,
        over_lap: int=100
    ):
        """
        Split Extracted text into overlapping chunks
        """
        chunks=[]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(text[start:end])

            start += chunk_size - over_lap

        return chunks

