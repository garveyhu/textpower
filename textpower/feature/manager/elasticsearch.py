from elasticsearch import Elasticsearch

from textpower.complex.config.system_settings import system_settings


class ElasticsearchManager:
    _pool = None

    @classmethod
    def initialize_pool(cls):
        if cls._pool is None:
            es_url = system_settings.ELASTICSEARCH_URL
            es_username = system_settings.ELASTIC_USERNAME
            es_password = system_settings.ELASTIC_PASSWORD
            if es_username and es_password:
                cls._pool = Elasticsearch(es_url, http_auth=(es_username, es_password))
            else:
                cls._pool = Elasticsearch(es_url)

    def __init__(self):
        self.__class__.initialize_pool()
        self.client = self.__class__._pool
