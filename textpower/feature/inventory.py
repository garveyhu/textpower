from textpower.feature.embeddings.embedding_creator import EmbeddingCreator
from textpower.feature.llms.llm_creator import LLMCreator
from textpower.feature.manager.elasticsearch import ElasticsearchManager
from textpower.feature.manager.redis import RedisManager
from textpower.feature.memory.elasticsearch import ElasticsearchMemory

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
