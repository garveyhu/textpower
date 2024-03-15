import json
from http import HTTPStatus
from typing import Any

import dashscope
import requests
from langchain_core.language_models import LLM

from textpower.complex.config.api_settings_inventory import (
    keys_qwen,
    llm,
    llm_temperature,
)


class Qwen(LLM):

    @property
    def _llm_type(self) -> str:
        return "Qwen"

    def _call(
        self,
        prompt: str,
        **kwargs: Any,
    ) -> str:
        content = self._call_prompt(prompt, **kwargs)
        return content

    def _call_prompt(self, prompt, **kwargs: Any):
        dashscope.api_key = keys_qwen()
        response = dashscope.Generation.call(
            model=llm(), prompt=prompt, temperature=llm_temperature(), **kwargs
        )
        if response.status_code == HTTPStatus.OK:
            if hasattr(response, "output"):
                output = response.output
                return output["text"]
        else:
            return (
                "Request id: %s, Status code: %s, error code: %s, error message: %s"
                % (
                    response.request_id,
                    response.status_code,
                    response.code,
                    response.message,
                )
            )

    def _call_prompt_http(self, prompt):
        url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
        payload = json.dumps(
            {
                "model": llm(),
                "input": {
                    "prompt": prompt,
                },
                "parameters": {},
            }
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + keys_qwen(),
        }
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == HTTPStatus.OK:
            print(response.text)
            return json.loads(response.text)["output"]["text"]
        else:
            return "errCode: %s" % (response.status_code,)
