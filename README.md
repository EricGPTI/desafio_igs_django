# **<font color="lightblue">Desafio_Django - API Funcionários</font>**
Desenvolvimento de API para gestão de funcionários

<hr/><br />

## **<font color="lightblue">Requisitos</font>**
<br />

![Licence](https://img.shields.io/github/license/EricGPTI/desafio_igs_django)
![Python Versions](https://img.shields.io/badge/Python-3.7.1%20to%203.10.0-brightgreen&style=plastic)
![Postgres](https://img.shields.io/badge/Postgres-13.4-blue&style=plastic)
![Django](https://img.shields.io/github/pipenv/locked/dependency-version/EricGPTI/desafio_igs_django/django?color=blue&style=plastic)
![DjangoRestFramework](https://img.shields.io/github/pipenv/locked/dependency-version/EricGPTI/desafio_igs_django/djangorestframework?color=red&style=plastic)

<hr/><br />

## **<font color="lightblue">Sobre min.</font>**
Autor: Eric Gomes

Linkedin: [Eric Gomes](https://www.linkedin.com/in/ericgpti/)

Github: [Github](https://github.com/EricGPTI)
<hr><br />

## **<font color="lightblue">O projeto</font>**


O projeto tem por objetivo a cração de uma api que permita ser integrada para gestão de usuário (CRUD).

<hr/><br />

## **<font color="lightblue">Como foi construída</font>**

A API foi construída usando Django, Django Rest Fremework, Banco de Dados Postgres e Docker.

<hr/><br />

## **<font color="lightblue">Como rodar o projeto</font>**

### **Windows**
* [Python 3.7.1+](https://www.python.org/downloads/)
* [Git for windows](https://gitforwindows.org/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* [WSL 2](https://docs.docker.com/desktop/windows/wsl/)

Siga os links acima na ordem para preparar seu ambiente.

Uma vez validado que os requisitos básicos são atendidos, é necessário baixar o projeto com o **git**.

Baixe o projeto no seu diretório de trabalho.
```
git clone https://github.com/EricGPTI/desafio_igs_django.git
```
entre no diretório do projeto. 
```
cd desafio_igs_django
```

### **<font color="lightblue">Subindo o banco de dados</font>**

Com o docker rodando e dentro do diretório do projeto execute o seguinte comando:
``` 
docker-compose up
```

O banco irá subir e você verá uma mensagem conforme imagem abaixo:
![image](https://user-images.githubusercontent.com/17994386/145925802-421c2f5b-68f0-4165-8063-adc5a4c9479a.png)

Se tudo deu certo seu banco de dados está pronto para receber conexão. Agora vamos rodar nossa API.

<hr><br />

### **<font color="lightblue">Instalando Dependências</font>**
**PIPENV**
```
pip install --user pipenv
```

**Dependências do projeto**
```
pipenv shell
pipenv sync
```

Se não desejar usar o pipenv, você pode também usar o próprio pip para instalar as dependências do projeto, tanto local quanto em ambiente virtual.

**Ambiente virtual**
```
pip install virtualenv
virtualenv .venv
.venv\Scritp\activate
pip install -r requimentes.txt
pip install -r requimentes-dev.txt
```

Desta forma você criou um ambiente virtual e instalou as dependências do projeto num ambiente apartado do seu sistema operacional.

Se não desejar usar o virtualenv, ignore os 3 primeiros passos acima e vá direto para  a instalação dos pacotes.

Uma vez que todos os pacotes foram instalados, é hora de preparar a aplicação para rodar.

### **<font color="lightblue">Rodando Migrações</font>**

A API possui arquivos de migração que irá permitir subir as tabelas do banco de dados sem maiores esforços. Para isso siga os próximos passos:

* No terminal do windows, dentro do diretório do projeto faça:
```
python manage.py migrate
```
O comando acima irá preparar a estrutura do banco de dados para receber os dados.
### **<font color="lightblue">Arquivos Estáticos</font>**
Para servir os arquivos estáticos localmente, rode o seguinte comando:
```
python manage.py collectstatic
```

Um novo diretório será criado e teremos nossos arquivos estáticos prontos para serem servidos, sem deixar nossa interface com uma aparência ruim.

### **<font color="lightblue">Criando Super Usuário</font>**
Precisamos de um usuário adminsitrador para iniciamos o cadastro de nossos departamentos.

```
python manage.py createsuperuser
```
Será solicitado email e senha para o usuário, siga os passos e crie um super usuário.

### **<font color="lightblue">Criando Super Usuário</font>**
Com o usuário administrador da aplicação criado, é hora de rodar nosso serviço de API.

```
python manage.py runserver
```
Se tudo correu bem nosso servidor estará no ar e pronto para fazer os acessos.
![image](https://user-images.githubusercontent.com/17994386/145927178-c6311c74-9549-4bfb-8722-452196d1d3db.png)

Agora que nosso servidor está rodando acesse o link abaixo:
[Admin](http://127.0.0.1:8000/admin)
entre com email e senha do administrador criado anteriormente e faça o cadastro de departamentos.

![image](https://user-images.githubusercontent.com/17994386/145927784-7a298788-bbba-4682-bd4b-e7428e09c857.png)

Criado os departamentos, temos agora que criar um token que permita nosso usário adminsitrador fazer requisições no backend.

Para isso vá até a opção de token e clique em criar um token. Selecione o usuário e crie um token.

![image](https://user-images.githubusercontent.com/17994386/145927990-4cfb8a70-34e7-4fc0-b2a4-e84c6d07a011.png)

Copie este token e salve em algum lugar, pois iremos utilizar para fazer as requisições à API.
Se desejar criar um um novo usuário você poderá criar, só lembre de dar as devidas permissões e de criar seu token para acesso.
<hr><br />

## **<font color="lightblue">Fazendo Requisições</font>**
**Endpoints**
* GET All employees - http://127.0.0.1:8000/api/v1/employees/
* POST employee - http://127.0.0.1:8000/api/v1/employees/
* DELETE employee - http://127.0.0.1:8000/api/v1/employees/{id}

Configure sua ferramenta de preferência como Insomnia ou Postman passando:
**Header:**
* Authorization  Token {Seu_token_aqui}
* Content-Type   application/json

**Criando um employee**
Faça uma requisição POST para o endereço e no body da requisição passe algo como:
```
{
	"name": "Pedro Costa",
	"email": "pedro.costa@gmail.com",
	"department": "TI"
}
```
Não esqueça que o tipo da requisição é JSON.
Se tudo correu bem você receberá um status code = 201 Created.
![image](https://user-images.githubusercontent.com/17994386/145929534-9e0e6189-1150-4d47-930e-6fbf9c2135c2.png)

Cada requisição um employee.

**Consultando employees**
Crie alguns employees e então faça uma consulta de todos os os employees existentes.
![image](https://user-images.githubusercontent.com/17994386/145929758-ee4447b9-2bf5-43ac-96df-b9dbd7d8eb90.png)

Na imagem acima apenas um employee foi retornado, isso porque apenas um foi criado previamente.
Nenhum dado é necessário ser passado no corpo da requisição.

**Deletando um employee**
Para deletar um usuário basta fazer uma chamada do tipo DELETE no endepoint específico passando o id do usuário.
Se tudo correr bem você receberá um status code = 200.

## **<font color="lightblue">Rodando os testes da aplicação</font>**
Para rodar os testes, é necessário que um token seja passado. Você encontrará uma variável header e um campo que poderá passar seu token válido.

Depois disso basta rodar os testes com pytest.

## **<font color="lightblue">Finalizando a aplicação.</font>**
Para finalizar a aplicação, basta usar as teclas de atalho **Ctrl+C** no terminal onde o docker está rodando nosso banco de dados e depois rodar o seguinte comando:
```
docker-compose down
```

Depois acesse o conseole onde o servidor da api está rodando e use as teclas de atalho **Ctrl+C**.
