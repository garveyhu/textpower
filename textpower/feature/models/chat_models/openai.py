from langchain_openai import ChatOpenAI as BaseOpenAIChat

from textpower.complex.config.api_settings_inventory import (
    chat,
    chat_temperature,
    keys_openai,
)


class OpenAIChat(BaseOpenAIChat):
    def __init__(self):
        model = chat()
        openai_api_key = keys_openai()
        temperature = chat_temperature()
        super().__init__(
            model=model, openai_api_key=openai_api_key, temperature=temperature
        )
