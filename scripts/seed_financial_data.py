"""Popula o núcleo financeiro e analítico com dados coerentes e idempotentes."""

from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
import sys

from sqlalchemy import create_engine, text

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.core.config.settings import get_settings


CATEGORIES = [
    ("REC_MEDICOES", "Receita de medições", "receita"),
    ("REC_SERVICOS", "Receita de serviços", "receita"),
    ("REC_OUTRAS", "Outras receitas operacionais", "receita"),
    ("DES_MATERIAIS", "Materiais de construção", "despesa"),
    ("DES_MAO_OBRA", "Mão de obra", "despesa"),
    ("DES_EQUIPAMENTOS", "Equipamentos e locações", "despesa"),
    ("DES_COMBUSTIVEL", "Combustíveis", "despesa"),
    ("DES_MANUTENCAO", "Manutenção de frota", "despesa"),
    ("DES_TERCEIROS", "Serviços terceirizados", "despesa"),
    ("DES_IMPOSTOS", "Impostos e retenções", "despesa"),
    ("DES_ADMIN", "Despesas administrativas", "despesa"),
    ("DES_LOGISTICA", "Fretes e logística", "despesa"),
    ("DES_SEGUROS", "Seguros", "despesa"),
    ("DES_FINANCEIRAS", "Despesas financeiras", "despesa"),
]

ACCOUNTS = [
    ("Banco do Brasil", "1234-5", "10001-1", "Operacional"),
    ("Caixa Econômica Federal", "0067", "20002-2", "Recebimentos de obras"),
    ("Santander", "4040", "30003-3", "Folha de pagamento"),
    ("Sicredi", "2201", "40004-4", "Reserva e investimentos"),
    ("Itaú", "1678", "50005-5", "Recebimentos comerciais"),
    ("Bradesco", "3120", "60006-6", "Pagamentos a fornecedores"),
    ("Nubank PJ", "0001", "70007-7", "Despesas administrativas"),
    ("Banco do Nordeste", "0088", "80008-8", "Financiamento de equipamentos"),
    ("Sicoob", "4410", "90009-9", "Conta de obras"),
    ("Caixa interno", None, "CAIXA-001", "Pequenas despesas"),
]


def one(conn, sql, **params):
    return conn.execute(text(sql), params).scalar_one()


def ensure(conn, table, key_column, key_value, **values):
    found = conn.execute(
        text(f'SELECT id FROM "{table}" WHERE "{key_column}"=:value LIMIT 1'),
        {"value": key_value},
    ).scalar_one_or_none()
    if found is not None:
        return found
    payload = {key_column: key_value, **values}
    columns = ", ".join(f'"{column}"' for column in payload)
    placeholders = ", ".join(f':{column}' for column in payload)
    return conn.execute(
        text(f'INSERT INTO "{table}" ({columns}) VALUES ({placeholders}) RETURNING id'), payload
    ).scalar_one()


