import json

class BedrockClient:

    def __init__(self):
        print("Bedrock Client Initialized")

    def invoke(
        self,
        prompt: str
    ):
        print("=======Prompt=======")
        print(prompt)
        print("====================")

        response={
            "content":[
                {
                    "text": "This response came from the mocked Bedrock client."
                }
            ]

        }

        return response
