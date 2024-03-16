from typing import List

from langchain.schema.document import Document

from textpower.complex.schema.chats import ChatList


def chatlist_to_chats(chats: ChatList):
    return [chat.model_dump() for chat in chats.chats]


def chats_to_docs(chats: List[dict]):
    """聊天记录chats转换为langchain文档Document格式

    Example:
            input:
                [
                    {
                        "page_content": "塞尔达有哪些探索技巧？",
                        "metadata": {
                            "sender": "Human",
                            "receiver": "AI",
                            "timestamp": "2023-11-07T12:05:00",
                            "type": "message"
                        }
                    },
                    {
                        "page_content": "游戏基本上没有设计固定的线路让你前进，要如何选择前进的道路完全取决于你的选择。",
                        "metadata": {
                            "sender": "AI",
                            "receiver": "Human",
                            "timestamp": "2023-11-07T12:05:03",
                            "type": "message"
                        }
                    }
                ]

            output:
                [
                    Document(
                        page_content="塞尔达有哪些探索技巧？",
                        metadata={
                            "sender": "Human",
                            "receiver": "AI",
                            "timestamp": "2023-11-07T12:05:00",
                            "type": "message"
                        }
                    ),
                    Document(
                        page_content="游戏基本上没有设计固定的线路让你前进，要如何选择前进的道路完全取决于你的选择。",
                        metadata={
                            "sender": "AI",
                            "receiver": "Human",
                            "timestamp": "2023-11-07T12:05:03",
                            "type": "message"
                        }
                    )
                ]

    """

    docs = [
        Document(page_content=chat["page_content"], metadata=chat["metadata"])
        for chat in chats
    ]
    return docs


def chats_to_chat_str(chats: List[dict]):
    chats_text = "\n".join(
        [f"{chat['metadata']['sender']}: {chat['page_content']}" for chat in chats]
    )
    return chats_text
