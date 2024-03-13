from langchain_elasticsearch import ElasticsearchStore

from textpower.complex.config.api_settings_inventory import dialog_id
from textpower.feature.inventory import elasticsearch, embedding


class ElasticsearchVector:
    """Elasticsearch存储向量（向量化）."""

    def __init__(self):
        self.client = elasticsearch()
        self.embedding = embedding()
        self.dialog_id = dialog_id()

    def dialog_vector(self):
        """会话向量Store"""
        return ElasticsearchStore(
            es_connection=self.client,
            embedding=self.embedding,
            index_name="dialog_" + self.dialog_id,
        )

    def resource_vector(self):
        """资源向量Store"""
        return ElasticsearchStore(
            es_connection=self.client,
            embedding=self.embedding,
            index_name="resource_" + self.dialog_id,
        )
