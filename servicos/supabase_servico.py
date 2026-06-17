import os 

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def procurar_contato():
    response = (
        supabase
        .table("contatos")
        .select("*")
        .limit(3)
        .execute()
    )

    return response.data