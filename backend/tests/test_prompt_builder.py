from ai.prompts.prompt_builder import PromptBuilder

def test_prompt_builder():
    builder = PromptBuilder()

    chunks =[
        "Employees receive 12 Casual Leaves annually.",
        "Carry forward limit is 5 leaves."
    ]

    prompt = builder.build_prompt(
        query= "How many casual leaves do employee get?",
        retrieved_chunks= chunks
    )

    print(prompt)

    assert "12 Casual Leaves" in prompt
    assert "How many casual leaves" in prompt