# UrbanPrime ERP

ERP corporativo interno da Construtora UrbanPrime. O sistema e exclusivo para funcionarios: clientes, fornecedores e terceiros nao possuem login.

## Tecnologias

Python 3.12+, FastAPI, Streamlit, PostgreSQL, SQLAlchemy ORM, Alembic, Pydantic, Passlib + bcrypt, PyJWT, python-dotenv, cryptography/Fernet e pytest.

## Banco PostgreSQL

No pgAdmin, crie o banco `urbanprime_erp` no servidor local:

```sql
CREATE DATABASE urbanprime_erp;
```

Configuracao esperada:

- Host: `localhost`
- Porta: `5432`
- Usuario: `postgres`
- Banco: `urbanprime_erp`

A senha fica no arquivo `.env`, nunca hardcoded no codigo.

## Configuracao

O projeto ja contem um `.env` local:

```env
DATABASE_URL=postgresql+psycopg2://postgres:123@localhost:5432/urbanprime_erp
SECRET_KEY=trocar_esta_chave_em_producao
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
FERNET_KEY=gerar_chave_fernet_valida
```

Para producao, gere uma `SECRET_KEY` forte e uma chave Fernet valida.

## Instalar

```powershell
cd C:\Users\steni\OneDrive\Documents\prog\ESTUDOS\SITE\urbanprime-erp
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Migrations

```powershell
alembic upgrade head
python scripts/seed_database.py
```

O DDL completo esta em `src/core/database/schema.sql` e os dados iniciais estao em `src/core/database/seed.sql`.

## Rodar Backend

```powershell
uvicorn src.main:app --reload
```

API: `http://localhost:8000`

## Rodar Streamlit

```powershell
streamlit run src/ui/app.py
```

## Credenciais Iniciais

- Usuario: `admin`
- Senha: `Admin@123`
- E-mail: `admin@urbanprime.com`

A senha inicial no seed esta salva como hash bcrypt.

## Estrutura

- `src/main.py`: aplicacao FastAPI e registro dos controllers.
- `src/core/config`: configuracoes por variaveis de ambiente.
- `src/core/auth`: autenticacao, usuarios, perfis, permissoes, sessoes e refresh tokens.
- `src/core/security`: senha, JWT, criptografia Fernet e RBAC.
- `src/core/audit`: logs de auditoria.
- `src/core/database`: conexao, base ORM, DDL e seed.
- `src/modules`: modulos de negocio do ERP.
- `src/ui`: interface administrativa em Streamlit.
- `scripts`: automacoes de admin, seed, reset e Streamlit.
- `tests`: testes basicos de seguranca, autenticacao, banco e fluxo principal.

## Fluxo Principal do Banco

`clientes -> contratos -> projetos -> obras -> orcamentos_base`

Regras aplicadas:

- `contratos` nao possui `obra_id`.
- `projetos` possui `contrato_id`.
- `obras` possui `contrato_id` e `projeto_id`.
- `obras` nao possui `orcamento_previsto`.
- O orcamento oficial vem de `orcamentos_base`.
- `contas_pagar` possui `ordem_compra_id`.
- `usuarios.funcionario_id` referencia `funcionarios.id`.
