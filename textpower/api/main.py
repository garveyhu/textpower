import json

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from textpower.api.functions import function_router
from textpower.api.response.code import ResultCode
from textpower.api.response.exception import CustomException
from textpower.api.response.result import Result
from textpower.complex.config.api_settings import init_config
from textpower.complex.config.system_settings import config_json

app = FastAPI(title=f"TextPower API", version="0.0.1")
app.include_router(function_router)


@app.middleware("http")
async def set_config(request: Request, call_next):
    with config_json.open() as f:
        config_data = json.load(f)

    init_config(config_data)

    response = await call_next(request)
    return response


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.result_code.code,
        content=Result(
            success=False, code=exc.result_code.code, message=exc.message
        ).model_dump(),
    )


@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=ResultCode.SYSTEM_INNER_ERROR.code,
        content=Result(
            success=False, code=ResultCode.SYSTEM_INNER_ERROR.code, message=str(exc)
        ).model_dump(),
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
