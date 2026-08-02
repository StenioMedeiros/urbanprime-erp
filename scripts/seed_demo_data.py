"""Carga demonstrativa idempotente para o UrbanPrime ERP."""

from datetime import date, datetime, time, timedelta
from decimal import Decimal
from pathlib import Path
import sys

from sqlalchemy import create_engine, text

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.core.config.settings import get_settings


TARGET = 12

PEOPLE = [
    ("Ana Paula Rodrigues", "ana.rodrigues", "ana.rodrigues@urbanprime.com", "Engenheira civil", "engenharia"),
    ("Bruno Henrique Alves", "bruno.alves", "bruno.alves@urbanprime.com", "Mestre de obras", "obras"),
    ("Camila Ferreira Melo", "camila.melo", "camila.melo@urbanprime.com", "Analista financeira", "financeiro"),
    ("Diego Moura Cavalcanti", "diego.cavalcanti", "diego.cavalcanti@urbanprime.com", "Analista de compras", "compras"),
    ("Edson José da Silva", "edson.silva", "edson.silva@urbanprime.com", "Técnico de segurança", "rh"),
    ("Fernanda Lima Barros", "fernanda.barros", "fernanda.barros@urbanprime.com", "Arquiteta", "engenharia"),
    ("Gabriel Nunes Costa", "gabriel.costa", "gabriel.costa@urbanprime.com", "Encarregado de obras", "obras"),
    ("Helena Maria Souza", "helena.souza", "helena.souza@urbanprime.com", "Assistente administrativa", "administrativo"),
    ("Igor Matheus Ribeiro", "igor.ribeiro", "igor.ribeiro@urbanprime.com", "Almoxarife", "compras"),
    ("Juliana Alves Monteiro", "juliana.monteiro", "juliana.monteiro@urbanprime.com", "Coordenadora de projetos", "engenharia"),
    ("Lucas Vinícius Santos", "lucas.santos", "lucas.santos@urbanprime.com", "Eletricista", "obras"),
    ("Mariana Bezerra Oliveira", "mariana.oliveira", "mariana.oliveira@urbanprime.com", "Analista de RH", "rh"),
]

CLIENTS = [
    "Família Almeida", "Agreste Distribuidora", "Clínica Santa Luzia", "Grupo Sete Colinas",
    "Comercial Rui Barbosa", "Colégio Sementinha", "Residencial Parque das Acácias",
    "Hotel Encantos do Agreste", "Laticínios Serra Branca", "Família Nogueira",
    "Centro Empresarial Heliópolis", "Instituto Educacional Boa Vista",
]

SUPPLIERS = [
    "Casa do Cimento Garanhuns", "Aço Forte do Agreste", "Madeireira Sete Colinas",
    "Elétrica Heliópolis", "Hidrocenter Garanhuns", "Tintas Agreste",
    "Cerâmica Vale do Mundaú", "Locadora Boa Vista", "Ferragens Magano",
    "Concreto Serra Branca", "Vidraçaria São José", "Pernambuco EPI e Ferramentas",
]

MATERIALS = [
    "Cimento CP II 50 kg", "Areia média lavada", "Brita nº 1", "Bloco cerâmico 9x19x19",
    "Vergalhão CA-50 10 mm", "Tijolo de oito furos", "Argamassa AC-II 20 kg",
    "Tinta acrílica premium 18 L", "Cabo elétrico 2,5 mm²", "Tubo PVC soldável 25 mm",
    "Telha cerâmica colonial", "Piso porcelanato acetinado",
]

