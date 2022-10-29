from dataclasses import dataclass
from model.holding.Holding import Holding

@dataclass
class Portfolio(Holding):
    funds: list