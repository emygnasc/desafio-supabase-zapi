*INTEGRAÇÃO SUPABASE + Z-API*
Projeto desenvolvido como um desafio técnico.
Lê contatos cadastrados no Supabase e envia mensagens personalizadas via WhatsApp usando a Z-API.
    Olá, <nome_contato> tudo bem com você?

*Setup da tabela*
Crie uma tabela chamada "contatos" com os seguintes campos:

|  Campo   |   Tipo   |
|----------|----------|
| id       |  bigint  |
| nome     |   text   |
| telefone |   text   |

Observe o exemplo:

| id |   nome   | telefone      |
|----|----------|---------------|
| 1  | Fulano   | 5511999999999 |
| 2  | Ciclano  | 5511888888888 |
| 3  | Beltrano | 5511777777777 |

*Variáveis de ambiente*
O projeto contém um arquivo ".env.example" com todas as variáveis necessárias. Basta utilizá-lo como modelo para criar o arquivo ".env" na raiz do projeto.

```.env
SUPABASE_URL=url_aqui
SUPABASE_KEY=publishablekey_aqui

ZAPI_INSTANCE=id_instancia
ZAPI_TOKEN=token_instancia
```

*Como rodar*

Para instalações necessárias: pip install -r requirements.txt
Ative o ambiente virtual e execute: python main.py