PROJECTS = [
    ("Residência unifamiliar em Heliópolis", "Construção de residência em Heliópolis", "residencial", "Rua Doutor José Mariano, 120 - Heliópolis"),
    ("Galpão logístico do Distrito Industrial", "Construção de galpão logístico", "industrial", "Distrito Industrial de Garanhuns, lote 18"),
    ("Modernização da Clínica Santa Luzia", "Reforma e ampliação de clínica", "hospitalar", "Avenida Rui Barbosa, 640 - Heliópolis"),
    ("Edifício Residencial Sete Colinas", "Construção do Residencial Sete Colinas", "residencial", "Rua São Vicente, 310 - Centro"),
    ("Centro Comercial Rui Barbosa", "Construção de centro comercial", "comercial", "Avenida Rui Barbosa, 980 - Heliópolis"),
    ("Ampliação do Colégio Sementinha", "Ampliação de escola particular", "educacional", "Rua Melo Peixoto, 85 - Boa Vista"),
    ("Condomínio Parque das Acácias", "Infraestrutura do Parque das Acácias", "residencial", "Avenida Caruaru, 1450 - São José"),
    ("Revitalização do Hotel Encantos", "Reforma do Hotel Encantos do Agreste", "hoteleiro", "Praça Souto Filho, 22 - Centro"),
    ("Unidade Agroindustrial Serra Branca", "Construção de unidade agroindustrial", "industrial", "Rodovia BR-423, km 94 - Zona Rural"),
    ("Casa de campo Vale Verde", "Construção de casa de campo", "residencial", "Sítio Vale Verde - Zona Rural"),
    ("Centro Empresarial Heliópolis", "Construção do Centro Empresarial Heliópolis", "comercial", "Rua Treze de Maio, 455 - Heliópolis"),
    ("Creche Escola Boa Vista", "Construção da Creche Escola Boa Vista", "educacional", "Rua Antônio Cesário, 190 - Boa Vista"),
]


def scalar(conn, sql, **params):
    return conn.execute(text(sql), params).scalar_one()


def ensure(conn, table, key_column, key_value, **values):
    found = conn.execute(
        text(f'SELECT id FROM "{table}" WHERE "{key_column}" = :key_value LIMIT 1'),
        {"key_value": key_value},
    ).scalar_one_or_none()
    if found is not None:
        return found
    payload = {key_column: key_value, **values}
    columns = ", ".join(f'"{column}"' for column in payload)
    placeholders = ", ".join(f':{column}' for column in payload)
    return conn.execute(
        text(f'INSERT INTO "{table}" ({columns}) VALUES ({placeholders}) RETURNING id'),
        payload,
    ).scalar_one()


