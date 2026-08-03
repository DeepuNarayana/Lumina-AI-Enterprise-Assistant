from ai.clients.bedrock_client import BedrockClient
from ai.prompts.prompt_template import general_chat_prompt

class LLMAgent:

    def __init__(self):
        #print("LLM Agent Initialized")
        self.client=BedrockClient()

    def execute(
        self,
        message: str
    ):
        prompt = general_chat_prompt.invoke(

            {
                "question": message
            }
        )

        response = self.client.invoke(
            prompt.text
        )

        return {
            "response": response["content"][0]["text"]
        }

        # return self.client.invoke(
        #     prompt.text
        # )
        # return {
        #     "agent":"llm",
        #     "question": message,
        #     "response": f"AI Response: I understand your question {message}"
        # }
    # def generate(self, message:str):
    #     return f"AI Response: I understand your question {message}"