def main():
    engine = create_engine(get_settings().database_url, pool_pre_ping=True)
    today = date.today()
    with engine.begin() as conn:
        category_ids = {}
        for code, name, category_type in CATEGORIES:
            category_ids[code] = ensure(
                conn, "categorias_financeiras", "codigo", code,
                nome=name, tipo=category_type,
                descricao=f"Categoria gerencial: {name.lower()}.", contabilizavel=True, ativo=True,
            )

        bank_account_ids = []
        for i, (bank, agency, account, description) in enumerate(ACCOUNTS, 1):
            bank_account_ids.append(ensure(
                conn, "contas_bancarias", "numero_conta", account,
                banco=bank, agencia=agency, tipo_conta="caixa" if i == 10 else "corrente",
                descricao=description, saldo_inicial=Decimal("25000.00") * i,
                data_saldo_inicial=date(2026, 1, 1), ativo=True,
            ))

        works = conn.execute(text("SELECT id, nome, responsavel_id, status FROM obras ORDER BY id LIMIT 12")).mappings().all()
        employees = conn.execute(text("SELECT id, nome, cargo, salario_base FROM funcionarios ORDER BY id LIMIT 12")).mappings().all()
        fleets = conn.execute(text("SELECT id, identificacao FROM frotas ORDER BY id LIMIT 12")).mappings().all()
        suppliers = conn.execute(text("SELECT id FROM fornecedores ORDER BY id LIMIT 12")).scalars().all()

        center_ids = []
        for i, work in enumerate(works, 1):
            center_id = ensure(
                conn, "centros_custo", "codigo", f"OBRA-{i:03d}",
                nome=f"{work['nome']}", tipo="obra", obra_id=work["id"],
                responsavel_id=work["responsavel_id"], descricao="Centro de custo exclusivo da obra.", ativo=True,
            )
            center_ids.append(center_id)
            progress = Decimal("100") if work["status"] == "concluida" else Decimal(str(42 + i * 3)) if work["status"] == "em_andamento" else Decimal(str(5 + i))
            conn.execute(text("UPDATE obras SET percentual_fisico=:progress WHERE id=:id"), {"progress": min(progress, Decimal("100")), "id": work["id"]})
        ensure(conn, "centros_custo", "codigo", "ADMIN-001", nome="Administração central", tipo="administrativo", descricao="Custos gerais do escritório.", ativo=True)
        ensure(conn, "centros_custo", "codigo", "FROTA-001", nome="Frota e equipamentos", tipo="frota", descricao="Custos compartilhados da frota.", ativo=True)
        ensure(conn, "centros_custo", "codigo", "ALMOX-001", nome="Almoxarifado central", tipo="estoque", descricao="Custos de estoque e logística.", ativo=True)

        measurements = conn.execute(text("""
            SELECT m.id, m.obra_id, m.contrato_id, m.competencia, m.valor_medido,
                   COALESCE(o.contrato_id, m.contrato_id) AS contrato_ref, c.cliente_id
            FROM medicoes m
            JOIN obras o ON o.id=m.obra_id
            JOIN contratos c ON c.id=COALESCE(o.contrato_id, m.contrato_id)
            ORDER BY m.id LIMIT 12
        """)).mappings().all()
        invoice_ids = []
        for i, measurement in enumerate(measurements, 1):
            gross = Decimal(measurement["valor_medido"])
            taxes = (gross * Decimal("0.02")).quantize(Decimal("0.01"))
            withholdings = (gross * Decimal("0.03")).quantize(Decimal("0.01"))
            net = gross - taxes - withholdings
            issue_date = date(2026, min(i, 12), 5)
            invoice_id = ensure(
                conn, "faturas", "numero_documento", f"NF-UP-2026-{i:04d}",
                cliente_id=measurement["cliente_id"], contrato_id=measurement["contrato_ref"],
                obra_id=measurement["obra_id"], medicao_id=measurement["id"],
                data_emissao=issue_date, competencia=measurement["competencia"], valor_bruto=gross,
                impostos=taxes, retencoes=withholdings, valor_liquido=net,
                data_vencimento=issue_date + timedelta(days=30),
                status="recebida" if i % 4 == 0 else "emitida", observacao="Faturamento vinculado à medição da obra.",
            )
            invoice_ids.append(invoice_id)
            receivable = conn.execute(text("SELECT id FROM contas_receber WHERE medicao_id=:id LIMIT 1"), {"id": measurement["id"]}).scalar_one_or_none()
            if receivable:
                conn.execute(text("""
                    UPDATE contas_receber SET fatura_id=:fatura, categoria_financeira_id=:categoria,
                           centro_custo_id=:centro, numero_documento=:documento,
                           data_competencia=:competencia, valor=:valor
                    WHERE id=:id
                """), {
                    "fatura": invoice_id, "categoria": category_ids["REC_MEDICOES"],
                    "centro": center_ids[(i - 1) % len(center_ids)], "documento": f"NF-UP-2026-{i:04d}",
                    "competencia": issue_date, "valor": net, "id": receivable,
                })

        payables = conn.execute(text("SELECT id, obra_id, valor, data_vencimento FROM contas_pagar ORDER BY id LIMIT 12")).mappings().all()
        expense_codes = ["DES_MATERIAIS", "DES_TERCEIROS", "DES_EQUIPAMENTOS", "DES_COMBUSTIVEL"]
        for i, payable in enumerate(payables, 1):
            work_index = next((index for index, work in enumerate(works) if work["id"] == payable["obra_id"]), (i - 1) % len(center_ids))
            conn.execute(text("""
                UPDATE contas_pagar SET categoria_financeira_id=:categoria, centro_custo_id=:centro,
                       numero_documento=:documento, data_competencia=:competencia WHERE id=:id
            """), {
                "categoria": category_ids[expense_codes[(i - 1) % len(expense_codes)]],
                "centro": center_ids[work_index], "documento": f"DOC-PAG-2026-{i:04d}",
                "competencia": payable["data_vencimento"], "id": payable["id"],
            })

        budgets = conn.execute(text("SELECT id, obra_id, valor_total FROM orcamentos_base ORDER BY id LIMIT 12")).mappings().all()
        budget_parts = [
            ("MAT", "Materiais e insumos", "Materiais", Decimal("0.35"), "DES_MATERIAIS"),
            ("MAO", "Mão de obra direta", "Mão de obra", Decimal("0.30"), "DES_MAO_OBRA"),
            ("EQP", "Equipamentos e logística", "Equipamentos", Decimal("0.15"), "DES_EQUIPAMENTOS"),
            ("TER", "Serviços especializados", "Terceirizados", Decimal("0.20"), "DES_TERCEIROS"),
        ]
        for budget in budgets:
            total = Decimal(budget["valor_total"])
            for code, description, stage, fraction, category_code in budget_parts:
                item_code = f"{code}-{budget['id']:03d}"
                exists = conn.execute(text("SELECT id FROM itens_orcamento WHERE orcamento_base_id=:budget AND codigo=:code"), {"budget": budget["id"], "code": item_code}).scalar_one_or_none()
                if not exists:
                    amount = (total * fraction).quantize(Decimal("0.01"))
                    conn.execute(text("""
                        INSERT INTO itens_orcamento
                        (orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total)
                        VALUES (:budget, :category, :code, :stage, :description, 'vb', 1, :amount, :amount)
                    """), {"budget": budget["id"], "category": category_ids[category_code], "code": item_code, "stage": stage, "description": description, "amount": amount})

        orders = conn.execute(text("SELECT id, fornecedor_id, obra_id, data_emissao, status FROM ordens_compra ORDER BY id LIMIT 12")).mappings().all()
        for order in orders:
            quotation = conn.execute(text("SELECT id FROM cotacoes WHERE fornecedor_id=:supplier AND (obra_id=:work OR obra_id IS NULL) ORDER BY id LIMIT 1"), {"supplier": order["fornecedor_id"], "work": order["obra_id"]}).scalar_one_or_none()
            emission = order["data_emissao"] or today
            conn.execute(text("""
                UPDATE ordens_compra SET cotacao_id=:quotation,
                       data_aprovacao=:approval, data_recebimento=:receipt WHERE id=:id
            """), {"quotation": quotation, "approval": emission + timedelta(days=2),
                    "receipt": emission + timedelta(days=10) if order["status"] == "recebida" else None, "id": order["id"]})

        for i, payable in enumerate(payables, 1):
            description = f"Apropriação de custo {i:02d} — obra {works[(i - 1) % len(works)]['nome']}"
            ensure(
                conn, "apropriacoes_custo", "descricao", description,
                obra_id=works[(i - 1) % len(works)]["id"], centro_custo_id=center_ids[(i - 1) % len(center_ids)],
                categoria_financeira_id=category_ids[expense_codes[(i - 1) % len(expense_codes)]],
                conta_pagar_id=payable["id"], competencia=f"2026-{i:02d}",
                data_apropriacao=date(2026, i, 15), tipo_custo="direto", quantidade=Decimal("1"),
                valor_unitario=payable["valor"], valor_total=payable["valor"], origem="conta_pagar",
            )

        for i in range(1, 13):
            is_income = i % 2 == 1
            ensure(
                conn, "movimentacoes_caixa", "descricao", f"Movimentação financeira histórica {i:02d}/2026",
                conta_bancaria_id=bank_account_ids[(i - 1) % len(bank_account_ids)],
                fatura_id=invoice_ids[(i - 1) % len(invoice_ids)] if is_income else None,
                categoria_financeira_id=category_ids["REC_MEDICOES" if is_income else expense_codes[(i - 1) % len(expense_codes)]],
                centro_custo_id=center_ids[(i - 1) % len(center_ids)], tipo="entrada" if is_income else "saida",
                data_movimentacao=date(2026, i, 20), valor=Decimal("42000.00") + i * Decimal("1750.00"),
                forma_pagamento="transferencia", conciliado=i < 10,
                data_conciliacao=date(2026, i, 21) if i < 10 else None,
            )

        indicators = [
            ("FATURAMENTO", "Faturamento mensal", "reais", Decimal("85000")),
            ("MARGEM_BRUTA", "Margem bruta", "percentual", Decimal("22")),
            ("OBRAS_ATIVAS", "Obras em andamento", "numero", Decimal("6")),
            ("CUSTO_OBRAS", "Custo realizado", "reais", Decimal("65000")),
            ("DISPONIBILIDADE_FROTA", "Disponibilidade da frota", "percentual", Decimal("85")),
            ("QUADRO_ATIVO", "Funcionários ativos", "numero", Decimal("15")),
        ]
        for month in range(1, 13):
            for code, name, unit, base_value in indicators:
                exists = conn.execute(text("SELECT id FROM metas_indicadores WHERE codigo_indicador=:code AND competencia=:competence AND obra_id IS NULL LIMIT 1"), {"code": code, "competence": f"2026-{month:02d}"}).scalar_one_or_none()
                if not exists:
                    conn.execute(text("""
                        INSERT INTO metas_indicadores (codigo_indicador, nome, competencia, valor_meta, unidade, observacao, ativo)
                        VALUES (:code, :name, :competence, :value, :unit, 'Meta corporativa mensal', true)
                    """), {"code": code, "name": name, "competence": f"2026-{month:02d}", "value": base_value * (Decimal("1") + Decimal(month - 1) / Decimal("100")), "unit": unit})

        for i, work in enumerate(works, 1):
            history_description = f"Situação inicial registrada para {work['nome']}"
            ensure(
                conn, "historicos_status", "observacao", history_description,
                entidade="obras", entidade_id=work["id"], status_anterior=None,
                status_novo=work["status"], data_alteracao=date(2026, min(i, 12), 1), usuario_id=1,
            )

        fleet_brands = [("Mercedes-Benz", "Atego"), ("Volkswagen", "Delivery"), ("Caterpillar", "320"), ("JCB", "3CX")]
        for i, fleet in enumerate(fleets, 1):
            brand, model = fleet_brands[(i - 1) % len(fleet_brands)]
            conn.execute(text("""
                UPDATE frotas SET marca=:brand, modelo=:model, ano_fabricacao=:year,
                       data_aquisicao=:acquisition, valor_aquisicao=:value, horimetro_atual=:meter
                WHERE id=:id
            """), {"brand": brand, "model": model, "year": 2018 + i % 7,
                    "acquisition": date(2022, min(i, 12), 10), "value": Decimal("95000") + i * Decimal("18500"),
                    "meter": Decimal("850") + i * Decimal("125"), "id": fleet["id"]})
            work = works[(i - 1) % len(works)]
            employee = employees[(i - 1) % len(employees)]
            supplier_id = suppliers[(i - 1) % len(suppliers)]
            ensure(conn, "manutencoes_frota", "descricao", f"Revisão preventiva de {fleet['identificacao']} — 2026",
                   frota_id=fleet["id"], fornecedor_id=supplier_id, obra_id=work["id"], tipo="preventiva",
                   data_entrada=date(2026, min(i, 12), 8), data_saida=date(2026, min(i, 12), 10),
                   custo=Decimal("850") + i * Decimal("120"), horimetro=Decimal("800") + i * Decimal("125"), status="concluida")
            ensure(conn, "abastecimentos_frota", "observacao", f"Abastecimento mensal de {fleet['identificacao']} — 2026-{i:02d}",
                   frota_id=fleet["id"], obra_id=work["id"], responsavel_id=employee["id"],
                   data_abastecimento=date(2026, i, 12), litros=Decimal("65") + i * Decimal("3"),
                   valor_total=Decimal("390") + i * Decimal("22"), quilometragem_horimetro=Decimal("900") + i * Decimal("120"))
            ensure(conn, "utilizacoes_frota", "observacao", f"Utilização mensal de {fleet['identificacao']} — 2026-{i:02d}",
                   frota_id=fleet["id"], obra_id=work["id"], funcionario_id=employee["id"],
                   data_utilizacao=date(2026, i, 18), horas_utilizadas=Decimal("72") + i * Decimal("4"),
                   horimetro_inicial=Decimal("850") + i * Decimal("100"),
                   horimetro_final=Decimal("922") + i * Decimal("104"), custo_hora=Decimal("95") + i * Decimal("5"))
            ensure(conn, "alocacoes_funcionario_obra", "funcao", f"{employee['cargo'] or 'Colaborador'} — equipe {i:02d}",
                   funcionario_id=employee["id"], obra_id=work["id"], centro_custo_id=center_ids[(i - 1) % len(center_ids)],
                   data_inicio=date(2026, 1, min(i, 28)), data_fim=None,
                   custo_hora=((Decimal(employee["salario_base"] or 0) / Decimal("220")).quantize(Decimal("0.01"))), ativo=True)

        conn.execute(text("UPDATE cronogramas SET peso_percentual=100 WHERE peso_percentual=0"))

        counts = conn.execute(text("""
            SELECT tablename,
                   (xpath('/row/count/text()', query_to_xml(format('SELECT count(*) AS count FROM %I', tablename), false, true, '')))[1]::text::int AS total
            FROM pg_tables WHERE schemaname='public' AND tablename <> 'alembic_version'
            ORDER BY tablename
        """)).all()
        below = [(table, total) for table, total in counts if total < 10]
        if below:
            raise RuntimeError(f"Tabelas com menos de 10 registros após a carga: {below}")
        print("Núcleo financeiro e analítico populado com sucesso.")
        for table, total in counts:
            print(f"{table}|{total}")


if __name__ == "__main__":
    main()
