# UrbanPrime ERP

Sistema integrado de gestão empresarial para a Construtora UrbanPrime.

## Integrantes da equipe

- **João Victor Leite Dos Santos**
- **Stênio Medeiros Freitas**
- **Thiago Ferreira Da Silva**

## 1. Descrição do sistema

O UrbanPrime ERP é um sistema corporativo interno para centralizar os processos de uma construtora. A aplicação integra as áreas Administrativa e de Segurança, Comercial, Engenharia e Projetos, Gestão de Obras, Financeiro, Compras e Estoque, Frota e Equipamentos e Recursos Humanos.

O sistema permite acompanhar clientes, contratos, projetos, obras, cronogramas, diários, medições, orçamentos, compras, estoque, contas, faturamento, caixa, equipamentos, funcionários e auditoria. O Dashboard consolida os registros em indicadores, séries históricas e projeções gerenciais.

Clientes, fornecedores e terceiros não possuem acesso direto. O login é destinado aos funcionários autorizados, de acordo com seus perfis e permissões.

## 2. Tecnologias e versões utilizadas

- Python `3.12.13`;
- PostgreSQL `18.4`;
- Streamlit `1.58.0`;
- FastAPI `0.137.2`;
- SQLAlchemy `2.0.51`;
- Alembic `1.18.4`;
- Pandas `3.0.3`;
- Pydantic `2.13.4`.

Todas as bibliotecas e suas versões exatas estão informadas no arquivo `requirements.txt`.

## 3. Requisitos de software

Antes de iniciar, o computador deve possuir:

- Python `3.12.13` instalado e disponível no terminal;
- PostgreSQL `18.4` com o servidor em execução;
- ferramentas `psql` e `pg_restore`, instaladas com o PostgreSQL;
- `pip`, incluído na instalação do Python;
- navegador atualizado;
- porta `5432` disponível para o PostgreSQL;
- porta `8501` disponível para o Streamlit.

O pgAdmin pode ser utilizado para criar o banco e executar os scripts SQL caso `psql` não esteja disponível no `PATH` do sistema.

## 4. Conteúdo principal da entrega

- `src/`: código-fonte da aplicação;
- `database/schema.sql`: estrutura completa das 45 tabelas;
- `database/dados.sql`: dados necessários, exportados com comandos `INSERT`;
- `database/banco.backup`: backup completo alternativo do PostgreSQL;
- `.env.exemplo`: modelo de configuração sem credenciais reais;
- `requirements.txt`: dependências com versões fixadas;
- `alembic/`: histórico das alterações de estrutura do banco;
- `docs/`: documentação complementar dos módulos e regras;
- `scripts/`: rotinas auxiliares de administração e desenvolvimento;
- `tests/`: testes automatizados do projeto.

## 5. Preparação do ambiente Python

Abra o PowerShell na pasta em que o projeto foi extraído:

```powershell
cd caminho\onde\o\projeto\foi\extraido
```

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente virtual no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, libere scripts somente para a sessão atual e tente novamente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instale todas as dependências:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 6. Criação e restauração do banco PostgreSQL

O banco utilizado pela aplicação se chama `urbanprime_erp`. A configuração padrão considera:

- host: `localhost`;
- porta: `5432`;
- usuário: definido na instalação local do PostgreSQL;
- banco: `urbanprime_erp`.

Crie um banco vazio pelo pgAdmin ou execute:

```powershell
psql -h localhost -p 5432 -U postgres -d postgres -c "CREATE DATABASE urbanprime_erp WITH ENCODING 'UTF8';"
```

Escolha apenas uma das opções de restauração abaixo.

### Opção A - Restaurar `schema.sql` e `dados.sql` (principal)

Execute primeiro a estrutura e depois os dados, respeitando esta ordem:

```powershell
psql -h localhost -p 5432 -U postgres -d urbanprime_erp -v ON_ERROR_STOP=1 -f database\schema.sql
psql -h localhost -p 5432 -U postgres -d urbanprime_erp -v ON_ERROR_STOP=1 -f database\dados.sql
```

O `schema.sql` contém tabelas, sequências, chaves primárias, chaves estrangeiras, índices e restrições. O `dados.sql` contém os registros e os valores atuais das sequências.

### Opção B - Restaurar `banco.backup` (alternativa)

Se preferir o backup completo, não execute os dois scripts da opção A. Depois de criar o banco vazio, execute:

