from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from textpower.feature.inventory import (
    es_buffer_window_memory,
    es_resource_vector,
    llms,
)
from textpower.function.prompts.chat import CONTEXT_PROMPT, HISTORY_PROMPT


class ChatChains:
    def call(self, text):
        chain = llms() | StrOutputParser()

        return chain.invoke(text)

    def conversation(self, text):
        memory = es_buffer_window_memory(k=5)
        chain = (
            RunnablePassthrough.assign(
                history=RunnableLambda(memory.load_memory_variables)
                | itemgetter("history")
            )
            | HISTORY_PROMPT
            | llms()
            | StrOutputParser()
        )
        response = chain.invoke({"input": text})
        memory.save_context({"input": text}, {"output": response})

        return response

    def rag(self, text):
        retriever = es_resource_vector().as_retriever()
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | CONTEXT_PROMPT
            | llms()
            | StrOutputParser()
        )

        return chain.invoke(text)
