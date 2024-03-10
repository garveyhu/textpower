import json

from textpower.complex.config.api_settings import init_config
from textpower.complex.config.system_settings import config_json


def init_with_file():
    with config_json.open() as f:
        config_data = json.load(f)

    init_config(config_data)
