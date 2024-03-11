from textpower.complex.config.api_settings_inventory import llm
from textpower.feature.models.llms.baichuan_chat import BaichuanChat
from textpower.feature.models.llms.openai import OpenAI
from textpower.feature.models.llms.openai_chat import OpenAIChat
from textpower.feature.models.llms.qianfan_chat import QianfanChat
from textpower.feature.models.llms.qwen import Qwen
from textpower.feature.models.llms.spark import Spark


class LLMCreator:
    llms = {
        # chat models
        "text-davinci-003": OpenAIChat,
        "gpt-3.5-turbo": OpenAIChat,
        "gpt-3.5-turbo-16k": OpenAIChat,
        "gpt-3.5-turbo-1106": OpenAIChat,
        "gpt-3.5-turbo-1106": OpenAIChat,
        "gpt-4": OpenAIChat,
        "gpt-4-32k": OpenAIChat,
        "gpt-4-turbo-preview": OpenAIChat,
        "ERNIE-Bot-turbo": QianfanChat,
        "ERNIE-4.0-8K": QianfanChat,
        "Baichuan2-Turbo-192K": BaichuanChat,
        # llm models
        "gpt-3.5-turbo-instruct": OpenAI,
        "spark-v2": Spark,
        "spark-v3": Spark,
        "spark-v3.5": Spark,
        "qwen-turbo": Qwen,
        "qwen-plus": Qwen,
    }

    @classmethod
    def create_llm(cls, llm_type=None):
        if llm_type is None:
            llm_type = llm()

        llm_class = cls.llms.get(llm_type)
        if not llm_class:
            raise ValueError(f"No llm class found for type {llm_type}")

        return llm_class()


def get_llm():
    return LLMCreator().create_llm()
