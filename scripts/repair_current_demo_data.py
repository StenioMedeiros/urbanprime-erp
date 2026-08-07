from __future__ import annotations

import argparse
import json
from datetime import date
from decimal import Decimal
from pathlib import Path

from sqlalchemy import MetaData, Table, select, text

from src.core.database.connection import engine


AFFECTED_TABLES = (
    "clientes",
    "fornecedores",
    "funcionarios",
    "contratos",
    "projetos",
    "revisoes_projeto",
    "obras",
    "diarios_obra",
    "cronogramas",
    "historicos_status",
    "centros_custo",
    "insumos",
    "orcamentos_base",
    "itens_orcamento",
    "cotacoes",
    "ordens_compra",
    "itens_ordem_compra",
    "contas_pagar",
    "contas_receber",
    "apropriacoes_custo",
    "faturas",
    "medicoes",
    "movimentacoes_caixa",
)


def snapshot(backup_path: Path) -> None:
    metadata = MetaData()
    metadata.reflect(bind=engine, only=AFFECTED_TABLES)
    data: dict[str, list[dict]] = {}
    with engine.connect() as connection:
        for table_name in AFFECTED_TABLES:
            table = Table(table_name, metadata, autoload_with=engine)
            rows = connection.execute(select(table).order_by(table.c.id)).mappings().all()
            data[table_name] = [dict(row) for row in rows]
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    backup_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )


def scalar(connection, query: str, **params):
    return connection.execute(text(query), params).scalar_one()


def validate_target(connection) -> None:
    recognized = scalar(
        connection,
        """
        SELECT COUNT(*)
        FROM clientes c
        JOIN contratos ct ON ct.cliente_id = c.id
        JOIN projetos p ON p.contrato_id = ct.id
        JOIN obras o ON o.projeto_id = p.id
        WHERE c.id = 1 AND ct.id = 1 AND p.id = 1 AND o.id = 1
          AND (c.nome = 'Cliente Teste UI 20260620'
               OR c.nome = 'Mercado São Cristóvão Ltda.')
        """,
    )
    if recognized != 1:
        raise RuntimeError(
            "A base não contém a cadeia demonstrativa conhecida. Nenhum dado foi alterado."
        )


