from marshmallow_dataclass import dataclass
from model.creds.AppCreds import AppCreds

@dataclass
class Creds:
    icici: AppCreds
    groww: AppCreds