def localize_legacy_data(conn):
    """Converte a carga antiga 'Demonstração 01' sem criar duplicidades."""
    profile_renames = {
        "gestor_obras_demo": "gestor_obras", "comercial_demo": "comercial",
        "almoxarifado_demo": "almoxarifado", "planejamento_demo": "planejamento",
        "auditoria_demo": "auditoria", "diretoria_demo": "diretoria", "consulta_demo": "consulta",
    }
    for old, new in profile_renames.items():
        conn.execute(text("UPDATE perfis SET nome=:new, descricao=:description WHERE nome=:old"),
                     {"new": new, "old": old, "description": f"Perfil de acesso para {new.replace('_', ' ')}"})
    for i in range(1, TARGET + 1):
        person = PEOPLE[i - 1]
        project_name, work_name, project_type, address = PROJECTS[i - 1]
        conn.execute(text("""
            UPDATE funcionarios SET nome=:name, email_corporativo=:email, cargo=:cargo, setor=:sector
            WHERE email_corporativo=:legacy
        """), {"name": person[0], "email": person[2], "cargo": person[3], "sector": person[4],
                 "legacy": f"demo.funcionario{i:02d}@urbanprime.com"})
        conn.execute(text("""
            UPDATE usuarios SET username=:username, email=:email WHERE username=:legacy
        """), {"username": person[1], "email": person[2], "legacy": f"demo{i:02d}"})
        conn.execute(text("""
            UPDATE clientes SET nome=:name, email=:email, endereco=:address, cidade='Garanhuns', estado='PE', cep=:cep
            WHERE cpf_cnpj=:document
        """), {"name": CLIENTS[i - 1], "email": f"contato.cliente{i:02d}@exemplo.com",
                 "address": f"{address}", "cep": f"5529{i % 10}-0{i:02d}", "document": f"90.000.000/0001-{i:02d}"})
        conn.execute(text("""
            UPDATE fornecedores SET razao_social=:name, nome_fantasia=:name, email=:email,
                   endereco=:address WHERE cnpj=:document
        """), {"name": SUPPLIERS[i - 1], "email": f"vendas{i:02d}@fornecedor-agreste.com",
                 "address": f"Garanhuns - Pernambuco, ponto comercial {i}",
                 "document": f"91.000.000/0001-{i:02d}"})
        conn.execute(text("UPDATE insumos SET nome=:new, descricao=:description WHERE nome=:old"),
                     {"new": MATERIALS[i - 1], "description": f"Material de construção utilizado nas obras de Garanhuns ({MATERIALS[i - 1]}).",
                      "old": f"Insumo Demonstração {i:02d}"})
        conn.execute(text("UPDATE contratos SET numero_contrato=:new, descricao=:description WHERE numero_contrato=:old"),
                     {"new": f"UP-2026-{i:03d}", "description": f"Contrato para {work_name.casefold()}.",
                      "old": f"DEMO-CTR-2026-{i:03d}"})
        conn.execute(text("UPDATE agenda_visitas SET local_visita=:new, observacoes=:description WHERE local_visita=:old"),
                     {"new": address, "description": f"Visita de acompanhamento: {work_name}.",
                      "old": f"Local Demonstração {i:02d}"})
        conn.execute(text("UPDATE projetos SET nome=:new, descricao=:description, tipo_projeto=:kind WHERE nome=:old"),
                     {"new": project_name, "description": f"Projeto executivo para {work_name.casefold()} em Garanhuns.",
                      "kind": project_type, "old": f"Projeto Demonstração {i:02d}"})
        conn.execute(text("""
            UPDATE obras SET nome=:new, descricao=:description, endereco=:address,
                   cidade='Garanhuns', estado='PE', cep=:cep WHERE nome=:old
        """), {"new": work_name, "description": f"{work_name}, localizada em Garanhuns - PE.",
                 "address": address, "cep": f"5529{i % 10}-1{i:02d}", "old": f"Obra Demonstração {i:02d}"})
        replacements = [
            ("diarios_obra", "atividades", f"Atividades demonstrativas do diário {i:02d}", f"Execução e acompanhamento dos serviços de {work_name.casefold()}"),
            ("chamados_tecnicos", "titulo", f"Chamado Demonstração {i:02d}", f"Verificação técnica — {work_name}"),
            ("orcamentos_base", "descricao", f"Orçamento-base demonstrativo {i:02d}", f"Orçamento-base — {work_name}"),
            ("movimentacoes_estoque", "observacao", f"Movimentação demonstrativa {i:02d}", f"Movimentação para {work_name}"),
            ("cotacoes", "descricao", f"Cotação demonstrativa {i:02d}", f"Cotação de materiais — {work_name}"),
            ("itens_ordem_compra", "descricao", f"Item demonstrativo da ordem {i:02d}", MATERIALS[i - 1]),
            ("cronogramas", "atividade", f"Atividade demonstrativa {i:02d}", f"Etapa {i:02d} — {work_name}"),
            ("registro_ponto", "observacao", f"Registro de ponto demonstrativo {i:02d}", f"Jornada na equipe de {work_name}"),
            ("contas_pagar", "descricao", f"Conta a pagar demonstrativa {i:02d}", f"Pagamento de materiais — {work_name}"),
            ("contas_receber", "descricao", f"Conta a receber demonstrativa {i:02d}", f"Parcela de medição — {work_name}"),
            ("logs_auditoria", "descricao", f"Registro demonstrativo de auditoria {i:02d}", f"Atualização de cadastro por {person[0]}"),
        ]
        for table, column, old, new in replacements:
            conn.execute(text(f'UPDATE "{table}" SET "{column}"=:new WHERE "{column}"=:old'), {"new": new, "old": old})
        conn.execute(text("UPDATE logs_auditoria SET entidade='cadastro' WHERE entidade='dados_demo'"))
        conn.execute(text("UPDATE ordens_compra SET numero=:new WHERE numero=:old"),
                     {"new": f"OC-2026-{i:03d}", "old": f"DEMO-OC-2026-{i:03d}"})
        conn.execute(text("UPDATE frotas SET identificacao=:new WHERE identificacao=:old"),
                     {"new": f"FROTA-UP-{i:02d}", "old": f"VEÍCULO-DEMO-{i:02d}"})


