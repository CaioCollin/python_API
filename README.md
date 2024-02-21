**Projeto: CRUD de Livros com Flask**

Este é um projeto simples que implementa um CRUD (Create, Read, Update, Delete) para manipulação de informações sobre livros. O objetivo é criar uma API utilizando Flask, um framework web em Python, que permita realizar operações básicas em uma lista de livros.

**Funcionalidades Implementadas:**

1. **Listagem de Livros:** A API fornece uma rota para obter todos os livros cadastrados.
2. **Obtenção de Livro por ID:** Também é possível obter detalhes de um livro específico fornecendo seu ID como parâmetro na URL.
3. **Edição de Livro por ID:** Há uma rota para editar os detalhes de um livro existente com base em seu ID.
4. **Inclusão de Novo Livro:** É possível adicionar um novo livro à lista existente por meio de uma requisição POST.
5. **Exclusão de Livro por ID:** Por fim, a API permite excluir um livro com base em seu ID.

**Estrutura do Projeto:**

- O projeto consiste em um único arquivo Python.
- Utiliza a biblioteca Flask para criação das rotas e manipulação das requisições HTTP.
- Os dados dos livros são mantidos em uma lista em memória para este exemplo, mas poderiam ser armazenados em um banco de dados para uma aplicação mais robusta.

**Instruções de Uso:**

1. Clone o repositório.
2. Execute o arquivo Python para iniciar o servidor.
3. Utilize um cliente HTTP (como cURL, Postman ou Insomnia) para realizar requisições para as rotas disponibilizadas.

Este projeto serve como uma introdução ao desenvolvimento de APIs RESTful em Python com Flask, fornecendo uma base sólida para a construção de aplicações mais complexas no futuro.
