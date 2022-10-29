from dataclasses import dataclass
from model.holding.Holding import Holding

@dataclass
class MfFund(Holding):
    units: int
    category: str
    on_sip: str