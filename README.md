# API Plabos

### Api usada para consumo de dados do projeto Plabos.

É necessário instalar o docker e o docker-compose para inicialização do banco de dados.

Para configurar a inicialização do projeto, crie um arquivo .env com os seguintes valores:

- POSTGRES_USER - Usuário do banco;
- POSTGRES_PASSWORD - Senha do usuário;
- POSTGRES_DB - Nome do banco usado;
- HOST - Nome do host usado para conexão ao banco (padrão localhost)
- PORT - Porta usada para conexão ao banco. (padrão 5432)

Após a configuração inicial:

- Instale as dependências do requirements.txt;
- Rode docker-compose up para instanciar o banco de dados localente;
- Rode uvicorn app.main:app --reload para executar a API.

