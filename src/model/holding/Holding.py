from dataclasses import dataclass

@dataclass
class Holding:
    name: str
    invested_value: float
    current_value: float
    xirr: float