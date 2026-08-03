
class PromptBuilder:

    def build_prompt(
        self,
        query: str,
        retrieved_chunks: list[str]
    ):

        context = "\n\n".join(retrieved_chunks)

        prompt= f"""
You are an intelligent AI Enterprise Assistant.

Answer ONLY using the context below.

If the answer is not present in the context, reply:

"I couldn't find this information in the provided documents."

----------------------
context:
{context}
----------------------

Question:
{query}

Answer:
"""
        return prompt
