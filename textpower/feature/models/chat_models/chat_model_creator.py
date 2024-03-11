from textpower.complex.config.api_settings_inventory import chat
from textpower.feature.models.chat_models.baichuan import BaichuanChat
from textpower.feature.models.chat_models.openai import OpenAIChat
from textpower.feature.models.chat_models.qianfan import QianfanChat
from textpower.feature.models.chat_models.qwen import QwenChat
from textpower.feature.models.chat_models.spark import SparkChat


class ChatModelCreator:
    chat_models = {
        "text-davinci-003": OpenAIChat,
        "gpt-3.5-turbo": OpenAIChat,
        "gpt-3.5-turbo-16k": OpenAIChat,
        "gpt-3.5-turbo-1106": OpenAIChat,
        "gpt-4": OpenAIChat,
        "gpt-4-32k": OpenAIChat,
        "gpt-3.5-turbo-1106": OpenAIChat,
        "gpt-4-turbo-preview": OpenAIChat,
        "ERNIE-Bot-turbo": QianfanChat,
        "ERNIE-4.0-8K": QianfanChat,
        "Baichuan2-Turbo-192K": BaichuanChat,
        "spark-v2": SparkChat,
        "spark-v3": SparkChat,
        "spark-v3.5": SparkChat,
        "qwen-turbo": QwenChat,
        "qwen-plus": QwenChat,
    }

    @classmethod
    def create_chat_model(cls, chat_model_type=None):
        if chat_model_type is None:
            chat_model_type = chat()

        chat_model_class = cls.chat_models.get(chat_model_type)
        if not chat_model_class:
            raise ValueError(f"No chat model class found for type {chat_model_type}")

        return chat_model_class()


def get_chat_model():
    return ChatModelCreator.create_chat_model()
