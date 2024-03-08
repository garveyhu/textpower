from fastapi import APIRouter, Body

from textpower.api.response.result import Result

chat_router = APIRouter(prefix="/chat", tags=["聊天API"])


"""LLM对话"""


@chat_router.post("/call", summary="通用会话(非记忆)")
async def call(text: str = Body(..., embed=True)):
    return Result.fail()


@chat_router.post("/conversation", summary="通用会话(记忆)")
async def conversation(text: str = Body(..., embed=True)):
    return Result.ok()


"""RAG对话"""


@chat_router.post("/conversation/rag", summary="RAG会话(记忆)")
async def conversation_rag(text: str = Body(..., embed=True)):
    return Result.ok()