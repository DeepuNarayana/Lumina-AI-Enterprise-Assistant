from ai.models.intent import Intent

SQL_KEYWORDS=[
    "sales",
    "revenue",
    "candidate",
    "employee",
    "store",
    "report",
    "database"
]

RAG_KEYWORDS=[
    "policy",
    "document",
    "pdf",
    "leave",
    "company",
    "guideline"
]

class PlannerAgent:
    def route(self, message:str)->Intent:

        text=message.lower()
        #message=message.lower()
        #if "sales" in text:
        if any(word in text for word in SQL_KEYWORDS):

            return Intent(
                agent="sql",
                confidence=0.98,
                reason="Structured enterprise data requested"
            )
        elif any(word in text for word in RAG_KEYWORDS):
        #elif "document" in text or "pdf" in text:
            return Intent(
                agent="rag",
                confidence=0.95,
                reason="Knowledge retrival from documents required"
                )
        else:
            return Intent(
                agent="llm",
                confidence=0.92,
                reason="General Conversational request"
            )

