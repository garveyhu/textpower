from langchain_openai import OpenAIEmbeddings as BaseOpenAIEmbeddings

from textpower.complex.config.api_settings_inventory import (
    embedding,
    embedding_dimensions,
    keys_openai,
)


class OpenAIEmbeddings(BaseOpenAIEmbeddings):
    def __init__(self):
        model = embedding()
        openai_key = keys_openai()
        dimensions = embedding_dimensions()
        super().__init__(model=model, openai_key=openai_key, dimensions=dimensions)
