from langchain_community.embeddings import (
    BaichuanTextEmbeddings as BaseBaichuanEmbeddings,
)

from textpower.complex.config.api_settings_inventory import (
    embedding,
    keys_baichuan,
)


class BaichuanEmbeddings(BaseBaichuanEmbeddings):
    def __init__(self):
        model = embedding()
        baichuan_api_key = keys_baichuan()
        super().__init__(model_name=model, baichuan_api_key=baichuan_api_key)
