from marshmallow_dataclass import dataclass
from model.config.HtmlTag import HtmlTag

@dataclass
class GrowwHtmlTags:
    mf_nav_bar: HtmlTag
    mf_investments: HtmlTag