def main():
    engine = create_engine(get_settings().database_url, pool_pre_ping=True)
    today = date.today()
    now = datetime.now()

    with engine.begin() as conn:
        admin_hash = scalar(conn, "SELECT senha_hash FROM usuarios ORDER BY id LIMIT 1")
        localize_legacy_data(conn)

        profile_names = [
            "administrador", "financeiro", "engenharia", "compras", "rh",
            "gestor_obras", "comercial", "almoxarifado",
            "planejamento", "auditoria", "diretoria", "consulta",
        ]
        profile_ids = []
        for i, name in enumerate(profile_names, 1):
            profile_ids.append(ensure(
                conn, "perfis", "nome", name,
                descricao=f"Perfil de acesso para {name.replace('_', ' ')}",
                nivel_acesso=min(100, 10 + i * 7), ativo=True,
            ))

        employee_ids, user_ids = [], []
        for i in range(1, TARGET + 1):
            person = PEOPLE[i - 1]
            employee_id = ensure(
                conn, "funcionarios", "email_corporativo", person[2],
                nome=person[0], cpf=f"90000000{i:03d}",
                rg=f"DEMORG{i:05d}", data_nascimento=date(1982 + i, (i % 12) + 1, min(i + 5, 28)),
                telefone=f"(87) 99000-{i:04d}", cargo=person[3],
                setor=person[4], data_admissao=date(2022, (i % 12) + 1, 1),
                salario_base=Decimal("3500.00") + i * 425, status="ativo",
            )
            employee_ids.append(employee_id)
            user_id = ensure(
                conn, "usuarios", "username", person[1],
                funcionario_id=employee_id, email=person[2],
                senha_hash=admin_hash, ativo=True, bloqueado=False, tentativas_login=0,
                ultimo_login=now - timedelta(days=i), data_criacao=now - timedelta(days=120 + i),
            )
            user_ids.append(user_id)
            if not conn.execute(text(
                "SELECT 1 FROM usuario_perfil WHERE usuario_id=:u AND perfil_id=:p"
            ), {"u": user_id, "p": profile_ids[i % len(profile_ids)]}).first():
                conn.execute(text(
                    "INSERT INTO usuario_perfil (usuario_id, perfil_id) VALUES (:u, :p)"
                ), {"u": user_id, "p": profile_ids[i % len(profile_ids)]})
            ensure(conn, "sessoes_usuario", "token_sessao_hash", f"demo-session-hash-{i:02d}",
                   usuario_id=user_id, ip_origem=f"192.0.2.{i}", user_agent="UrbanPrime Demo Browser",
                   data_login=now - timedelta(hours=i), data_expiracao=now + timedelta(days=7), ativo=i % 4 != 0)
            ensure(conn, "tokens_refresh", "token_hash", f"demo-refresh-hash-{i:02d}",
                   usuario_id=user_id, data_criacao=now - timedelta(hours=i),
                   data_expiracao=now + timedelta(days=30), revogado=i % 5 == 0,
                   ip_origem=f"192.0.2.{i}", user_agent="UrbanPrime Demo Browser")
            ensure(conn, "logs_auditoria", "descricao", f"Atualização de cadastro por {person[0]}",
                   usuario_id=user_id, modulo=person[4],
                   acao=["visualizar", "criar", "editar"][(i - 1) % 3], entidade="cadastro",
                   entidade_id=i, nivel="info", ip_origem=f"192.0.2.{i}",
                   user_agent="UrbanPrime Demo Browser")

        client_ids, supplier_ids, input_ids = [], [], []
        for i in range(1, TARGET + 1):
            client_ids.append(ensure(
                conn, "clientes", "cpf_cnpj", f"90.000.000/0001-{i:02d}",
                nome=CLIENTS[i - 1], tipo_pessoa="juridica",
                email=f"contato.cliente{i:02d}@exemplo.com", telefone=f"(87) 3100-{i:04d}",
                endereco=PROJECTS[i - 1][3], cidade="Garanhuns", estado="PE",
                cep=f"5529{i % 10}-0{i:02d}", status="ativo" if i % 4 else "inativo",
            ))
            supplier_ids.append(ensure(
                conn, "fornecedores", "cnpj", f"91.000.000/0001-{i:02d}",
                razao_social=SUPPLIERS[i - 1], nome_fantasia=SUPPLIERS[i - 1],
                email=f"vendas{i:02d}@fornecedor-agreste.com",
                telefone=f"(87) 3200-{i:04d}", endereco=f"Garanhuns - Pernambuco, ponto comercial {i}", status="ativo",
            ))
            input_ids.append(ensure(
                conn, "insumos", "nome", MATERIALS[i - 1],
                descricao=f"Material de construção utilizado nas obras de Garanhuns ({MATERIALS[i - 1]}).",
                unidade_medida=["un", "kg", "m", "m²"][(i - 1) % 4],
                quantidade_atual=Decimal("100.000") + i * 15,
                estoque_minimo=Decimal("20.000") + i, valor_unitario=Decimal("12.50") * i,
                status="ativo",
            ))

        contract_ids, project_ids, work_ids = [], [], []
        measurement_ids, order_ids = [], []
        for i in range(1, TARGET + 1):
            employee_id, client_id = employee_ids[i - 1], client_ids[i - 1]
            project_name, work_name, project_type, address = PROJECTS[i - 1]
            contract_id = ensure(
                conn, "contratos", "numero_contrato", f"UP-2026-{i:03d}",
                cliente_id=client_id, descricao=f"Contrato para {work_name.casefold()}.",
                valor_total=Decimal("450000.00") + i * 37500,
                data_assinatura=today - timedelta(days=180 - i),
                data_inicio=today - timedelta(days=120 - i), data_fim=today + timedelta(days=300 + i * 10),
                status=["ativo", "em_aberto", "concluido"][(i - 1) % 3],
            )
            contract_ids.append(contract_id)
            ensure(conn, "agenda_visitas", "local_visita", address,
                   cliente_id=client_id, funcionario_id=employee_id,
                   data_visita=today + timedelta(days=i), horario=time(9 + (i % 7), 0),
                   observacoes=f"Visita de acompanhamento: {work_name}.",
                   status=["agendada", "realizada", "cancelada"][(i - 1) % 3])
            project_id = ensure(
                conn, "projetos", "nome", project_name,
                contrato_id=contract_id, responsavel_id=employee_id,
                descricao=f"Projeto executivo para {work_name.casefold()} em Garanhuns.", tipo_projeto=project_type,
                data_inicio=today - timedelta(days=90), data_previsao_entrega=today + timedelta(days=120 + i),
                status=["em_elaboracao", "em_revisao", "aprovado"][(i - 1) % 3],
            )
            project_ids.append(project_id)
            ensure(conn, "revisoes_projeto", "arquivo_revisao", f"demo/revisao-{i:02d}.pdf",
                   projeto_id=project_id, responsavel_id=employee_id, numero_revisao=i,
                   descricao=f"Revisão {i} — {project_name}", motivo="Compatibilização de disciplinas",
                   data_revisao=today - timedelta(days=i), aprovado=i % 3 != 0)
            work_id = ensure(
                conn, "obras", "nome", work_name,
                contrato_id=contract_id, projeto_id=project_id,
                descricao=f"{work_name}, localizada em Garanhuns - PE.", endereco=address,
                cidade="Garanhuns", estado="PE", cep=f"5529{i % 10}-1{i:02d}", responsavel_id=employee_id,
                data_inicio=today - timedelta(days=60 + i), data_previsao_fim=today + timedelta(days=240 + i),
                status=["planejada", "em_andamento", "concluida"][(i - 1) % 3],
            )
            work_ids.append(work_id)
            ensure(conn, "diarios_obra", "atividades", f"Execução e acompanhamento dos serviços de {work_name.casefold()}",
                   obra_id=work_id, funcionario_id=employee_id, data_registro=today - timedelta(days=i),
                   clima=["ensolarado", "nublado", "chuvoso"][(i - 1) % 3],
                   ocorrencias="Operação normal, sem ocorrências críticas")
            measurement_id = ensure(
                conn, "medicoes", "competencia", f"2026-{i:02d}",
                obra_id=work_id, contrato_id=contract_id, valor_medido=Decimal("35000.00") + i * 2750,
                data_medicao=today - timedelta(days=i * 3),
                status=["pendente", "aprovada", "faturada"][(i - 1) % 3],
            )
            measurement_ids.append(measurement_id)
            ensure(conn, "chamados_tecnicos", "titulo", f"Verificação técnica — {work_name}",
                   obra_id=work_id, solicitante_id=employee_id,
                   descricao=f"Avaliar serviço pendente em {work_name.casefold()}.",
                   prioridade=["baixa", "media", "alta", "critica"][(i - 1) % 4],
                   status=["aberto", "em_atendimento", "resolvido"][(i - 1) % 3])
            ensure(conn, "orcamentos_base", "descricao", f"Orçamento-base — {work_name}",
                   obra_id=work_id, versao=1, valor_total=Decimal("400000.00") + i * 30000,
                   data_aprovacao=today - timedelta(days=70), aprovado_por_id=employee_id,
                   status="vigente")
            ensure(conn, "movimentacoes_estoque", "observacao", f"Movimentação para {work_name}",
                   insumo_id=input_ids[i - 1], obra_id=work_id,
                   tipo="entrada" if i % 2 else "saida", quantidade=Decimal("5.000") + i,
                   data_movimentacao=today - timedelta(days=i))
            ensure(conn, "cotacoes", "descricao", f"Cotação de materiais — {work_name}",
                   fornecedor_id=supplier_ids[i - 1], obra_id=work_id,
                   valor_total=Decimal("8000.00") + i * 700, data_cotacao=today - timedelta(days=i * 2),
                   status=["aberta", "aprovada", "recusada"][(i - 1) % 3])
            order_id = ensure(
                conn, "ordens_compra", "numero", f"OC-2026-{i:03d}",
                fornecedor_id=supplier_ids[i - 1], obra_id=work_id,
                data_emissao=today - timedelta(days=i), valor_total=Decimal("5000.00") + i * 650,
                status=["aberta", "aprovada", "recebida"][(i - 1) % 3],
            )
            order_ids.append(order_id)
            ensure(conn, "itens_ordem_compra", "descricao", MATERIALS[i - 1],
                   ordem_compra_id=order_id, insumo_id=input_ids[i - 1], quantidade=Decimal("10.000") + i,
                   valor_unitario=Decimal("25.00") + i,
                   valor_total=(Decimal("10.000") + i) * (Decimal("25.00") + i))
            ensure(conn, "frotas", "identificacao", f"FROTA-UP-{i:02d}",
                   tipo=["caminhão", "utilitário", "escavadeira"][(i - 1) % 3],
                   placa=f"DMO{i:01d}A{i:02d}", status="em_uso" if i % 2 else "disponivel", obra_id=work_id)
            ensure(conn, "cronogramas", "atividade", f"Etapa {i:02d} — {work_name}",
                   obra_id=work_id, data_inicio=today - timedelta(days=15),
                   data_fim=today + timedelta(days=15 + i), percentual_concluido=Decimal(str((i * 8) % 101)),
                   status=["planejado", "em_andamento", "concluido"][(i - 1) % 3])
            ensure(conn, "folha_pagamento", "competencia", f"2025-{i:02d}",
                   funcionario_id=employee_id, salario_bruto=Decimal("4500.00") + i * 300,
                   descontos=Decimal("350.00") + i * 20,
                   salario_liquido=Decimal("4150.00") + i * 280,
                   status="pago" if i < 11 else "aberta")
            ensure(conn, "registro_ponto", "observacao", f"Jornada na equipe de {work_name}",
                   funcionario_id=employee_id, data=today - timedelta(days=i), entrada=time(8, 0),
                   saida_intervalo=time(12, 0), retorno_intervalo=time(13, 0), saida=time(17, 0))

        for i in range(1, TARGET + 1):
            ensure(conn, "contas_pagar", "descricao", f"Pagamento de materiais — {PROJECTS[i - 1][1]}",
                   fornecedor_id=supplier_ids[i - 1], ordem_compra_id=order_ids[i - 1],
                   obra_id=work_ids[i - 1], valor=Decimal("5000.00") + i * 650,
                   data_vencimento=today + timedelta(days=i * 3),
                   data_pagamento=today - timedelta(days=i) if i % 3 == 0 else None,
                   status="pago" if i % 3 == 0 else "em_aberto")
            ensure(conn, "contas_receber", "descricao", f"Parcela de medição — {PROJECTS[i - 1][1]}",
                   cliente_id=client_ids[i - 1], contrato_id=contract_ids[i - 1],
                   medicao_id=measurement_ids[i - 1], valor=Decimal("35000.00") + i * 2750,
                   data_vencimento=today + timedelta(days=i * 4),
                   data_recebimento=today - timedelta(days=i) if i % 4 == 0 else None,
                   status="recebido" if i % 4 == 0 else "em_aberto")

        counts = conn.execute(text("""
            SELECT tablename,
                   (xpath('/row/count/text()', query_to_xml(format('SELECT count(*) AS count FROM %I', tablename), false, true, '')))[1]::text::int AS total
            FROM pg_tables WHERE schemaname='public' AND tablename <> 'alembic_version'
            ORDER BY tablename
        """)).all()
        below = [(name, count) for name, count in counts if count < 10]
        if below:
            raise RuntimeError(f"Tabelas abaixo de 10 registros: {below}")
        print("Carga demonstrativa concluída.")
        for name, count in counts:
            print(f"{name}|{count}")


if __name__ == "__main__":
    main()
