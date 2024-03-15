from langchain_pinecone import PineconeVectorStore

from textpower.complex.config.api_settings_inventory import keys_pinecone
from textpower.feature.inventory import embeddings


class PineconeVector:
    """Pinecone存储向量（向量化）."""

    def __init__(self):
        self.api_key = keys_pinecone()
        self.embedding = embeddings()

    def pinecone_vector(self):
        """会话向量Store"""
        return PineconeVectorStore(
            pinecone_api_key=self.api_key,
            embedding=self.embedding,
            index_name="langchain",
        )
