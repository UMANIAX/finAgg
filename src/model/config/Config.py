from marshmallow_dataclass import dataclass
from model.config.CredsConfig import CredsConfig
from model.config.Web import Web
from model.config.groww.GrowwApp import GrowwApp
from model.config.icici.IciciApp import IciciApp

@dataclass
class Config:
    icici: IciciApp
    groww: GrowwApp
    creds: CredsConfig
    web: Web