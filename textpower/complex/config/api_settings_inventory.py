from textpower.complex.config.api_settings import get_config, set_config


"""cases"""


def chat():
    """获取使用的chat模型类型"""
    return get_config("cases.chat")


def embedding():
    """获取使用的embedding模型类型"""
    return get_config("cases.embedding")


def vector():
    """获取使用的向量库类型"""
    return get_config("cases.vector")


"""lists"""


def lists_chat():
    """获取chat模型列表"""
    return get_config("lists.chat")


def lists_embedding():
    """获取embedding模型列表"""
    return get_config("lists.embedding")


def lists_vector():
    """获取向量库列表"""
    return get_config("lists.vector")


def model_temperature():
    """获取模型温度"""
    list = lists_chat()
    for chats in list:
        if chats["name"] == chat():
            return float(chats["temperature"])
    return None


"""keys"""


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


def keys_ernie():
    """获取ernie keys"""
    config = get_config("keys.ernie")
    return (config["ERNIE_API_KEY"], config["ERNIE_API_SECRET"])


def keys_pinecone():
    """获取pinecone keys"""
    config = get_config("keys.pinecone")
    return config["PINECONE_API_KEY"]


"""修改配置"""


def set_model_temperature(temperature):
    """修改温度"""
    list = lists_chat()
    for chats in list:
        if chats["name"] == chat():
            chats["temperature"] = temperature


"""用户、会话、应用"""


def user_id():
    """获取用户id"""
    return get_config("user.id")


def dialog_id():
    """获取会话id"""
    return get_config("dialog.id")


def app_id():
    """获取应用id"""
    return get_config("app.id")
