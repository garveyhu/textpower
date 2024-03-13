
from langchain_community.chat_message_histories import RedisChatMessageHistory
class RedisMemory(RedisChatMessageHistory):
    """Redis存储聊天历史（只存储上下文文本，不向量化）."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = 10000