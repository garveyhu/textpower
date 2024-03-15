import importlib.util
import json
from pathlib import Path

import uvicorn
from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse

from textpower.complex.config.api_settings import init_config
from textpower.complex.config.system_settings import config_json
from textpower.complex.response.code import ResultCode
from textpower.complex.response.exception import CustomException
from textpower.complex.response.result import Result

app = FastAPI(title="TextPower API", version="0.0.1")


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


def register_routers(app: FastAPI):
    root_path = Path(__file__).parent
    for path in root_path.rglob("*.py"):
        if path.stem == "__init__" or path.name == Path(__file__).name:
            continue
        rel_path = path.relative_to(root_path.parent)
        dot_path = str(rel_path).replace("/", ".").replace("\\", ".")[:-3]

        spec = importlib.util.spec_from_file_location(dot_path, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, APIRouter):
                app.include_router(item)


register_routers(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
