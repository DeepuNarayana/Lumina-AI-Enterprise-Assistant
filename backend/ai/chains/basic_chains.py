from app.ai.prompts.prompt_template import general_chat_prompt
from app.ai.llm.fake_llm import llm

chain= general_chat_prompt | llm

if __name__=="__main__":
    response=chain.invoke(
        {
            "question": "what is python"
        }
    )
    print("\n====Final Response====")
    print(response)