from io import StringIO

from langchain_text_splitters import CharacterTextSplitter

from textpower.complex.config.api_settings_inventory import llm
from textpower.complex.schema.chats import ChatList
from textpower.complex.utils.convert_util import chatlist_to_chats, chats_to_docs
from textpower.feature.inventory import es_dialog_vector, es_resource_vector
from textpower.feature.vector.elasticsearch import ElasticsearchVector


class ElasticSearchChat:
    """ES存储聊天记录"""

    def __init__(self):
        self.db = es_dialog_vector()
        self.index_name = ElasticsearchVector.dialog_index()

    def store_chat(self, chats: ChatList):
        docs = chats_to_docs(chatlist_to_chats(chats))
        for doc in docs:
            doc.metadata["llm_type"] = llm()
        self.db.add_documents(docs)
        self.db.client.indices.refresh(index=self.index_name)


class ElasticSearchResource:
    """ES存储文件资源"""

    def __init__(self):
        self.db = es_resource_vector()
        self.index_name = ElasticsearchVector.resource_index()

    def store_resource(self, resource: StringIO):
        file_content = resource.read()
        text_splitter = CharacterTextSplitter(
            chunk_size=1000, chunk_overlap=0, separator="\n"
        )
        docs = text_splitter.create_documents([file_content])
        for paragraph in docs:
            paragraph.metadata["type"] = "file"
        self.db.add_documents(docs)
        self.db.client.indices.refresh(index=self.index_name)
