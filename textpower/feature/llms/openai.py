from langchain_openai import OpenAI as BaseOpenAI

from textpower.complex.config.api_settings_inventory import (
    keys_openai,
    llm,
    llm_temperature,
)


class OpenAI(BaseOpenAI):
    def __init__(self):
        model = llm()
        openai_api_key = keys_openai()
        temperature = llm_temperature()
        super().__init__(
            model=model, openai_api_key=openai_api_key, temperature=temperature
        )
