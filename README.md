# PIKombucha - Backend de Produtos

## Sobre o projeto

O objetivo deste projeto é implementar um MVP de um API backend REST responsável por tratar os produtos do PIKombucha, que é um site para venda de bebidas saudáveis. Funciona em conjunto com o frontend disponível neste [repositório](https://github.com/ANNEBORTOLI/ftont-puc-mvp-sprint-backend-avancado-). Possibilita a inclusão, remoção, edição e visualização dos produtos.

Este projeto fez parte do MVP da Sprint de Backend Avançado da Pós-Graduação da PUC-RJ

### 🛠️Tecnologias Principais

<ul>
  <li>Python 3.12</li>
  <li>Flask 3.0.0</li>
  <li>SQLite</li>
  <li>SQAlchemy 2.0.23</li>
  <li>flask-openapi3 3.0.1</li>
</ul>

### 📑Regras de negócio

- Inclusão, remoção, edição e visualização dos produtos do PIKombucha
-

### Endpoints

- User Endpoints

| URL / ENDPOINT | VERBO  | DESCRIÇÃO                            |
| -------------- | ------ | ------------------------------------ |
| /product       | GET    | Retorna o produto a partir de seu id |
| /product       | POST   | Adiciona um produto                  |
| /product       | DELETE | Remove um produto                    |
| /product       | PUT    | Edita um produto                     |
| /products      | GET    | Retorna todos os produtos            |

## Documentação

- Lista das rotas no Swagger
<div align="center">
  <img src="public/rotas-swagger.png">
</div>
<br>

- Arquitetura do projeto
<div align="center">
  <img src="public/desenho.png">
</div>
<br>

## Instruções de Uso

Seguem as instruções para a instalação, configuração e uso da aplicação.

### Instalação

1. Clone do repositório

```sh
   git clone git@github.com:ANNEBORTOLI/api-puc-mvp-sprint-backend-avancado.git
   cd api-puc-mvp-sprint-backend-avancado
```

2. Criar um virtual environment, na raiz do projeto:

```
  python.exe -m venv .env
```

3. Instalando os pacotes

```
    pip install -r requirements.txt
```

### Execução local

1. Rodando a aplicação localmente

```
  (env)$ flask run --host 0.0.0.0 --port 5000
```

2. Rodando em modo de desenvolvimento

```
  (env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

3. Abra a URL abaixo no browser para visualizar a documentação no Swagger

```
  http://localhost:5000/
```

### Docker

1. Na raiz do projeto, execute:

```
  docker build -t rest-api .
```

2. Execute o container:

```
  docker run -p 5000:5000 rest-api
```

3. Abra a URL abaixo no browser para visualizar a documentação no Swagger

```
  http://localhost:5000/
```

## Desenvolvedor

- [Github](https://github.com/ANNEBORTOLI)
- [LinkedIn](https://www.linkedin.com/in/anne-bortoli/)
