# from dataclasses import dataclass

# @dataclass
class Intent:
    def __init__(
        self,
        agent : str,
        confidence : float,
        reason : str
    ):
        self.agent = agent
        self.confidence = confidence
        self.reason = reason