# Dicionário de dados

O banco vigente possui 44 tabelas de aplicação, além de `alembic_version`.

- A estrutura-base está em `src/core/database/schema.sql` e na migration `0001_initial_schema`.
- A evolução financeira e analítica está na migration `0002_financial_analytics`.
- Os relacionamentos e a ordem operacional estão documentados em `docs/modelo_financeiro.md`.

As 13 entidades introduzidas na versão `0002` são:

- categorias financeiras;
- centros de custo;
- contas bancárias;
- faturas;
- movimentações de caixa;
- itens de orçamento;
- apropriações de custo;
- metas e indicadores;
- histórico de status;
- manutenções da frota;
- abastecimentos da frota;
- utilizações da frota;
- alocações de funcionários em obras.
