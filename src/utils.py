import json
from types import SimpleNamespace

from model.config.Config import Config

def get_config() -> Config:
    file_path = 'src/config.json'
    with open(file_path, 'rb') as file:
        config_json = file.read().decode('utf-8')
    config = Config.Schema().loads(config_json)
    return config