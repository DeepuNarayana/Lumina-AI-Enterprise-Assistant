class SalesRepository:
    def __init__(self):
        print("Sales Repository Initialized")

    def get_sales(
        self
    ):
        """
        Temporary implementation,
        Later this will query Postgresql.
        """

        return [
            {
                "customer": "ABC Retail",
                "amount": 1000,
                "region": "South"
            },
            {
                "customer": "ZYX Mart",
                "amount": 20000,
                "region": "North"
            }
        ]
