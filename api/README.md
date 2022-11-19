# :leaves: **Desafio Frexco**

### Desafio para o processo seletivo da Frexco

## 📖 Sobre

Este projeto consiste em um desafio para o processo seletivo da Frexco, possui dois endpoits, para cadastrar e listar usuário. 


## 🛠 Tecnologias utilizados

Para o desenvolvimento deste projeto, as seguintes tecnologias foram usadas:

- **Python 3.9**
- **Django**
- **Django-rest-framework** 



## ▶️ Como executar o projeto
Para executar o projeto, primeiramente é necessário instalar as dependências, com o comando: 

`pip install -r requirements.txt`

E executar o projeto com: 

`python3 manage.py runserver`

a aplicação estará rodando no http://localhost:8000

## Descrição dos endpoints

### Endpoint para criação do usuário : POST
 >`http://localhost:8000/create/`

#### Formato de entrada:

```
{
  "login": "",
  "senha": "",
  "dataNascimento": ""
}
```

A senha é opcional e caso não esteja no corpo da requisição, será criada aleatóriamente. Os campos de login e data de nascimento são obrigatórios. 

#### Formato de saída: 

```
{
  "login": "",
  "senha": "",
  "dataNascimento": ""
}
```

### Endpoint para listagem de usuários : GET
 >`http://localhost:8000/list/`

É uma requisição do tipo get que retorna todos os usuários cadastrados, quando a requisição é feita os dados do banco de dados são salvos em três arquivos diferentes: 

- data.json
- data.csv
- data.xlsx

Então os dados podem ser visualizados nesses três diferentes formatos. 

  



