from servicos.supabase_servico import procurar_contato
from servicos.zapi_servico import enviar_mensagem

def main():
    contatos = procurar_contato()

    if not contatos:
        print("Nenhum contato encontrado.")
        return
    
    print(f"Contatos encontrados: {len(contatos)}")
    
    for contato in contatos:
        nome = contato["nome"]
        telefone = contato["telefone"]

        mensagem = f"Olá, {nome} tudo bem com você?"

        try:
            resposta = enviar_mensagem(
                telefone,
                mensagem,
                modo_teste=True
            )

            print(
                f"Mensagem para {nome}"
            )

        except Exception as ERRO:
            print(
                f"Erro para {nome}: {ERRO}"
            )

if __name__ == "__main__":
    main()