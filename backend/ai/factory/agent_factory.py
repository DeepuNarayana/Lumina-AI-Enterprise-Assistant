from ai.agents.sql_agent import SQLAgent
from ai.agents.llm_agent import LLMAgent

class AgentFactory:

    def __init__(self):

        self._agents ={
            "sql": SQLAgent(),
            "llm": LLMAgent()

        }

    def get_agent(
        self,
        agent_name:str
    ):
        agent= self._agents.get(agent_name)

        if not agent:
            raise ValueError(
                f"unknown agent:{agent_name}"
            )
        return agent


