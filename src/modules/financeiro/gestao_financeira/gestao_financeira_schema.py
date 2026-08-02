from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, create_model


def make_update(name: str, base: type[BaseModel]):
    fields = {
        field_name: (field.annotation | None, None)
        for field_name, field in base.model_fields.items()
    }
    return create_model(name, __base__=BaseModel, **fields)


def make_read(name: str, base: type[BaseModel]):
    model = create_model(
        name,
        __base__=base,
        id=(int, ...),
        created_at=(datetime | None, None),
        updated_at=(datetime | None, None),
    )
    model.model_config = ConfigDict(from_attributes=True)
    model.model_rebuild(force=True)
    return model


class CategoriaFinanceiraBase(BaseModel):
    codigo: str
    nome: str
    tipo: str
    categoria_pai_id: int | None = None
    descricao: str | None = None
    contabilizavel: bool = True
    ativo: bool = True


class CategoriaFinanceiraCreate(CategoriaFinanceiraBase):
    pass


CategoriaFinanceiraUpdate = make_update("CategoriaFinanceiraUpdate", CategoriaFinanceiraBase)
CategoriaFinanceiraRead = make_read("CategoriaFinanceiraRead", CategoriaFinanceiraBase)


class CentroCustoBase(BaseModel):
    codigo: str
    nome: str
    tipo: str = "obra"
    obra_id: int | None = None
    responsavel_id: int | None = None
    descricao: str | None = None
    ativo: bool = True


class CentroCustoCreate(CentroCustoBase):
    pass


CentroCustoUpdate = make_update("CentroCustoUpdate", CentroCustoBase)
CentroCustoRead = make_read("CentroCustoRead", CentroCustoBase)


class ContaBancariaBase(BaseModel):
    banco: str
    agencia: str | None = None
    numero_conta: str
    tipo_conta: str = "corrente"
    descricao: str | None = None
    saldo_inicial: Decimal = Decimal("0")
    data_saldo_inicial: date
    ativo: bool = True


class ContaBancariaCreate(ContaBancariaBase):
    pass


ContaBancariaUpdate = make_update("ContaBancariaUpdate", ContaBancariaBase)
ContaBancariaRead = make_read("ContaBancariaRead", ContaBancariaBase)


class FaturaBase(BaseModel):
    cliente_id: int
    contrato_id: int | None = None
    obra_id: int | None = None
    medicao_id: int | None = None
    numero_documento: str
    data_emissao: date
    competencia: str
    valor_bruto: Decimal
    impostos: Decimal = Decimal("0")
    retencoes: Decimal = Decimal("0")
    valor_liquido: Decimal
    data_vencimento: date
    status: str = "emitida"
    observacao: str | None = None


class FaturaCreate(FaturaBase):
    pass


FaturaUpdate = make_update("FaturaUpdate", FaturaBase)
FaturaRead = make_read("FaturaRead", FaturaBase)


class MovimentacaoCaixaBase(BaseModel):
    conta_bancaria_id: int
    conta_pagar_id: int | None = None
    conta_receber_id: int | None = None
    fatura_id: int | None = None
    categoria_financeira_id: int
    centro_custo_id: int | None = None
    tipo: str
    data_movimentacao: date
    valor: Decimal
    descricao: str
    forma_pagamento: str | None = None
    conciliado: bool = False
    data_conciliacao: date | None = None


class MovimentacaoCaixaCreate(MovimentacaoCaixaBase):
    pass


MovimentacaoCaixaUpdate = make_update("MovimentacaoCaixaUpdate", MovimentacaoCaixaBase)
MovimentacaoCaixaRead = make_read("MovimentacaoCaixaRead", MovimentacaoCaixaBase)


class ItemOrcamentoBase(BaseModel):
    orcamento_base_id: int
    categoria_financeira_id: int | None = None
    codigo: str
    etapa: str | None = None
    descricao: str
    unidade_medida: str = "un"
    quantidade: Decimal = Decimal("1")
    valor_unitario: Decimal = Decimal("0")
    valor_total: Decimal = Decimal("0")


class ItemOrcamentoCreate(ItemOrcamentoBase):
    pass


ItemOrcamentoUpdate = make_update("ItemOrcamentoUpdate", ItemOrcamentoBase)
ItemOrcamentoRead = make_read("ItemOrcamentoRead", ItemOrcamentoBase)


