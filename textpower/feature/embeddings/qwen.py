import json
from http import HTTPStatus
from typing import List

import dashscope
import requests
from langchain_core.embeddings import Embeddings

from textpower.complex.config.api_settings_inventory import embedding, keys_qwen


class QwenEmbeddings(Embeddings):
    def __init__(self):
        self.model = embedding()
        self.qwen_api_key = keys_qwen()

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_with_str(texts, 0)

    def embed_query(self, text: str) -> List[float]:
        return self.embed_with_str(text, 1)

    def embed_with_str(self, text, type):
        """Embed with dashscope."""
        dashscope.api_key = self.qwen_api_key
        resp = dashscope.TextEmbedding.call(model=self.model, input=text)
        if resp.status_code == HTTPStatus.OK:
            list = resp.output["embeddings"]
            if len(list) > 1:
                data = []
                for item in list:
                    data.append(item["embedding"])
                return data
            else:
                if type == 0:
                    list2 = [list[0]["embedding"]]
                    return list2
                else:
                    return list[0]["embedding"]
        else:
            return resp

    def embed_with_str_http(self, text, type):
        """Embed with HTTP request."""
        url = "https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding/text-embedding"
        payload = json.dumps(
            {
                "model": self.model,
                "input": {"texts": [text] if type == 1 else text},
                "parameters": {"text_type": "query"},
            }
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.qwen_api_key,
        }
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == HTTPStatus.OK:
            resp = json.loads(response.text)
            list = resp["output"]["embeddings"]
            if len(list) > 1:
                data = []
                for item in list:
                    data.append(item["embedding"])
                return data
            else:
                if type == 0:
                    list2 = [list[0]["embedding"]]
                    return list2
                else:
                    return list[0]["embedding"]
        else:
            return response
