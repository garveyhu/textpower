import json
import logging
from typing import List

from langchain.memory import ConversationBufferWindowMemory, ConversationSummaryMemory
from langchain_core.messages import BaseMessage, messages_from_dict
from langchain_elasticsearch.chat_history import (
    ElasticsearchChatMessageHistory as BaseElasticsearchChatMessageHistory,
)

from textpower.complex.config.api_settings_inventory import dialog_id
from textpower.feature.llms.llm_creator import LLMCreator
from textpower.feature.manager.elasticsearch import ElasticsearchManager

logger = logging.getLogger(__name__)


class ElasticsearchMemory:
    """Elasticsearch存储聊天历史（只存储上下文文本，不向量化）."""

    def __init__(self):
        self.history = ElasticsearchChatMessageHistory(
            es_connection=ElasticsearchManager().client,
            index="chat_history",
            session_id=dialog_id(),
        )

    def summarize_memory(self, **kwargs):
        """对历史进行LLM总结，生成新的历史上下文."""
        return ConversationSummaryMemory.from_messages(
            llm=LLMCreator().create_llm(),
            chat_memory=self.history,
            return_messages=True,
            **kwargs,
        )

    def buffer_window_memory(self, **kwargs):
        """对历史进行滑动窗口设置，生成窗口大小的历史上下文."""
        return ConversationBufferWindowMemory(
            chat_memory=self.history, return_messages=True, **kwargs
        )


class ElasticsearchChatMessageHistory(BaseElasticsearchChatMessageHistory):
    """Using an external elasticsearch search size"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = 10000

    @property
    def messages(self) -> List[BaseMessage]:
        """Retrieve the messages from Elasticsearch with specified size."""
        try:
            result = self.client.search(
                index=self.index,
                query={"term": {"session_id": self.session_id}},
                sort="created_at:asc",
                size=self.size,
            )
        except Exception as err:
            logger.error(f"Could not retrieve messages from Elasticsearch: {err}")
            raise err

        if result and len(result["hits"]["hits"]) > 0:
            items = [
                json.loads(document["_source"]["history"])
                for document in result["hits"]["hits"]
            ]
        else:
            items = []

        return messages_from_dict(items)
