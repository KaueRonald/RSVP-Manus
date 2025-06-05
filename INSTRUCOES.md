# Instruções para Execução Local

Este documento descreve os passos necessários para configurar e executar o projeto RSVP-Manus localmente.

## Pré-requisitos

*   Python 3.11
*   pip (gerenciador de pacotes Python)
*   Git (sistema de controle de versão)
*   MySQL Server (ou um servidor compatível como MariaDB)
*   Bibliotecas de desenvolvimento do MySQL (`libmysqlclient-dev` ou equivalente)
*   Bibliotecas de desenvolvimento do Python 3.11 (`python3.11-dev` ou equivalente)

## Configuração

1.  **Clonar o Repositório:**
    Se você ainda não tem o código, clone o repositório (ou use a versão que enviei):
    ```bash
    git clone https://github.com/KaueRonald/RSVP-Manus.git
    cd RSVP-Manus
    ```

2.  **Criar e Ativar Ambiente Virtual (Recomendado):**
    É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```

3.  **Instalar Dependências do Sistema:**
    Certifique-se de que as bibliotecas de desenvolvimento necessárias estão instaladas. Em sistemas baseados em Debian/Ubuntu:
    ```bash
    sudo apt-get update
    sudo apt-get install -y default-libmysqlclient-dev pkg-config gcc python3.11-dev
    ```
    Para outros sistemas, consulte a documentação da sua distribuição.

4.  **Instalar Dependências Python:**
    Instale todas as bibliotecas Python listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configurar Banco de Dados MySQL:**
    *   Crie um banco de dados MySQL para o projeto (ex: `rsvp`).
    *   Crie um usuário para o banco de dados (ex: `rsvp`) e conceda as permissões necessárias.
    *   Anote o nome do banco, usuário, senha, host e porta.

6.  **Criar Arquivo `.env`:**
    Na raiz do projeto (`RSVP-Manus/`), crie um arquivo chamado `.env` e adicione as seguintes variáveis, substituindo pelos seus valores:
    ```dotenv
    SECRET_KEY=sua_chave_secreta_aqui # Gere uma chave segura
    DEBUG=True # Mude para False em produção

    DB_ENGINE=django.db.backends.mysql
    DB_NAME=rsvp # Nome do seu banco de dados
    DB_USER=rsvp # Usuário do seu banco de dados
    DB_PASSWORD=sua_senha_aqui # Senha do seu banco de dados
    DB_HOST=localhost # Ou o host do seu servidor MySQL (ex: 127.0.0.1)
    DB_PORT=3306 # Porta do seu servidor MySQL

    # Outras chaves de API (opcional, se não for usar os serviços)
    SENDGRID_API_KEY=
    WHATSAPP_API_TOKEN=
    GOOGLE_CALENDAR_CREDENTIALS_JSON=
    ```
    *Nota:* Para gerar uma `SECRET_KEY` segura, você pode usar o seguinte comando Python:
    `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

7.  **Aplicar Migrações:**
    Execute as migrações para criar as tabelas no banco de dados:
    ```bash
    python manage.py makemigrations events guests users
    python manage.py migrate
    ```

8.  **Criar Superusuário (Opcional):**
    Se precisar acessar a área administrativa do Django (`/admin/`) ou se não tiver um usuário, crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para definir nome de usuário, email e senha.

## Execução

1.  **Iniciar Servidor de Desenvolvimento:**
    Execute o servidor de desenvolvimento do Django:
    ```bash
    python manage.py runserver
    ```

2.  **Acessar a Aplicação:**
    Abra seu navegador e acesse `http://127.0.0.1:8000/`.
    *   Faça login com as credenciais do superusuário criado ou com um usuário existente.
    *   Navegue até `/events/list/` para ver a lista de eventos.

## Observações

*   As configurações `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS` no `config/settings.py` foram ajustadas para permitir o acesso durante meus testes. Para produção, revise essas configurações e restrinja os hosts permitidos.
*   Os modelos `Category` e `GuestGroup` que estavam no app `guests` foram comentados em `apps/guests/models.py` pois foram recriados dentro do app `events` e vinculados ao modelo `Event` para atender aos requisitos.
*   O arquivo `requirements.txt` foi ajustado para usar `mysqlclient==2.1.1` devido a problemas encontrados com versões mais recentes durante a instalação no ambiente de teste.

