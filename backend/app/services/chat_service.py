from ai.agents.planner import PlannerAgent
from ai.factory.agent_factory import AgentFactory
#from ai.agents.sql_agent import SQLAgent


class ChatService:

    def __init__(self):
        self.planner=PlannerAgent()

        self.factory =AgentFactory()

        #self.sql_agent= SQLAgent()

    def process(
        self,
        message: str
    ):
        intent=self.planner.route(message)

        print(f"Planner Selected-> {intent.agent}")

        agent=self.factory.get_agent(
            intent.agent
        )

        return agent.execute(message)

        # if intent.agent == "sql":
        #     return self.sql_agent.execute(message)

        # return {
        #     "agent": intent.agent,
        #     "response": "other Agents will be implemented next"
        # }

        # #logger.info(
        # #    f"Planner Selected Agent : {intent.agent}"
        # #)
        # print(intent)
        # return intent
