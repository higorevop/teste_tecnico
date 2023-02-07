# Crédito Fácil

## Dependencias 
Python 3.10

## Iniciando o projeto

Para instalar o projeto, clone o repositório:

`git clone https://@bitbucket.org/eliasvieira/teste_tecnico.git`

Acesse a pasta usando `cd test_tecnico`

Inicie uma nova venv `python -m venv .venv`

Ative a venv criada `. .venv/bin/activate`

Instale as dependencias `pip install -r requirements.txt`

Rode as migrations `./manage.py migrate`

## Servidor de desenvolvimento

Rode `./manage.py runserver`

Acesse `http://127.0.0.1:8000/`.

A aplicação vai atualizar automaticamente se você alterar qualquer arquivo

## Rodando testes unitários

Rode `./manage.py test` para executar os testes unitários.
