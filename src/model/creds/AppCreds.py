from typing import Optional
from marshmallow_dataclass import dataclass

@dataclass
class AppCreds:
    username: str
    password: str
    pin: Optional[str]