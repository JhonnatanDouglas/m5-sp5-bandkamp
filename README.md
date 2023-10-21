# Projeto BandKamp

O Projeto BandKamp é uma plataforma de gerenciamento de música construída com o poderoso framework Django e a biblioteca Django Rest Framework (DRF). Este projeto oferece uma API RESTful que permite aos usuários criar, listar, atualizar e excluir álbuns de música e suas respectivas músicas. Além disso, os usuários podem se registrar, fazer login e manter seus perfis de usuário.

## Descrição

O Projeto BandKamp foi desenvolvido para atender às necessidades de entusiastas da música, artistas e amantes da música que desejam gerenciar suas coleções de álbuns e músicas de forma eficaz e organizada. Com a API fornecida pelo Projeto BandKamp, os usuários podem realizar as seguintes ações:

- **Registro e Autenticação**: Os usuários podem se registrar, criando um perfil de usuário com informações como nome de usuário, email e senha. Eles também podem fazer login com suas credenciais.

- **Gerenciamento de Álbuns**: Os usuários podem criar, atualizar, listar e excluir álbuns de música. Cada álbum possui um nome e um ano de lançamento associados.

- **Gerenciamento de Músicas**: Para cada álbum, os usuários podem adicionar músicas, especificando um título e a duração da música.

- **Perfil de Usuário**: Os usuários podem visualizar e atualizar seu perfil de usuário, incluindo informações como nome de usuário e email.

- **Documentação da API**: A API é bem documentada e pode ser acessada por meio do Swagger, fornecendo informações detalhadas sobre todas as rotas disponíveis, parâmetros de requisição e exemplos de solicitações e respostas.

## Tecnologias Utilizadas

O Projeto BandKamp utiliza as seguintes tecnologias:

- Python 3.11.5
- Django 4.2.6
- Django REST framework 3.14.0
- Gunicorn 21.2.0
- Whitenoise 6.6.0
- IPython 8.16.1
- ipdb 0.13.13
- python-dotenv 1.0.0
- drf-spectacular 0.26.5
- djangorestframework-simplejwt 5.3.0


## Índice

1. [Rota: Autenticação](#rota-autenticação)
   1. [Login de Usuário](#1-login-de-usuário)
2. [Rota: Usuários](#rota-usuários)
   1. [Criar Usuário](#2-criar-usuário)
   2. [Listar Usuários](#3-listar-usuários)
   3. [Detalhes do Usuário](#4-detalhes-do-usuário)
   4. [Atualizar Usuário](#5-atualizar-usuário)
   5. [Excluir Usuário](#6-excluir-usuário)
3. [Rota: Álbuns](#rota-álbuns)
   1. [Criar Álbum](#7-criar-álbum)
   2. [Listar Álbuns](#8-listar-álbuns)
4. [Rota: Músicas](#rota-músicas)
   1. [Criar Música](#9-criar-música)
   2. [Listar Músicas de um Álbum](#10-listar-músicas-de-um-álbum)

### Rota: Autenticação

#### 1. Login de Usuário

- **URL:** `/api/users/login/`
- **Método:** `POST`
- **Corpo da Requisição:**
  ```json
  {
      "username": "nome_de_usuario",
      "password": "senha"
  }
  ```
- **Descrição:** Autentica um usuário e fornece um token JWT para uso em outras partes do aplicativo.

### Rota: Usuários

#### 2. Criar Usuário

- **URL:** `/api/users/`
- **Método:** `POST`
- **Corpo da Requisição:**
  ```json
  {
      "username": "nome_de_usuario",
      "password": "senha",
      "email": "email@example.com",
      "full_name": "Nome Completo (opcional)",
      "artistic_name": "Nome Artístico"
  }
  ```
- **Descrição:** Cria um novo usuário com informações como nome de usuário, senha, email e nome artístico.

#### 3. Listar Usuários

- **URL:** `/api/users/`
- **Método:** `GET`
- **Descrição:** Retorna a lista de todos os usuários registrados.

#### 4. Detalhes do Usuário

- **URL:** `/api/users/<int:pk>/`
- **Método:** `GET`
- **Descrição:** Retorna detalhes de um usuário específico com base no ID fornecido.

#### 5. Atualizar Usuário

- **URL:** `/api/users/<int:pk>/`
- **Método:** `PUT`
- **Corpo da Requisição:**
  ```json
  {
      "username": "novo_nome_de_usuario",
      "password": "nova_senha",
      "email": "novo_email@example.com",
      "full_name": "Novo Nome Completo (opcional)",
      "artistic_name": "Novo Nome Artístico"
  }
  ```
- **Descrição:** Atualiza as informações de um usuário específico com base no ID fornecido.

#### 6. Excluir Usuário

- **URL:** `/api/users/<int:pk>/`
- **Método:** `DELETE`
- **Descrição:** Remove um usuário específico com base no ID fornecido.

### Rota: Álbuns

#### 7. Criar Álbum

- **URL:** `/api/albums/`
- **Método:** `POST`
- **Corpo da Requisição:**
  ```json
  {
      "name": "Nome do Álbum",
      "year": 2023
  }
  ```
- **Descrição:** Cria um novo álbum com informações como nome e ano.

#### 8. Listar Álbuns

- **URL:** `/api/albums/`
- **Método:** `GET`
- **Descrição:** Retorna a lista de todos os álbuns registrados.

### Rota: Músicas

#### 9. Criar Música

- **URL:** `/api/albums/<int:pk>/songs/`
- **Método:** `POST`
- **Corpo da Requisição:**
  ```json
  {
      "title": "Título da Música",
      "duration": "3:45"
  }
  ```
- **Descrição:** Cria uma nova música em um álbum específico com informações como título e duração.

#### 10. Listar Músicas de um Álbum

- **URL:** `/api/albums/<int:pk>/songs/`
- **Método:** `GET`
- **Descrição:** Retorna a lista de todas as músicas em um álbum específico com base no ID do álbum fornecido.