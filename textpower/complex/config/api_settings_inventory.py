from textpower.complex.config.api_settings import get_config, set_config

"""⭐cases⭐"""


def llm():
    """获取使用的llm模型类型"""
    return get_config("cases.llm")


def embedding():
    """获取使用的embedding模型类型"""
    return get_config("cases.embedding")


def vector():
    """获取使用的向量库类型"""
    return get_config("cases.vector")


"""⭐keys⭐"""


def keys_openai():
    """获取openai keys"""
    config = get_config("keys.openai")
    return config["OPENAI_API_KEY"]


def keys_spark():
    """获取spark keys"""
    config = get_config("keys.spark")
    return (config["SPARK_APPID"], config["SPARK_API_KEY"], config["SPARK_API_SECRET"])


def keys_qwen():
    """获取qwen keys"""
    config = get_config("keys.qwen")
    return config["QWEN_API_KEY"]


def keys_qianfan():
    """获取qianfan keys"""
    config = get_config("keys.qianfan")
    return (config["QIANFAN_API_KEY"], config["QIANFAN_API_SECRET"])


def keys_baichuan():
    """获取baichuan keys"""
    config = get_config("keys.baichuan")
    return config["BAICHUAN_API_KEY"]


def keys_pinecone():
    """获取pinecone keys"""
    config = get_config("keys.pinecone")
    return config["PINECONE_API_KEY"]


"""⭐lists⭐"""


def lists_llm():
    """获取llm模型列表"""
    return get_config("lists.llm")


def lists_embedding():
    """获取embedding模型列表"""
    return get_config("lists.embedding")


def lists_vector():
    """获取向量库列表"""
    return get_config("lists.vector")


def llm_temperature():
    """获取llm模型温度"""
    list = lists_llm()
    for llms in list:
        if llms["name"] == llm():
            return float(llms["temperature"])
    return None


def embedding_dimensions():
    """获取embedding模型维度"""
    list = lists_embedding()
    for embeddings in list:
        if embeddings["name"] == embedding():
            return int(embeddings["dimensions"])
    return None


"""⭐用户、会话、应用⭐"""


def user_id():
    """获取用户id"""
    return get_config("user.id")


def dialog_id():
    """获取会话id"""
    return get_config("dialog.id")


def app_id():
    """获取应用id"""
    return get_config("app.id")
