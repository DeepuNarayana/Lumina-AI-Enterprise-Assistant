from ai.agents.planner import PlannerAgent
from ai.agents.llm_agents import LLMAgent

class AIService:
    def __init__(self):
        self.planner=PlannerAgent()
        self.llm=LLMAgent()

    def process_message(self, message:str):
        intent=self.planner.route(message)
        #route=self.planner.route(message)

        print(f"Agent: {intent.agent}")
        print(f"Confidence: {intent.confidence}")
        print(f"Reason: {intent.reason}")

        if intent.agent == "sql":
            return "SQL Agent will answer this request"

        elif intent.agent == "rag":
            return "RAG agent will answer this request"
        else:
            return self.llm.generate(message)