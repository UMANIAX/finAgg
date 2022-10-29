from marshmallow_dataclass import dataclass

@dataclass
class HtmlTag:
    tag: str
    type: str