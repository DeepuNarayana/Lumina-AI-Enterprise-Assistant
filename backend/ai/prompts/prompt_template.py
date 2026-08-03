from langchain_core.prompts import PromptTemplate

general_chat_prompt=PromptTemplate(
    input_variables=["question"],
    template="""
    You are Lumina AI Assistant,

    You are helpful Assistant

    Answer the user question proffessionally

    User Question:
    {question}

    Answer:
    """
)

if __name__=="__main__":
    prompt =  general_chat_prompt.invoke(
        {
            "question": "what is python?"
        }
    )
    print(prompt)