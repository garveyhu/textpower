from textpower.complex.config.api_settings_inventory import llm
from textpower.feature.models.llms.openai import OpenAI


class LLMCreator:
    llms = {
        "gpt-3.5-turbo-instruct": OpenAI,
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
