import os
import requests

from dotenv import load_dotenv

load_dotenv()

INSTANCE = os.getenv("ZAPI_INSTANCE")
TOKEN = os.getenv("ZAPI_TOKEN")

URL = (
    f"https://api.z-api.io/instances/"
    f"{INSTANCE}/token/{TOKEN}/send-text"
)

def enviar_mensagem(numero, mensagem):
    
    payload = {
        "phone": numero,
        "message": mensagem
    }

    response = requests.post(
        URL,
        json=payload,
        timeout=10
    )

    return response