class PromptBuilder:
    def build_prompt(
        self,
        message:str
    )-> str:

        prompt= f"""
You are Lumina AI, an Enterprise AI Assistant.

Role:
- Help employees professionally.
- Answer business-related questions.
- Be concise and accurate.
- If you don't know something, clearly say so.
- Never generate harmful or misleading content.

User Question:
{message}

"""
        return prompt.strip()
