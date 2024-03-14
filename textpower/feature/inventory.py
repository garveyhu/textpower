from textpower.feature.embeddings.embedding_creator import EmbeddingCreator
from textpower.feature.llms.llm_creator import LLMCreator
from textpower.feature.manager.elasticsearch import ElasticsearchManager
from textpower.feature.manager.redis import RedisManager
from textpower.feature.memory.elasticsearch import ElasticsearchMemory
from textpower.feature.memory.redis import RedisMemory
from textpower.feature.vector.elasticsearch import ElasticsearchVector
from textpower.feature.vector.pinecone import PineconeVector

"""⭐embeddings⭐"""


def embedding():
    """`EmbeddingCreator`
    获取embedding模型
    """
    return EmbeddingCreator.create_embedding()


"""⭐llms⭐"""


def llm():
    """`LLMCreator`
    获取llm模型
    """
    return LLMCreator().create_llm()


"""⭐manager⭐"""


def elasticsearch():
    """`ElasticsearchManager`
    获取elasticsearch客户端
    """
    return ElasticsearchManager().client


def redis():
    """`RedisManager`
    获取redis客户端
    """
    return RedisManager().client


"""⭐memory⭐"""


def es_summarize_memory(**kwargs):
    """`ElasticsearchMemory`
    对历史进行LLM总结，生成新的历史上下文

    Example:
        .. code-block:: python

            from langchain.chains import ConversationChain
            from textpower.feature.inventory import es_summarize_memory

            memory = es_summarize_memory()
            conversation_chain = ConversationChain(llm=llm, verbose=True, memory=memory)
            result = conversation_chain.predict(input=text)

    Args:
        buffer: str = ""
        memory_key: str = "history"
    """
    return ElasticsearchMemory().summarize_memory(**kwargs)


def es_buffer_window_memory(**kwargs):
    """`ElasticsearchMemory`
    对历史进行滑动窗口设置，生成窗口大小的历史上下文

    Example:
        .. code-block:: python

            from langchain.chains import ConversationChain
            from textpower.feature.inventory import es_buffer_window_memory

            memory = es_buffer_window_memory(k=3)
            conversation_chain = ConversationChain(llm=llm, verbose=True, memory=memory)
            result = conversation_chain.predict(input=text)

    Args:
        human_prefix: str = "Human"
        ai_prefix: str = "AI"
        memory_key: str = "history"
        k: int = 5
    """
    return ElasticsearchMemory().buffer_window_memory(**kwargs)


def redis_summarize_memory(**kwargs):
    """`RedisMemory`
    对历史进行LLM总结，生成新的历史上下文

    Example:
        .. code-block:: python

            from langchain.chains import ConversationChain
            from textpower.feature.inventory import redis_summarize_memory

            memory = redis_summarize_memory()
            conversation_chain = ConversationChain(llm=llm, verbose=True, memory=memory)
            result = conversation_chain.predict(input=text)

    Args:
        buffer: str = ""
        memory_key: str = "history"
    """
    return RedisMemory().summarize_memory(**kwargs)


def redis_buffer_window_memory(**kwargs):
    """`RedisMemory`
    对历史进行滑动窗口设置，生成窗口大小的历史上下文

    Example:
        .. code-block:: python

            from langchain.chains import ConversationChain
            from textpower.feature.inventory import redis_buffer_window_memory

            memory = redis_buffer_window_memory(k=3)
            conversation_chain = ConversationChain(llm=llm, verbose=True, memory=memory)
            result = conversation_chain.predict(input=text)

    Args:
        human_prefix: str = "Human"
        ai_prefix: str = "AI"
        memory_key: str = "history"
        k: int = 5
    """
    return RedisMemory().buffer_window_memory(**kwargs)


"""⭐vector⭐"""


def es_dialog_vector():
    """`ElasticsearchVector`
    会话向量Store

    Example:
        .. code-block:: python

            from textpower.feature.inventory import es_dialog_vector
            from textpower.feature.vector.elasticsearch import ElasticsearchVector

            db = es_dialog_vector()
            db.add_documents(content)
            db.client.indices.refresh(index=ElasticsearchVector.dialog_index())

    """
    return ElasticsearchVector().dialog_vector()


def es_resource_vector():
    """`ElasticsearchVector`
    资源向量Store

    Example:
        .. code-block:: python

            from textpower.feature.inventory import es_resource_vector
            from textpower.feature.vector.elasticsearch import ElasticsearchVector

            db = es_resource_vector()
            db.add_documents(content)
            db.client.indices.refresh(index=ElasticsearchVector.resource_index())
    """
    return ElasticsearchVector().resource_vector()


def pinecone_vector():
    """Pinecone存储向量（向量化）.

    Example:
        .. code-block:: python

            from textpower.feature.inventory import pinecone_vector

            db = pinecone_vector()
            db.add_documents(content)
    """

    return PineconeVector().pinecone_vector()