def update_legacy_chain(connection) -> None:
    connection.execute(
        text(
            """
            UPDATE clientes SET
                nome = 'Mercado São Cristóvão Ltda.',
                tipo_pessoa = 'juridica',
                cpf_cnpj = '90.000.013/0001-01',
                email = 'contato@mercadosaocristovao.exemplo',
                telefone = '(87) 3761-1300',
                endereco = 'Rua São Cristóvão, 310 - Boa Vista',
                cidade = 'Garanhuns', estado = 'PE', cep = '55292-310',
                status = 'ativo', updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE fornecedores SET
                razao_social = 'Materiais São Cristóvão Ltda.',
                nome_fantasia = 'Depósito São Cristóvão',
                cnpj = '90.000.014/0001-02',
                email = 'vendas@depositosaocristovao.exemplo',
                telefone = '(87) 3761-1310',
                endereco = 'Avenida Caruaru, 820 - São José, Garanhuns - PE',
                status = 'ativo', updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE funcionarios SET
                nome = 'Rafael Henrique Melo',
                cpf = '000.000.013-04', rg = '13.000.004-PE',
                data_nascimento = DATE '1992-04-18',
                email_corporativo = 'rafael.melo@urbanprime.com',
                telefone = '(87) 99913-0404', cargo = 'Engenheiro civil',
                setor = 'engenharia', data_admissao = DATE '2025-01-06',
                salario_base = 9200.00, status = 'ativo', updated_at = NOW()
            WHERE id = 4
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE contratos SET
                numero_contrato = 'UP-2026-013',
                descricao = 'Contrato para reforma e ampliação do Mercado São Cristóvão.',
                data_assinatura = DATE '2026-06-15',
                data_inicio = DATE '2026-06-20', data_fim = DATE '2026-12-20',
                status = 'ativo', updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE projetos SET
                nome = 'Reforma do Mercado São Cristóvão',
                descricao = 'Projeto executivo para reforma e ampliação comercial em Garanhuns.',
                tipo_projeto = 'comercial', data_inicio = DATE '2026-06-20',
                data_previsao_entrega = DATE '2026-11-30',
                status = 'em_elaboracao', updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE obras SET
                nome = 'Reforma e ampliação do Mercado São Cristóvão',
                descricao = 'Reforma do salão de vendas, depósito e área administrativa.',
                endereco = 'Rua São Cristóvão, 310 - Boa Vista',
                cidade = 'Garanhuns', estado = 'PE', cep = '55292-310',
                data_inicio = DATE '2026-07-01',
                data_previsao_fim = DATE '2026-12-15',
                status = 'planejada', updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE centros_custo SET
                nome = 'Reforma e ampliação do Mercado São Cristóvão',
                descricao = 'Centro de custo exclusivo da reforma comercial.',
                updated_at = NOW()
            WHERE obra_id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE insumos SET
                nome = 'Aditivo impermeabilizante 18 L',
                descricao = 'Aditivo impermeabilizante para concretos e argamassas.',
                unidade_medida = 'balde', updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE orcamentos_base SET
                descricao = 'Orçamento-base — Reforma do Mercado São Cristóvão',
                updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE ordens_compra SET
                numero = 'OC-2026-013', data_emissao = DATE '2026-06-20',
                data_aprovacao = DATE '2026-06-21', status = 'aprovada',
                updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE contas_pagar SET
                descricao = 'Compra de aditivo impermeabilizante — Mercado São Cristóvão',
                updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE contas_receber SET
                descricao = 'Parcela contratual — Reforma do Mercado São Cristóvão',
                categoria_financeira_id = (
                    SELECT id FROM categorias_financeiras WHERE codigo = 'REC_SERVICOS'
                ),
                centro_custo_id = (SELECT id FROM centros_custo WHERE obra_id = 1),
                numero_documento = 'REC-UP-2026-0013',
                data_competencia = DATE '2026-06-20', updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE apropriacoes_custo SET
                descricao = 'Apropriação de custo — Reforma do Mercado São Cristóvão',
                updated_at = NOW()
            WHERE id = 1
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE historicos_status SET
                observacao = 'Situação inicial registrada para a Reforma do Mercado São Cristóvão',
                updated_at = NOW()
            WHERE entidade = 'obras' AND entidade_id = 1
            """
        )
    )


def complete_operational_relations(connection) -> None:
    if scalar(connection, "SELECT COUNT(*) FROM revisoes_projeto WHERE projeto_id = 1") == 0:
        connection.execute(
            text(
                """
                INSERT INTO revisoes_projeto
                    (projeto_id, responsavel_id, numero_revisao, descricao, motivo,
                     arquivo_revisao, data_revisao, aprovado)
                VALUES
                    (1, 4, 1, 'Revisão inicial — Reforma do Mercado São Cristóvão',
                     'Compatibilização inicial das disciplinas',
                     'demo/reforma-mercado-sao-cristovao-r01.pdf', DATE '2026-06-25', false)
                """
            )
        )
    if scalar(connection, "SELECT COUNT(*) FROM diarios_obra WHERE obra_id = 1") == 0:
        connection.execute(
            text(
                """
                INSERT INTO diarios_obra
                    (obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias)
                VALUES
                    (1, 4, DATE '2026-07-01', 'ensolarado',
                     'Mobilização da equipe e isolamento das áreas de intervenção.',
                     'Operação inicial sem ocorrências críticas.')
                """
            )
        )
    if scalar(connection, "SELECT COUNT(*) FROM cronogramas WHERE obra_id = 1") == 0:
        connection.execute(
            text(
                """
                INSERT INTO cronogramas
                    (obra_id, atividade, data_inicio, data_fim, peso_percentual,
                     percentual_concluido, status)
                VALUES
                    (1, 'Mobilização e preparação do canteiro', DATE '2026-07-01',
                     DATE '2026-07-15', 10, 100, 'concluido')
                """
            )
        )

    missing_history = connection.execute(
        text(
            """
            SELECT o.id, o.status, o.nome
            FROM obras o
            WHERE NOT EXISTS (
                SELECT 1 FROM historicos_status hs
                WHERE hs.entidade = 'obras' AND hs.entidade_id = o.id
            )
            """
        )
    ).mappings().all()
    for work in missing_history:
        connection.execute(
            text(
                """
                INSERT INTO historicos_status
                    (entidade, entidade_id, status_anterior, status_novo,
                     data_alteracao, observacao)
                VALUES
                    ('obras', :work_id, NULL, :status, NOW(), :observation)
                """
            ),
            {
                "work_id": work["id"],
                "status": work["status"],
                "observation": f"Situação inicial registrada para {work['nome']}",
            },
        )

    missing_centers = connection.execute(
        text(
            """
            SELECT o.id, o.nome, o.responsavel_id
            FROM obras o
            WHERE NOT EXISTS (SELECT 1 FROM centros_custo cc WHERE cc.obra_id = o.id)
            ORDER BY o.id
            """
        )
    ).mappings().all()
    for work in missing_centers:
        connection.execute(
            text(
                """
                INSERT INTO centros_custo
                    (codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo)
                VALUES
                    (:code, :name, 'obra', :work_id, :responsible,
                     'Centro de custo exclusivo da obra.', true)
                """
            ),
            {
                "code": f"OBRA-{work['id']:03d}",
                "name": work["nome"],
                "work_id": work["id"],
                "responsible": work["responsavel_id"],
            },
        )


