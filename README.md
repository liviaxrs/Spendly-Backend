#  Spendly - Backend API

Uma API RESTful leve e rápida para gerenciamento e controle de gastos pessoais. Desenvolvida em Python com **FastAPI** e integrada ao banco de dados NoSQL **Google Cloud Firestore**.

##  Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
* **Servidor ASGI:** Uvicorn
* **Banco de Dados:** Google Cloud Firestore (Firebase)
* **Hospedagem (Deploy):** Google Cloud Run (Serverless)
* **Containerização:** Docker

##  Estrutura do Projeto

A arquitetura do projeto foi pensada para ser simples e escalável:

```text
├── app/
│   ├── main.py          # Ponto de entrada da API e inicialização do app
│   ├── Core             # Configurações globais da aplicação
│   ├── models           # Modelos de dados (Pydantic) para validação
│   ├── routes           # Endpoints da aplicação 
│   ├── repositories     # Acesso ao banco de dados
│   └── services         # Camada de regra de negócio da aplicação
├── Dockerfile           # Instruções para o container no Cloud Run
├── requirements.txt     # Dependências do projeto
└── README.md
