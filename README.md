# 🏥 Sick House - Sistema de Gestão de Pacientes e Consultas

Sistema de gestão clínica/hospitalar desenvolvido com Django REST Framework para gerenciamento de pacientes e consultas.

## 📋 Sobre o Projeto

Sistema de gestão para clínicas e hospitais, permitindo o cadastro de pacientes, agendamento de consultas e acompanhamento médico.

### ⚙️ Funcionalidades

- ✅ Cadastro e gestão de pacientes
- ✅ Agendamento de consultas médicas
- ✅ Controle de status de consultas (Pendente, Agendada, Realizada, etc.)
- ✅ Diferentes tipos de consultas especializadas
- ✅ Múltiplos estabelecimentos de saúde
- ✅ API RESTful completa
- ✅ Interface administrativa Django

## 🚀 Tecnologias Utilizadas

- **Backend**: Django 5.2 + Django REST Framework
- **Database**: PostgreSQL
- **Autenticação**: Django REST Framework
- **CORS**: django-cors-headers
- **Python**: 3.12+

## 📦 Estrutura do Projeto

```
sick_house/
├── core/ # Configurações do projeto Django
│ ├── settings.py # Configurações principais
│ ├── urls.py # URLs principais
│ └── wsgi.py # WSGI configuration
├── pacientes/ # App de pacientes
│ ├── models.py # Modelo Paciente
│ ├── serializers.py # Serializers da API
│ ├── views.py # Views e ViewSets
│ ├── urls.py # URLs do app
│ └── admin.py # Interface admin
├── consultas/ # App de consultas
│ ├── models.py # Modelo Consulta
│ ├── serializers.py # Serializers da API
│ ├── views.py # Views e ViewSets
│ ├── urls.py # URLs do app
│ └── admin.py # Interface admin
├── manage.py # Script de administração
└── requirements.txt # Dependências do projeto
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.12+
- PostgreSQL
- pip

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd sick_house
```

### 2. Configure ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie um banco PostgreSQL e configure no `core/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sick_house_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Execute migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie superusuário

```bash
python manage.py createsuperuser
```

### 7. Execute o servidor

```bash
python manage.py runserver
```

## 🌐 API Endpoints

### Pacientes

- `GET /api/pacientes/` - Lista todos os pacientes
- `POST /api/pacientes/` - Cria novo paciente
- `GET /api/pacientes/{id}/` - Detalhes do paciente
- `PUT /api/pacientes/{id}/` - Atualiza paciente
- `DELETE /api/pacientes/{id}/` - Exclui paciente
- `GET /api/pacientes/by_cpf/?cpf=123` - Busca por CPF
- `GET /api/pacientes/by_nome/?nome=João` - Busca por nome

### Consultas

- `GET /api/consultas/` - Lista todas as consultas
- `POST /api/consultas/` - Cria nova consulta
- `GET /api/consultas/{id}/` - Detalhes da consulta
- `PUT /api/consultas/{id}/` - Atualiza consulta
- `DELETE /api/consultas/{id}/` - Exclui consulta (soft delete)
- `GET /api/consultas/by_paciente/?paciente_id=uuid` - Consultas por paciente
- `GET /api/consultas/by_status/?status=PENDENTE` - Consultas por status
- `GET /api/consultas/search/?termo=neuro` - Busca por termo

## 🎯 Modelos de Dados

### Paciente

```python
{
    "id": "uuid",
    "nome": "string",
    "data_nascimento": "date",
    "cpf": "string",
    "rg": "string",
    "cns": "string",
    "nome_do_pai": "string",
    "nome_da_mae": "string",
    "celular1": "string",
    "celular2": "string",
    "sexo": "M/F/O",
    "logradouro": "string",
    "numero": "string",
    "bairro": "string",
    "data_cadastro": "date",
    "data_ultima_consulta": "date",
    "observacao": "text",
    "email": "email"
}
```

### Consulta

```python
{
    "id": "uuid",
    "paciente": "uuid",
    "tipo_consulta": "NEUROCIRURGIAO|ORTOPEDISTA|...",
    "status": "PENDENTE|AGENDADA|...",
    "data_solicitacao": "date",
    "data_agendamento": "date",
    "estabelecimento": "POLICLINICA|SARAH|...",
    "observacao": "text",
    "motivo": "string",
    "ativo": "boolean"
}
```

## 🔧 Comandos Úteis

```bash
# Executar servidor de desenvolvimento
python manage.py runserver

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Shell do Django
python manage.py shell

# Testes
python manage.py test
```

## 👤 Acesso Administrativo

Acesse o painel admin em: http://localhost:8000/admin/

Use as credenciais do superusuário criado para gerenciar:

- Pacientes
- Consultas
- Usuários do sistema
