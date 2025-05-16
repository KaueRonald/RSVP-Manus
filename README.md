# RSVP ERP

> Sistema ERP para gestão completa de eventos corporativos e sociais, com módulo especializado em RSVP (confirmação de presença), geração de QR Code, comunicação multicanal e relatórios.

---

## 📋 Índice

- [Visão Geral](#visão-geral)  
- [Funcionalidades](#funcionalidades)  
- [Tecnologias](#tecnologias)  
- [Pré‐requisitos](#pré‐requisitos)  
- [Instalação](#instalação)  
- [Configuração de Ambiente](#configuração-de-ambiente)  
- [Execução](#execução)  
- [Estrutura de Pastas](#estrutura-de-pastas)  
- [Testes](#testes)  
- [Licença](#licença)  

---

## 🎯 Visão Geral

O **RSVP ERP** é uma plataforma Django + MySQL para:

- **Cadastro e gestão de eventos** (nome, data, local, capacidade, etc.)  
- **Gerenciamento de convidados** (importação, segmentação, status)  
- **Envio de convites** por e-mail, SMS e WhatsApp  
- **Página de RSVP** com geração de QR Code e PDF de ingresso  
- **Dashboards e relatórios** de presença, perfil de convidados e performance  
- **Controle de usuários e permissões** por função  
- **Integrações** com SendGrid, WhatsApp Business API, Google Calendar e webhooks  

Para um diagrama de alto nível e mais detalhes de arquitetura, consulte **docs/architecture.md**.

---

## ✨ Funcionalidades

1. **Gestão de Eventos**  
   - CRUD de eventos, definição de categorias e cronogramas.  
   - Upload de convites, mapas e materiais.  
   - Links de RSVP personalizados.

2. **Gestão de Convidados**  
   - Importação via CSV/Excel ou API.  
   - Cadastro manual e segmentação por tags.  
   - Histórico de presença.

3. **Comunicação Automática**  
   - Templates customizáveis.  
   - Agendamento de lembretes pré e pós-evento.  
   - Tokens únicos para RSVP.

4. **Módulo RSVP**  
   - Confirmação de presença ou recusa.  
   - Campos personalizados (acompanhante, dieta, observações).  
   - QR Code único, PDF para download e botão “Adicionar ao calendário”.

5. **Relatórios & Dashboards**  
   - Gráficos de taxa de confirmação, perfil dos convidados.  
   - Filtros por evento, grupo e status.  
   - Exportação para Excel/CSV.

6. **Usuários & Permissões**  
   - Papéis (organizador, recepção, gestor).  
   - Auditoria de ações.

7. **Integrações**  
   - SendGrid, WhatsApp Business API, Google Calendar.  
   - API RESTful e webhooks para automação externa.

---

## 🛠️ Tecnologias

- **Backend:** Django (Python 3.10+)  
- **Banco de Dados:** MySQL  
- **Frontend:** Bootstrap (templates Django)  
- **QR Code:** `qrcode` (Python)  
- **Env Variables:** `python-dotenv`  
- **Servidor de Produção:** Gunicorn + NGINX  
- **Testes:** pytest & pytest-django  

---

## 🚀 Pré-requisitos

- Python 3.10+  
- MySQL Server  
- Git  
- (Opcional) virtualenv ou venv  

---

## ⚙️ Instalação

```bash
# Clone o repositório
git clone git@github.com:blackbeans/RSVP.git
cd RSVP

# (1) Crie e ative um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# (2) Instale as dependências de sistema (Ubuntu/Debian)
sudo apt update
sudo apt install build-essential python3-dev default-libmysqlclient-dev

# (3) Instale as dependências Python
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
