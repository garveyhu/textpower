from langchain_community.chat_models import QianfanChatEndpoint as BaseQianfanChat

from textpower.complex.config.api_settings_inventory import (
    chat,
    chat_temperature,
    keys_qianfan,
)


class QianfanChat(BaseQianfanChat):
    def __init__(self):
        model = chat()
        qianfan_ak, qianfan_sk = keys_qianfan()
        temperature = chat_temperature()
        super().__init__(
            model=model,
            qianfan_ak=qianfan_ak,
            qianfan_sk=qianfan_sk,
            temperature=temperature,
        )
