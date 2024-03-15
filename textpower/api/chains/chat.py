from fastapi import APIRouter, Body

from textpower.complex.response.result import Result
from textpower.function.chains.chat import ChatChains

router = APIRouter(prefix="/chat", tags=["聊天API"])


"""LLM对话"""


@router.post("/call", summary="通用会话(非记忆)")
async def call(text: str = Body(..., embed=True)):
    return Result.ok(ChatChains().call(text))


@router.post("/conversation", summary="通用会话(记忆)")
async def conversation(text: str = Body(..., embed=True)):
    return Result.ok(ChatChains().conversation(text))


"""RAG对话"""


@router.post("/conversation/rag", summary="RAG会话(记忆)")
async def conversation_rag(text: str = Body(..., embed=True)):
    return Result.ok(ChatChains().rag(text))