class ApropriacaoCustoBase(BaseModel):
    obra_id: int
    centro_custo_id: int | None = None
    categoria_financeira_id: int
    conta_pagar_id: int | None = None
    ordem_compra_id: int | None = None
    funcionario_id: int | None = None
    frota_id: int | None = None
    competencia: str
    data_apropriacao: date
    tipo_custo: str
    descricao: str
    quantidade: Decimal = Decimal("1")
    valor_unitario: Decimal = Decimal("0")
    valor_total: Decimal
    origem: str = "manual"


class ApropriacaoCustoCreate(ApropriacaoCustoBase):
    pass


ApropriacaoCustoUpdate = make_update("ApropriacaoCustoUpdate", ApropriacaoCustoBase)
ApropriacaoCustoRead = make_read("ApropriacaoCustoRead", ApropriacaoCustoBase)


class MetaIndicadorBase(BaseModel):
    codigo_indicador: str
    nome: str
    competencia: str
    valor_meta: Decimal
    unidade: str = "numero"
    centro_custo_id: int | None = None
    obra_id: int | None = None
    observacao: str | None = None
    ativo: bool = True


class MetaIndicadorCreate(MetaIndicadorBase):
    pass


MetaIndicadorUpdate = make_update("MetaIndicadorUpdate", MetaIndicadorBase)
MetaIndicadorRead = make_read("MetaIndicadorRead", MetaIndicadorBase)


class HistoricoStatusBase(BaseModel):
    entidade: str
    entidade_id: int
    status_anterior: str | None = None
    status_novo: str
    data_alteracao: datetime
    usuario_id: int | None = None
    observacao: str | None = None


class HistoricoStatusCreate(HistoricoStatusBase):
    pass


HistoricoStatusUpdate = make_update("HistoricoStatusUpdate", HistoricoStatusBase)
HistoricoStatusRead = make_read("HistoricoStatusRead", HistoricoStatusBase)


class ManutencaoFrotaBase(BaseModel):
    frota_id: int
    fornecedor_id: int | None = None
    obra_id: int | None = None
    tipo: str
    descricao: str
    data_entrada: date
    data_saida: date | None = None
    custo: Decimal = Decimal("0")
    horimetro: Decimal | None = None
    status: str = "aberta"


class ManutencaoFrotaCreate(ManutencaoFrotaBase):
    pass


ManutencaoFrotaUpdate = make_update("ManutencaoFrotaUpdate", ManutencaoFrotaBase)
ManutencaoFrotaRead = make_read("ManutencaoFrotaRead", ManutencaoFrotaBase)


class AbastecimentoFrotaBase(BaseModel):
    frota_id: int
    obra_id: int | None = None
    responsavel_id: int | None = None
    data_abastecimento: date
    litros: Decimal
    valor_total: Decimal
    quilometragem_horimetro: Decimal | None = None
    observacao: str | None = None


class AbastecimentoFrotaCreate(AbastecimentoFrotaBase):
    pass


AbastecimentoFrotaUpdate = make_update("AbastecimentoFrotaUpdate", AbastecimentoFrotaBase)
AbastecimentoFrotaRead = make_read("AbastecimentoFrotaRead", AbastecimentoFrotaBase)


class UtilizacaoFrotaBase(BaseModel):
    frota_id: int
    obra_id: int | None = None
    funcionario_id: int | None = None
    data_utilizacao: date
    horas_utilizadas: Decimal
    horimetro_inicial: Decimal | None = None
    horimetro_final: Decimal | None = None
    custo_hora: Decimal = Decimal("0")
    observacao: str | None = None


class UtilizacaoFrotaCreate(UtilizacaoFrotaBase):
    pass


UtilizacaoFrotaUpdate = make_update("UtilizacaoFrotaUpdate", UtilizacaoFrotaBase)
UtilizacaoFrotaRead = make_read("UtilizacaoFrotaRead", UtilizacaoFrotaBase)


class AlocacaoFuncionarioObraBase(BaseModel):
    funcionario_id: int
    obra_id: int
    centro_custo_id: int | None = None
    funcao: str | None = None
    data_inicio: date
    data_fim: date | None = None
    custo_hora: Decimal = Decimal("0")
    ativo: bool = True


class AlocacaoFuncionarioObraCreate(AlocacaoFuncionarioObraBase):
    pass


AlocacaoFuncionarioObraUpdate = make_update("AlocacaoFuncionarioObraUpdate", AlocacaoFuncionarioObraBase)
AlocacaoFuncionarioObraRead = make_read("AlocacaoFuncionarioObraRead", AlocacaoFuncionarioObraBase)
