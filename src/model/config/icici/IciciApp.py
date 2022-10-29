from marshmallow_dataclass import dataclass
from model.config.App import App
from model.config.icici.IciciHtmlTags import IciciHtmlTags

@dataclass
class IciciApp(App):
    icici_tags: IciciHtmlTags