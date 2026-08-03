from langchain_core.runnables import RunnableLambda

def fake_model(prompt):
    return f"""

claude Response

-----------------
{prompt}

"""
def fake_llm(prompt):
    print("\n=====prompt Recived by Fake LLM=====\n")
    print(prompt)

    return "this is fake AI Response"
llm=RunnableLambda(fake_llm)