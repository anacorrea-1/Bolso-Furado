# 💸 Bolso Furado

O **Bolso Furado** é uma aplicação desktop desenvolvida em Python para gestão e controle de finanças pessoais. O sistema oferece uma interface gráfica intuitiva que permite aos usuários registrar, categorizar e acompanhar suas despesas diárias, facilitando a organização do orçamento pessoal e a visualização de para onde o dinheiro está indo.

---

## 📖 A História por Trás do Projeto

O nome **Bolso Furado** nasceu de uma expressão popular que todo mundo já sentiu na pele: aquela sensação de receber o salário ou a mesada e, poucos dias depois, olhar para a carteira sem saber exatamente onde o dinheiro foi parar — como se houvesse literalmente um furo no bolso.

A ideia do projeto surgiu da necessidade de transformar esse problema cotidiano em uma solução prática, leve e acessível. Em vez de planilhas complexas ou aplicativos cheios de recursos difíceis de configurar, o objetivo desde o início foi criar um sistema direto ao ponto, acompanhado de uma identidade visual amigável (com seu próprio mascote) para tornar o hábito de anotar gastos algo simples e até divertido.

Durante o seu desenvolvimento, o projeto foi estruturado seguindo boas práticas de engenharia de software — passando pela modelagem completa do banco de dados (MER e DER), criação de scripts de migração e separação clara entre regras de negócio, acesso a dados e interfaces gráficas — evoluindo de um simples registro de despesas para um sistema completo com autenticação de usuários, categorização personalizada e análise visual de gastos.

---

## ✨ Funcionalidades Principais

* **Autenticação de Usuários:** Tela de login (`login_view.py`) e cadastro de novos usuários (`cadastro.py`) para acesso individualizado aos dados financeiros.
* **Gerenciamento de Categorias:** Criação e organização de categorias personalizadas (`cadastro_categoria.py`) para classificar os gastos (ex.: Alimentação, Transporte, Lazer).
* **Registro de Despesas:** Formulário dedicado para lançamento de novos gastos (`cadastro_despesa.py`) vinculados às categorias cadastradas.
* **Acompanhamento e Visualização:**
  * **Listagem Geral (`lista_despesas.py`):** Consulta completa do histórico de despesas registradas.
  * **Visão por Categoria (`despesas_categoria.py`):** Agrupamento e análise dos gastos segmentados por tipo de despesa.
* **Apresentação do Sistema:** Tela informativa (`conheca_view.py`) apresentando o projeto e a identidade visual do aplicativo.

---

## 🛠️ Estrutura do Projeto

O projeto segue uma arquitetura organizada separando interface, regras de negócio, banco de dados e documentação:

```text
Bolso-Furado/
├── documents/
│   └── modelagem_bd/          # Diagramas DER e MER do banco de dados (.png, .asta, .brM3)
├── migrate/
│   ├── Script_bando_de_dados.sql   # Script de criação das tabelas
│   └── Script_Dados_Exemplos.sql   # Dados iniciais para testes
├── src/
│   ├── database/
│   │   └── conexao.py         # Configuração de conexão com o banco de dados
│   ├── model/                 # Entidades e regras de negócio (usuario, categoria, despesas)
│   └── view/                  # Telas da interface gráfica e recursos visuais (img/)
├── main.py                    # Arquivo principal de inicialização do app
└── requirements.txt           # Dependências do projeto
```

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
* **Python 3.10+** instalado na máquina (testado com Python 3.13).
* Servidor de banco de dados configurado conforme as credenciais definidas em `src/database/conexao.py`.

### 2. Configuração do Banco de Dados
1. Execute o script `migrate/Script_bando_de_dados.sql` no seu gerenciador de banco de dados para criar a estrutura de tabelas.
2. *(Opcional)* Execute o script `migrate/Script_Dados_Exemplos.sql` caso deseje popular o sistema com registros de exemplo.
3. Verifique se os dados de acesso em `src/database/conexao.py` correspondem ao seu ambiente local.

# 3. Inicie a aplicação
python main.py
```

---

## 🗄️ Modelagem de Dados

A documentação completa da estrutura relacional do banco de dados (Modelo Entidade-Relacionamento e Diagrama Entidade-Relacionamento) está disponível na pasta `documents/modelagem_bd/`.