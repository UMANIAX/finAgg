from typing import Optional
from marshmallow_dataclass import dataclass
from model.config.HtmlTag import HtmlTag

@dataclass
class LoginHtmlTags:
    username: HtmlTag
    username_continue: Optional[HtmlTag]
    password: HtmlTag
    submit: HtmlTag
    pin: Optional[HtmlTag]