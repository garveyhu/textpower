from fastapi import APIRouter

from textpower.api.function.chat import chat_router

function_router = APIRouter(tags=["功能API集"])

function_router.include_router(chat_router)