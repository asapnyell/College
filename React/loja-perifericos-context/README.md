# 🛒 Loja de Periféricos Tech

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Context-API](https://img.shields.io/badge/Context--API-000000?style=for-the-badge&logo=react)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

Este projeto é uma aplicação **React** desenvolvida para demonstrar o poder do `useContext` no gerenciamento global de estados. A aplicação simula a experiência de uma loja de periféricos, integrando um sistema de compras com uma interface adaptável.

---

## 🚀 Funcionalidades Principais

* **Gerenciamento de Carrinho:** Adição dinâmica de produtos, cálculo de total e limpeza de itens via Context API.
* **Tema Customizável:** Alternância rápida entre **Modo Claro** e **Modo Escuro**.
* **Persistência de Dados:** Uso de `LocalStorage` para que a escolha do seu tema favorito não se perca ao recarregar a página.
* **Design Responsivo:** Interface otimizada para desktops, tablets e smartphones.

## 🛠️ Tecnologias Utilizadas

- **[React.js](https://reactjs.org/):** Biblioteca principal para construção da interface.
- **Context API:** Gerenciamento de estado global sem "prop drilling".
- **Variáveis CSS3:** Utilizadas para a lógica de temas (Dark/Light Mode).

---
## ⚙️ Como Rodar o Projeto

Siga os passos abaixo para configurar o ambiente e executar a aplicação em sua máquina local.

### 1. Pré-requisitos
Certifique-se de ter o [Node.js](https://nodejs.org/) instalado em sua máquina.

### 2. Instalação e Execução

Abaixo estão os comandos necessários, execute-os em seu terminal:

| Passo | Descrição | Comando |
| :---  | :-------  | :------ |
| **1** | Clone o repositório | `git clone https://github.com/asapnyell/College.git` |
| **2** | Acesse a pasta | `cd College/React/loja-perifericos-context` |
| **3** | Instale as dependências | `npm install` |
| **4** | Inicie o projeto | `npm run dev` |


### 3. Acessando a aplicação

Após o passo 4, o terminal exibirá um endereço local. Geralmente é:

> 🌐 **Local:** [http://localhost:5173/](http://localhost:5173/)

Basta copiar o link, colar no seu navegador e testar as funcionalidades de **Carrinho** e **Tema Escuro**!

---

### 🛠️ Scripts Disponíveis

No diretório do projeto, você pode executar:

- `npm run dev`: Roda o app em modo de desenvolvimento.
- `npm run build`: Cria a versão de produção na pasta `dist`.
- `npm run preview`: Visualiza localmente a versão de produção criada.