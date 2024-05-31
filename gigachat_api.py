import json
import os
import uuid

import dotenv
import requests
from requests.auth import HTTPBasicAuth

from utils import get_file_id

dotenv.load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv("SECRET_KEY")


def get_access_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": str(uuid.uuid4()),
    }
    payload = {"scope": "GIGACHAT_API_PERS"}
    response = requests.post(
        url,
        headers=headers,
        data=payload,
        auth=HTTPBasicAuth(CLIENT_ID, SECRET_KEY),
        verify=False,
    )
    return response.json()["access_token"]


def get_image(file_id: str, access_token: str) -> str:
    url = (
        f"https://gigachat.devices.sberbank.ru/api/v1/files/{file_id}/content"
    )

    payload = {}
    headers = {
        "Accept": "application/jpg",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(url, headers=headers, data=payload, verify=False)
    return response.content


def send_prompt(msg: str, access_token: str):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps(
        {
            "model": "GigaChat",
            "messages": [
                {
                    "role": "user",
                    "content": msg,
                },
            ],
            "function_call": "auto",
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response.json()["choices"][0]["message"]["content"]


def sent_prompt_and_get_response(msg: str, access_token: str):
    res = send_prompt(msg, access_token)
    data, is_image = get_file_id(res)
    if is_image:
        data = get_image(file_id=data, access_token=access_token)

    return data, is_image
