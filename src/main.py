from fastapi import FastAPI

from src.core.auth.auth_controller import router as auth_router
from src.modules.rh.funcionario.funcionario_controller import router as funcionario_router
from src.modules.comercial.cliente.cliente_controller import router as cliente_router
from src.modules.comercial.contrato.contrato_controller import router as contrato_router
from src.modules.comercial.agenda_visita.agenda_visita_controller import router as agenda_visita_router
from src.modules.engenharia.projeto.projeto_controller import router as projeto_router
from src.modules.engenharia.revisao_projeto.revisao_projeto_controller import router as revisao_projeto_router
from src.modules.obras.obra.obra_controller import router as obra_router
from src.modules.obras.diario_obra.diario_obra_controller import router as diario_obra_router
from src.modules.obras.medicao.medicao_controller import router as medicao_router
from src.modules.obras.chamado_tecnico.chamado_tecnico_controller import router as chamado_tecnico_router
from src.modules.financeiro.orcamento_base.orcamento_base_controller import router as orcamento_base_router
from src.modules.financeiro.conta_pagar.conta_pagar_controller import router as conta_pagar_router
from src.modules.financeiro.conta_receber.conta_receber_controller import router as conta_receber_router
from src.modules.estoque.insumo.insumo_controller import router as insumo_router
from src.modules.estoque.movimentacao_estoque.movimentacao_estoque_controller import router as movimentacao_estoque_router
from src.modules.compras.fornecedor.fornecedor_controller import router as fornecedor_router
from src.modules.compras.cotacao.cotacao_controller import router as cotacao_router
from src.modules.compras.ordem_compra.ordem_compra_controller import router as ordem_compra_router
from src.modules.compras.ordem_compra.item_ordem_compra_controller import router as item_ordem_compra_router
from src.modules.planejamento.frota.frota_controller import router as frota_router
from src.modules.planejamento.cronograma.cronograma_controller import router as cronograma_router
from src.modules.rh.folha_pagamento.folha_pagamento_controller import router as folha_pagamento_router
from src.modules.rh.registro_ponto.registro_ponto_controller import router as registro_ponto_router

app = FastAPI(title="UrbanPrime ERP", version="0.1.0")


@app.get("/health", tags=["Sistema"])
def health_check():
    return {"status": "ok", "service": "UrbanPrime ERP"}


app.include_router(auth_router)
app.include_router(funcionario_router)
app.include_router(cliente_router)
app.include_router(contrato_router)
app.include_router(agenda_visita_router)
app.include_router(projeto_router)
app.include_router(revisao_projeto_router)
app.include_router(obra_router)
app.include_router(diario_obra_router)
app.include_router(medicao_router)
app.include_router(chamado_tecnico_router)
app.include_router(orcamento_base_router)
app.include_router(conta_pagar_router)
app.include_router(conta_receber_router)
app.include_router(insumo_router)
app.include_router(movimentacao_estoque_router)
app.include_router(fornecedor_router)
app.include_router(cotacao_router)
app.include_router(ordem_compra_router)
app.include_router(item_ordem_compra_router)
app.include_router(frota_router)
app.include_router(cronograma_router)
app.include_router(folha_pagamento_router)
app.include_router(registro_ponto_router)
