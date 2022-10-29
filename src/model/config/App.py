from marshmallow_dataclass import dataclass
from model.config.LoginHtmlTags import LoginHtmlTags

@dataclass
class App:
    login_html_tags: LoginHtmlTags
    landing_page: str