from marshmallow_dataclass import dataclass
from model.config.App import App
from model.config.groww.GrowwHtmlTags import GrowwHtmlTags

@dataclass
class GrowwApp(App):
    mf_tags: GrowwHtmlTags
    mf_network_data_uri: str