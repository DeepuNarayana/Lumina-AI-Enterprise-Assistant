from ai.llm.fake_llm import FakeLLM


def test_fake_llm():

    llm = FakeLLM()

    prompt = """
Context:
Employees receive 12 Casual Leaves annually.

Question:
How many casual leaves do employees get?
"""

    response = llm.generate_response(prompt)

    print(response)

    assert "12 Casual Leaves" in response