# Modelo financeiro e analítico

## Ordem do fluxo

1. Cliente
2. Contrato
3. Projeto
4. Obra e centro de custo
5. Orçamento-base e itens do orçamento
6. Cronograma e execução da obra
7. Medição
8. Fatura
9. Conta a receber
10. Movimentação de caixa de entrada

O fluxo de despesas segue:

1. Fornecedor e cotação
2. Ordem de compra
3. Conta a pagar
4. Apropriação do custo na obra
5. Movimentação de caixa de saída

## Regras estruturais

- Chaves primárias são inteiros gerados pelo PostgreSQL.
- Chaves estrangeiras obrigatórias usam `RESTRICT` ou `CASCADE` conforme a propriedade do registro.
- Vínculos analíticos opcionais usam `SET NULL`, preservando o histórico financeiro.
- Uma obra possui no máximo um centro de custo próprio.
- Uma fatura sempre pertence a um cliente e pode apontar para contrato, obra e medição.
- Contas a pagar e receber representam obrigações; movimentações de caixa representam realização.
- Apropriações de custo atribuem despesas a obras sem duplicar a obrigação financeira.
- Itens de orçamento representam o previsto; apropriações representam o realizado.

## Novas entidades

- `categorias_financeiras`
- `centros_custo`
- `contas_bancarias`
- `faturas`
- `movimentacoes_caixa`
- `itens_orcamento`
- `apropriacoes_custo`
- `metas_indicadores`
- `historicos_status`
- `manutencoes_frota`
- `abastecimentos_frota`
- `utilizacoes_frota`
- `alocacoes_funcionario_obra`
