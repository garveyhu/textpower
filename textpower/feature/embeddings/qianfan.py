from langchain_community.embeddings import QianfanEmbeddingsEndpoint as BaseQianfanEmbeddings

from textpower.complex.config.api_settings_inventory import (
    embedding,
    keys_qianfan,
)


class QianfanEmbeddings(BaseQianfanEmbeddings):
    def __init__(self):
        model = embedding()
        qianfan_ak, qianfan_sk = keys_qianfan()
        super().__init__(model=model, qianfan_ak=qianfan_ak, qianfan_sk=qianfan_sk)