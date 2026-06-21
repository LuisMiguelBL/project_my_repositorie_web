# Projeto Web com Django + Microserviço de Notificações

## Descrição

Este trabalho é composto por **dois projetos independentes**:

### 1. Portfolio (Porta 8000)

Sistema principal desenvolvido com Django e Django REST Framework.

Funcionalidades:

* Página de portfólio pessoal
* API de Perfil
* Autenticação JWT
* Integração com microserviço de notificações

### 2. Microserviço de Notificações (Porta 8001)

Serviço independente responsável pelo gerenciamento de notificações.

Funcionalidades:

* Cadastro de empresas
* Cadastro de targets
* Criação de notificações
* Consulta de notificações
* Marcação de notificações como lidas

---

# Pré-requisitos

* Python 3.10 ou superior
* Git
* Pip

Verifique as versões:

```bash
python --version
git --version
pip --version
```

---

# 1. Clonar os Repositórios

## Portfolio

```bash
git clone https://github.com/LuisMiguelBL/project_my_repositorie_web.git

```

## Microserviço

Abra outro terminal:

```bash
git clone https://github.com/LuisMiguelBL/micro-service-notifications.git

```

---

# 2. Configurar o Portfolio

Entre na pasta do portfolio:

```bash
cd <PASTA_PORTFOLIO>
```

## Criar ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar migrações

```bash
python manage.py migrate
```

## Criar superusuário

```bash
python manage.py createsuperuser
```

Preencha:

```text
Username: admin
Email: admin@email.com
Password: ********
```

## Executar servidor

```bash
python manage.py runserver
```

O sistema estará disponível em:

```text
http://127.0.0.1:8000
```

---

# 3. Configurar o Microserviço

Abra outro terminal.

Entre na pasta do microserviço:

```bash
cd <PASTA_MICROSERVICO>
```

## Criar ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar migrações

```bash
python manage.py migrate
```

## Criar superusuário

```bash
python manage.py createsuperuser
```

## Executar servidor

```bash
python manage.py runserver 8001
```

O sistema estará disponível em:

```text
http://127.0.0.1:8001
```

---

# 4. Configuração Inicial do Microserviço

Acesse:

```text
http://127.0.0.1:8001/admin
```

Faça login com o superusuário.

## Criar Empresa

Menu:

```text
Empresas -> Add
```

Exemplo:

```text
Nome: Portfolio UAST
```

Após salvar será gerado automaticamente um hash.

Exemplo:

```text
49a80d0d50e57b9e
```

Guarde esse valor.

---

# 5. Configurar Integração com o Portfolio

No Portfolio, configure:

```text
API_URL = http://127.0.0.1:8001
```

e

```text
X-Api-Key = HASH_GERADO_NO_MICROSERVICO
```

Exemplo:

```text
49a80d0d50e57b9e
```

---

# 6. Testando a API de Perfil

## Obter Token JWT

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d "{\"username\":\"admin\",\"password\":\"SUA_SENHA\"}"
```

Resposta esperada:

```json
{
  "refresh": "...",
  "access": "..."
}
```

Copie o valor de `access`.

---

## Consultar Perfil

```bash
curl http://127.0.0.1:8000/api/perfil/ \
-H "Authorization: Bearer SEU_TOKEN"
```

---

## Atualizar Perfil

```bash
curl -X PATCH http://127.0.0.1:8000/api/perfil/ \
-H "Authorization: Bearer SEU_TOKEN" \
-H "Content-Type: application/json" \
-d "{\"nome\":\"Novo Nome\"}"
```

---

# 7. Testando o Microserviço

Substitua:

```text
SEU_HASH
```

pelo hash criado na Empresa.

---

## Criar Notificação

```bash
curl -X POST http://127.0.0.1:8001/api/notificacoes/criar/ \
-H "X-Api-Key: SEU_HASH" \
-H "Content-Type: application/json" \
-d "{\"user_id\":1,\"mensagem\":\"Bem-vindo ao sistema!\"}"
```

---

## Contar Notificações Não Lidas

```bash
curl http://127.0.0.1:8001/api/notificacoes/nao-lidas/ \
-H "X-Api-Key: SEU_HASH" \
-H "X-User-Id: 1"
```

Resposta esperada:

```json
{
  "count": 1
}
```

---

## Listar Notificações

```bash
curl http://127.0.0.1:8001/api/notificacoes/ \
-H "X-Api-Key: SEU_HASH" \
-H "X-User-Id: 1"
```

---

## Listar Apenas Não Lidas

```bash
curl "http://127.0.0.1:8001/api/notificacoes/?is_read=false" \
-H "X-Api-Key: SEU_HASH" \
-H "X-User-Id: 1"
```

---

## Marcar Como Lida

Substitua o ID da notificação:

```bash
curl -X PATCH http://127.0.0.1:8001/api/notificacoes/1/lida/ \
-H "X-Api-Key: SEU_HASH" \
-H "X-User-Id: 1"
```

---

# 8. Verificação Final

Os dois servidores devem estar executando simultaneamente:

### Portfolio

```text
http://127.0.0.1:8000
```

### Microserviço

```text
http://127.0.0.1:8001
```

Ao acessar o Portfolio:

* O sistema deve carregar normalmente.
* O sino de notificações deve consultar o microserviço.
* As notificações criadas no microserviço devem aparecer no Portfolio.

---

# Estrutura dos Projetos

## Portfolio

```text
portfolio/
├── core/
├── portfolio/
├── manage.py
├── requirements.txt
└── README.md
```

## Microserviço

```text
notificacao_ms/
├── notificacoes/
├── notificacao_ms/
├── manage.py
├── requirements.txt
└── README.md
```

---

# Autor

Nome: Luís Miguel Belfort

Disciplina: Sistemas Desenvolvidos para Web

Professor: Heldon José