def complete_purchases_and_budgets(connection) -> None:
    missing_quotes = connection.execute(
        text(
            """
            SELECT oc.id, oc.fornecedor_id, oc.obra_id, oc.numero, oc.valor_total,
                   COALESCE(oc.data_emissao, CURRENT_DATE) AS data_emissao,
                   o.nome AS obra
            FROM ordens_compra oc
            LEFT JOIN obras o ON o.id = oc.obra_id
            WHERE oc.cotacao_id IS NULL
            ORDER BY oc.id
            """
        )
    ).mappings().all()
    for order in missing_quotes:
        quote_id = connection.execute(
            text(
                """
                SELECT id FROM cotacoes
                WHERE fornecedor_id = :supplier
                  AND (obra_id = :work OR (obra_id IS NULL AND :work IS NULL))
                ORDER BY id DESC LIMIT 1
                """
            ),
            {"supplier": order["fornecedor_id"], "work": order["obra_id"]},
        ).scalar_one_or_none()
        if quote_id is None:
            quote_id = connection.execute(
                text(
                    """
                    INSERT INTO cotacoes
                        (fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status)
                    VALUES
                        (:supplier, :work, :description, :value, :quote_date, 'aprovada')
                    RETURNING id
                    """
                ),
                {
                    "supplier": order["fornecedor_id"],
                    "work": order["obra_id"],
                    "description": f"Cotação de materiais — {order['obra'] or order['numero']}",
                    "value": order["valor_total"],
                    "quote_date": order["data_emissao"],
                },
            ).scalar_one()
        connection.execute(
            text(
                """
                UPDATE ordens_compra SET
                    cotacao_id = :quote_id,
                    data_emissao = COALESCE(data_emissao, :issue_date),
                    data_aprovacao = COALESCE(data_aprovacao, :issue_date + 2),
                    updated_at = NOW()
                WHERE id = :order_id
                """
            ),
            {
                "quote_id": quote_id,
                "issue_date": order["data_emissao"],
                "order_id": order["id"],
            },
        )

    if scalar(connection, "SELECT COUNT(*) FROM itens_ordem_compra WHERE ordem_compra_id = 1") == 0:
        connection.execute(
            text(
                """
                INSERT INTO itens_ordem_compra
                    (ordem_compra_id, insumo_id, descricao, quantidade,
                     valor_unitario, valor_total)
                VALUES
                    (1, 1, 'Aditivo impermeabilizante 18 L', 10, 50, 500)
                """
            )
        )

    category_codes = {
        "MAT": ("Materiais e insumos", "Materiais", Decimal("0.35"), "DES_MATERIAIS"),
        "MAO": ("Mão de obra direta", "Mão de obra", Decimal("0.30"), "DES_MAO_OBRA"),
        "EQP": ("Equipamentos e logística", "Equipamentos", Decimal("0.15"), "DES_EQUIPAMENTOS"),
        "TER": ("Serviços especializados", "Terceirizados", Decimal("0.20"), "DES_TERCEIROS"),
    }
    missing_budgets = connection.execute(
        text(
            """
            SELECT ob.id, ob.valor_total
            FROM orcamentos_base ob
            WHERE NOT EXISTS (
                SELECT 1 FROM itens_orcamento io WHERE io.orcamento_base_id = ob.id
            )
            ORDER BY ob.id
            """
        )
    ).mappings().all()
    for budget in missing_budgets:
        total = Decimal(budget["valor_total"])
        for prefix, (description, stage, fraction, category_code) in category_codes.items():
            amount = (total * fraction).quantize(Decimal("0.01"))
            connection.execute(
                text(
                    """
                    INSERT INTO itens_orcamento
                        (orcamento_base_id, categoria_financeira_id, codigo, etapa,
                         descricao, unidade_medida, quantidade, valor_unitario, valor_total)
                    VALUES
                        (:budget, (SELECT id FROM categorias_financeiras WHERE codigo = :category),
                         :code, :stage, :description, 'vb', 1, :amount, :amount)
                    """
                ),
                {
                    "budget": budget["id"],
                    "category": category_code,
                    "code": f"{prefix}-{budget['id']:03d}",
                    "stage": stage,
                    "description": description,
                    "amount": amount,
                },
            )