```powershell
pg_restore -h localhost -p 5432 -U postgres -d urbanprime_erp --no-owner --no-privileges --exit-on-error database\banco.backup
```

Os três artefatos foram produzidos pelo PostgreSQL `18.4` e validados por restauração em banco temporário.

## 7. Configuração do arquivo `.env`

O sistema lê as configurações do arquivo local `.env`. Crie esse arquivo copiando o modelo fornecido:

```powershell
Copy-Item .env.exemplo .env
```

Edite somente o novo `.env` e substitua os marcadores demonstrativos:

```env
DATABASE_URL=postgresql+psycopg2://SEU_USUARIO:SUA_SENHA@localhost:5432/urbanprime_erp
SECRET_KEY=SUBSTITUA_POR_UMA_CHAVE_SECRETA_COM_PELO_MENOS_32_CARACTERES
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
FERNET_KEY=SUBSTITUA_POR_UMA_CHAVE_FERNET_VALIDA
APP_TIMEZONE=America/Recife
APP_LOCALE=pt_BR
APP_CURRENCY=BRL
DEFAULT_CITY=Garanhuns
DEFAULT_STATE=PE
```

Para gerar a `SECRET_KEY` e a `FERNET_KEY`, execute:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(48))"
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Copie o primeiro resultado para `SECRET_KEY` e o segundo para `FERNET_KEY`. Informe na `DATABASE_URL` o usuário e a senha definidos no PostgreSQL do computador em que o sistema será executado.

O `.env` contém dados locais e não deve ser enviado, publicado ou adicionado ao Git. Apenas o `.env.exemplo` faz parte da entrega.

## 8. Executar a aplicação Streamlit

Com o ambiente virtual ativado, na raiz do projeto, execute exatamente:

```powershell
python -m streamlit run src\ui\app.py
```

Após a inicialização, acesse:

```text
http://localhost:8501
```

## 9. Usuário administrador para avaliação

- usuário: `admin`;
- senha: `Admin@123`;
- e-mail: `admin@urbanprime.com`.

A senha está armazenada no banco somente como hash bcrypt. Essa conta é demonstrativa e foi incluída para permitir a avaliação do sistema.

## 10. Executar os testes

Para verificar o projeto antes de iniciar a interface:

```powershell
python -m pytest -q
```

## 11. API FastAPI (opcional)

O Streamlit é a interface principal solicitada para avaliação. O backend FastAPI também pode ser iniciado, em outro terminal com o ambiente virtual ativado, usando:

```powershell
python -m uvicorn src.main:app --reload
```

A API ficará disponível em `http://localhost:8000` e a documentação automática em `http://localhost:8000/docs`.

## 12. Estrutura resumida do projeto

- `src/main.py`: entrada da API FastAPI;
- `src/core/config`: leitura das variáveis de ambiente;
- `src/core/auth`: autenticação, usuários, perfis e sessões;
- `src/core/security`: senhas, JWT, criptografia e permissões;
- `src/core/audit`: histórico de acessos e alterações;
- `src/core/database`: conexão, modelos-base e arquivos históricos de desenvolvimento;
- `src/modules`: regras e funcionalidades de negócio;
- `src/ui`: aplicação Streamlit;
- `alembic`: migrações de desenvolvimento do banco;
- `database`: arquivos oficiais de reconstrução do banco para a entrega;
- `docs`: documentação funcional e técnica;
- `scripts`: rotinas auxiliares;
- `tests`: testes automatizados.

## 13. Observações importantes

- Todos os comandos devem ser executados a partir da raiz do projeto.
- Não restaure `schema.sql` e `banco.backup` no mesmo banco; escolha somente uma opção.
- Depois de restaurar os arquivos oficiais de entrega, não execute `alembic upgrade head`, pois o banco já estará na revisão `0002_financial_analytics`.
- Os arquivos `src/core/database/schema.sql` e `src/core/database/seed.sql` são históricos do desenvolvimento. Para a entrega, utilize exclusivamente os arquivos da pasta `database/`.
- O sistema utiliza o horário de Garanhuns/PE (`America/Recife`), datas brasileiras e valores em real.
- O PostgreSQL pode solicitar a senha do usuário durante a criação ou restauração do banco.
- Se `psql` ou `pg_restore` não forem reconhecidos, execute-os a partir da pasta `bin` da instalação do PostgreSQL ou use o pgAdmin.
- Não altere o código-fonte para configurar outro computador; ajuste somente o `.env` local.
- A aplicação deve ser encerrada no terminal com `Ctrl+C`.
