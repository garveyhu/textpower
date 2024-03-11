from textpower.complex.config.api_settings_inventory import embedding
from textpower.feature.models.embeddings.baichuan import BaichuanEmbeddings
from textpower.feature.models.embeddings.openai import OpenAIEmbeddings
from textpower.feature.models.embeddings.qianfan import QianfanEmbeddings
from textpower.feature.models.embeddings.qwen import QwenEmbeddings


class EmbeddingCreator:
    embeddings = {
        "text-embedding-3-large": OpenAIEmbeddings,
        "text-embedding-3-small": OpenAIEmbeddings,
        "text-embedding-ada-002": OpenAIEmbeddings,
        "Embedding-V1": QianfanEmbeddings,
        "Baichuan-Text-Embedding": BaichuanEmbeddings,
        "text-embedding-v1": QwenEmbeddings,
    }

    @classmethod
    def create_embedding(cls, embedding_type=None):
        if embedding_type is None:
            embedding_type = embedding()

        embedding_class = cls.embeddings.get(embedding_type)
        if not embedding_class:
            raise ValueError(f"No embedding class found for type {embedding_type}")

        return embedding_class()


def get_embedding():
    return EmbeddingCreator.create_embedding()