def complete_financial_links(connection) -> None:
    connection.execute(
        text(
            """
            UPDATE contas_pagar cp SET
                categoria_financeira_id = COALESCE(
                    cp.categoria_financeira_id,
                    (SELECT id FROM categorias_financeiras WHERE codigo = 'DES_MATERIAIS')
                ),
                centro_custo_id = COALESCE(
                    cp.centro_custo_id,
                    (SELECT id FROM centros_custo WHERE obra_id = cp.obra_id)
                ),
                data_competencia = COALESCE(cp.data_competencia, cp.data_vencimento),
                numero_documento = COALESCE(
                    cp.numero_documento,
                    'DOC-PAG-2026-' || LPAD(cp.id::text, 4, '0')
                ),
                updated_at = NOW()
            WHERE cp.categoria_financeira_id IS NULL
               OR cp.centro_custo_id IS NULL
               OR cp.data_competencia IS NULL
               OR cp.numero_documento IS NULL
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE contas_receber cr SET
                categoria_financeira_id = COALESCE(
                    cr.categoria_financeira_id,
                    (SELECT id FROM categorias_financeiras WHERE codigo = 'REC_SERVICOS')
                ),
                centro_custo_id = COALESCE(
                    cr.centro_custo_id,
                    (
                        SELECT cc.id
                        FROM obras o
                        JOIN centros_custo cc ON cc.obra_id = o.id
                        WHERE o.contrato_id = cr.contrato_id
                        ORDER BY o.id LIMIT 1
                    )
                ),
                data_competencia = COALESCE(cr.data_competencia, cr.data_vencimento),
                numero_documento = COALESCE(
                    cr.numero_documento,
                    'REC-UP-2026-' || LPAD(cr.id::text, 4, '0')
                ),
                updated_at = NOW()
            WHERE cr.categoria_financeira_id IS NULL
               OR cr.centro_custo_id IS NULL
               OR cr.data_competencia IS NULL
               OR cr.numero_documento IS NULL
            """
        )
    )

    bank_account_id = scalar(
        connection,
        "SELECT id FROM contas_bancarias WHERE ativo = true ORDER BY id LIMIT 1",
    )
    received_without_cash = connection.execute(
        text(
            """
            SELECT cr.id, cr.fatura_id, cr.categoria_financeira_id, cr.centro_custo_id,
                   cr.valor, cr.data_recebimento, cr.numero_documento
            FROM contas_receber cr
            WHERE cr.status = 'recebido' AND cr.fatura_id IS NOT NULL
              AND NOT EXISTS (
                  SELECT 1 FROM movimentacoes_caixa mc
                  WHERE mc.tipo = 'entrada'
                    AND (mc.conta_receber_id = cr.id OR mc.fatura_id = cr.fatura_id)
              )
            """
        )
    ).mappings().all()
    for receivable in received_without_cash:
        connection.execute(
            text(
                """
                INSERT INTO movimentacoes_caixa
                    (conta_bancaria_id, conta_receber_id, fatura_id,
                     categoria_financeira_id, centro_custo_id, tipo,
                     data_movimentacao, valor, descricao, forma_pagamento,
                     conciliado, data_conciliacao)
                VALUES
                    (:bank, :receivable, :invoice, :category, :center, 'entrada',
                     :payment_date, :value, :description, 'transferencia', true,
                     :payment_date)
                """
            ),
            {
                "bank": bank_account_id,
                "receivable": receivable["id"],
                "invoice": receivable["fatura_id"],
                "category": receivable["categoria_financeira_id"],
                "center": receivable["centro_custo_id"],
                "payment_date": receivable["data_recebimento"] or date.today(),
                "value": receivable["valor"],
                "description": f"Recebimento {receivable['numero_documento']}",
            },
        )

    paid_without_cash = connection.execute(
        text(
            """
            SELECT cp.id, cp.categoria_financeira_id, cp.centro_custo_id,
                   cp.valor, cp.data_pagamento, cp.numero_documento
            FROM contas_pagar cp
            WHERE cp.status = 'pago' AND cp.data_pagamento IS NOT NULL
              AND NOT EXISTS (
                  SELECT 1 FROM movimentacoes_caixa mc
                  WHERE mc.tipo = 'saida' AND mc.conta_pagar_id = cp.id
              )
            """
        )
    ).mappings().all()
    for payable in paid_without_cash:
        connection.execute(
            text(
                """
                INSERT INTO movimentacoes_caixa
                    (conta_bancaria_id, conta_pagar_id, categoria_financeira_id,
                     centro_custo_id, tipo, data_movimentacao, valor, descricao,
                     forma_pagamento, conciliado, data_conciliacao)
                VALUES
                    (:bank, :payable, :category, :center, 'saida', :payment_date,
                     :value, :description, 'transferencia', true, :payment_date)
                """
            ),
            {
                "bank": bank_account_id,
                "payable": payable["id"],
                "category": payable["categoria_financeira_id"],
                "center": payable["centro_custo_id"],
                "payment_date": payable["data_pagamento"],
                "value": payable["valor"],
                "description": f"Pagamento {payable['numero_documento']}",
            },
        )

    connection.execute(
        text(
            """
            UPDATE movimentacoes_caixa mc SET conta_receber_id = cr.id
            FROM contas_receber cr
            WHERE mc.tipo = 'entrada' AND mc.fatura_id = cr.fatura_id
              AND mc.conta_receber_id IS NULL
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE contas_receber cr SET
                status = 'recebido',
                data_recebimento = COALESCE(
                    cr.data_recebimento,
                    (
                        SELECT MIN(mc.data_movimentacao)
                        FROM movimentacoes_caixa mc
                        WHERE mc.tipo = 'entrada'
                          AND (mc.conta_receber_id = cr.id OR mc.fatura_id = cr.fatura_id)
                    )
                ),
                updated_at = NOW()
            WHERE EXISTS (
                SELECT 1 FROM movimentacoes_caixa mc
                WHERE mc.tipo = 'entrada'
                  AND (mc.conta_receber_id = cr.id OR mc.fatura_id = cr.fatura_id)
            )
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE faturas f SET status = 'recebida', updated_at = NOW()
            WHERE EXISTS (
                SELECT 1 FROM movimentacoes_caixa mc
                WHERE mc.tipo = 'entrada' AND mc.fatura_id = f.id
            )
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE faturas f SET status = 'emitida', updated_at = NOW()
            WHERE NOT EXISTS (
                SELECT 1 FROM movimentacoes_caixa mc
                WHERE mc.tipo = 'entrada' AND mc.fatura_id = f.id
            )
            """
        )
    )
    connection.execute(
        text(
            """
            UPDATE medicoes m SET
                status = CASE
                    WHEN f.status = 'recebida' THEN 'recebida'
                    ELSE 'faturada'
                END,
                updated_at = NOW()
            FROM faturas f
            WHERE f.medicao_id = m.id
            """
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Corrige lacunas conhecidas da base demonstrativa atual."
    )
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--backup", type=Path)
    args = parser.parse_args()

    with engine.connect() as connection:
        validate_target(connection)
    if not args.apply:
        print("Base reconhecida. Use --apply e informe --backup para executar.")
        return
    if args.backup is None:
        raise SystemExit("--backup é obrigatório quando --apply é utilizado.")

    snapshot(args.backup)
    with engine.begin() as connection:
        validate_target(connection)
        update_legacy_chain(connection)
        complete_operational_relations(connection)
        complete_purchases_and_budgets(connection)
        complete_financial_links(connection)
    print(f"Correções aplicadas. Backup: {args.backup}")


if __name__ == "__main__":
    main()
