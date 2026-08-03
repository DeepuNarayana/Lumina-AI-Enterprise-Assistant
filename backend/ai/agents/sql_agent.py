from app.repositories.sales_repository import SalesRepository


class SQLAgent:

    def __init__(self):
        print("SQL Agent Initialized")

        self.sales_repository=SalesRepository()

    def execute(
        self,
        message: str
    ):
        sales_data = self.sales_repository.get_sales()

        return {
            "agent":"sql",
            "question": "message",
            "sales_data": sales_data
        }