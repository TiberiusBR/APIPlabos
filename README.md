# API Plabos

### Api usada para consumo de dados do projeto Plabos.

É necessário instalar o docker e o docker-compose para inicialização do banco de dados.

Para configurar a inicialização do projeto, crie um arquivo .env com os seguintes valores:

- POSTGRES_USER - Usuário do banco;
- POSTGRES_PASSWORD - Senha do usuário;
- POSTGRES_DB - Nome do banco usado;

**Chaves Opcionais**
- POSTGRES_HOST - Nome do host usado para conexão ao banco (padrão localhost) (**CASO EM CONTAINER, SETAR COMO POSTGRES**)
- POSTGRES_PORT - Porta usada para conexão ao banco. (padrão 5432)
- API_PORT - Porta usada para conexão a API (padrão 8000)
- UVICORN_HOST - Hostname/ip (servidor WEB) (padrão 127.0.0.1 / localhost) (**CASO EM CONTAINER, SETAR COMO 0.0.0.0**)

Após a configuração inicial:

- Instale as dependências do requirements.txt;
- Construa a imagem do container `docker build -t tiberiusbr/apiplabos .`
- Rode docker-compose up para instanciar o banco de dados localmente;
- Mude o diretório para a pasta app (cd app)
- Rode `uvicorn main:app --reload` para executar a API.

