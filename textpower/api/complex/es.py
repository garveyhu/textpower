from io import StringIO

from fastapi import APIRouter, File, UploadFile

from textpower.complex.response.result import Result
from textpower.complex.schema.chats import ChatList
from textpower.function.complex.es import ElasticSearchChat, ElasticSearchResource

router = APIRouter(prefix="/es", tags=["ES相关API"])


"""ES存储"""


@router.post("/store-chat", summary="存储聊天记录")
async def store_chat(chats: ChatList):
    ElasticSearchChat().store_chat(chats)

    return Result.ok()


@router.post("/store-file", summary="存储文件记录")
async def store_file(file: UploadFile = File(...)):
    resource = StringIO((await file.read()).decode("utf-8"))
    ElasticSearchResource().store_resource(resource)

    return Result.ok()
