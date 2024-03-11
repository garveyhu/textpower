from langchain_community.chat_models import ChatBaichuan as BaseBaichuanChat

from textpower.complex.config.api_settings_inventory import (
    chat,
    chat_temperature,
    keys_baichuan,
)


class BaichuanChat(BaseBaichuanChat):
    def __init__(self):
        model = chat()
        baichuan_api_key = keys_baichuan()
        temperature = chat_temperature()
        super().__init__(
            model=model, baichuan_api_key=baichuan_api_key, temperature=temperature
        )
