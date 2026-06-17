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

def enviar_mensagem(numero, mensagem, modo_teste=False):
    
    payload = {
        "phone": numero,
        "message": mensagem
    }

    if modo_teste:
        print("MODO DE TESTE")
        print(payload)

        return{
            "STATUS": "Em modo de teste"
        }

    response = requests.post(
        URL,
        json=payload,
        timeout=10
    )

    return response