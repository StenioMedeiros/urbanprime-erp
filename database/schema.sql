--
-- PostgreSQL database dump
--

\restrict EBxyVRYnVuMR1mAi3mH5zzSadkvsKrfPJmhhUg9yytaBdE1oSPlWDr5rnpIz45h

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: abastecimentos_frota; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.abastecimentos_frota (
    id integer NOT NULL,
    frota_id integer NOT NULL,
    obra_id integer,
    responsavel_id integer,
    data_abastecimento date NOT NULL,
    litros numeric(14,3) NOT NULL,
    valor_total numeric(16,2) NOT NULL,
    quilometragem_horimetro numeric(14,2),
    observacao text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_abastecimento_valores CHECK (((litros > (0)::numeric) AND (valor_total >= (0)::numeric)))
);


--
-- Name: abastecimentos_frota_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.abastecimentos_frota_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: abastecimentos_frota_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.abastecimentos_frota_id_seq OWNED BY public.abastecimentos_frota.id;


--
-- Name: agenda_visitas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.agenda_visitas (
    id integer NOT NULL,
    cliente_id integer NOT NULL,
    funcionario_id integer,
    data_visita date NOT NULL,
    horario time without time zone,
    local_visita character varying(180),
    observacoes text,
    status character varying(30) DEFAULT 'agendada'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: agenda_visitas_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.agenda_visitas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: agenda_visitas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.agenda_visitas_id_seq OWNED BY public.agenda_visitas.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- Name: alocacoes_funcionario_obra; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alocacoes_funcionario_obra (
    id integer NOT NULL,
    funcionario_id integer NOT NULL,
    obra_id integer NOT NULL,
    centro_custo_id integer,
    funcao character varying(120),
    data_inicio date NOT NULL,
    data_fim date,
    custo_hora numeric(14,2) DEFAULT '0'::numeric NOT NULL,
    ativo boolean DEFAULT true NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_alocacao_custo_hora CHECK ((custo_hora >= (0)::numeric))
);


--
-- Name: alocacoes_funcionario_obra_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.alocacoes_funcionario_obra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: alocacoes_funcionario_obra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.alocacoes_funcionario_obra_id_seq OWNED BY public.alocacoes_funcionario_obra.id;


--
-- Name: apropriacoes_custo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.apropriacoes_custo (
    id integer NOT NULL,
    obra_id integer NOT NULL,
    centro_custo_id integer,
    categoria_financeira_id integer NOT NULL,
    conta_pagar_id integer,
    ordem_compra_id integer,
    funcionario_id integer,
    frota_id integer,
    competencia character varying(7) NOT NULL,
    data_apropriacao date NOT NULL,
    tipo_custo character varying(30) NOT NULL,
    descricao character varying(200) NOT NULL,
    quantidade numeric(16,3) DEFAULT '1'::numeric NOT NULL,
    valor_unitario numeric(16,2) DEFAULT '0'::numeric NOT NULL,
    valor_total numeric(16,2) NOT NULL,
    origem character varying(40) DEFAULT 'manual'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_apropriacao_valores CHECK (((quantidade >= (0)::numeric) AND (valor_unitario >= (0)::numeric) AND (valor_total >= (0)::numeric)))
);


--
-- Name: apropriacoes_custo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.apropriacoes_custo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: apropriacoes_custo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.apropriacoes_custo_id_seq OWNED BY public.apropriacoes_custo.id;


--
-- Name: categorias_financeiras; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.categorias_financeiras (
    id integer NOT NULL,
    codigo character varying(30) NOT NULL,
    nome character varying(120) NOT NULL,
    tipo character varying(20) NOT NULL,
    categoria_pai_id integer,
    descricao text,
    contabilizavel boolean DEFAULT true NOT NULL,
    ativo boolean DEFAULT true NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_categoria_financeira_tipo CHECK (((tipo)::text = ANY ((ARRAY['receita'::character varying, 'despesa'::character varying, 'ambos'::character varying])::text[])))
);


--
-- Name: categorias_financeiras_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.categorias_financeiras_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: categorias_financeiras_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.categorias_financeiras_id_seq OWNED BY public.categorias_financeiras.id;


--
-- Name: centros_custo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.centros_custo (
    id integer NOT NULL,
    codigo character varying(30) NOT NULL,
    nome character varying(140) NOT NULL,
    tipo character varying(30) DEFAULT 'obra'::character varying NOT NULL,
    obra_id integer,
    responsavel_id integer,
    descricao text,
    ativo boolean DEFAULT true NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: centros_custo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.centros_custo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: centros_custo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.centros_custo_id_seq OWNED BY public.centros_custo.id;


--
-- Name: chamados_tecnicos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.chamados_tecnicos (
    id integer NOT NULL,
    obra_id integer NOT NULL,
    solicitante_id integer,
    titulo character varying(160) NOT NULL,
    descricao text,
    prioridade character varying(30) DEFAULT 'media'::character varying NOT NULL,
    status character varying(30) DEFAULT 'aberto'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: chamados_tecnicos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.chamados_tecnicos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: chamados_tecnicos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.chamados_tecnicos_id_seq OWNED BY public.chamados_tecnicos.id;


--
-- Name: clientes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.clientes (
    id integer NOT NULL,
    nome character varying(160) NOT NULL,
    tipo_pessoa character varying(20) DEFAULT 'juridica'::character varying NOT NULL,
    cpf_cnpj character varying(20),
    email character varying(180),
    telefone character varying(30),
    endereco text,
    cidade character varying(100),
    estado character varying(2),
    cep character varying(12),
    status character varying(30) DEFAULT 'ativo'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.clientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: clientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.clientes_id_seq OWNED BY public.clientes.id;


--
-- Name: contas_bancarias; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.contas_bancarias (
    id integer NOT NULL,
    banco character varying(120) NOT NULL,
    agencia character varying(30),
    numero_conta character varying(40) NOT NULL,
    tipo_conta character varying(30) DEFAULT 'corrente'::character varying NOT NULL,
    descricao character varying(160),
    saldo_inicial numeric(16,2) DEFAULT '0'::numeric NOT NULL,
    data_saldo_inicial date NOT NULL,
    ativo boolean DEFAULT true NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: contas_bancarias_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.contas_bancarias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: contas_bancarias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.contas_bancarias_id_seq OWNED BY public.contas_bancarias.id;


--
-- Name: contas_pagar; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.contas_pagar (
    id integer NOT NULL,
    fornecedor_id integer,
    ordem_compra_id integer,
    obra_id integer,
    descricao character varying(180) NOT NULL,
    valor numeric(14,2) NOT NULL,
    data_vencimento date NOT NULL,
    data_pagamento date,
    status character varying(30) DEFAULT 'em_aberto'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    categoria_financeira_id integer,
    centro_custo_id integer,
    data_competencia date,
    numero_documento character varying(60)
);


--
-- Name: contas_pagar_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.contas_pagar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: contas_pagar_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.contas_pagar_id_seq OWNED BY public.contas_pagar.id;


--
-- Name: contas_receber; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.contas_receber (
    id integer NOT NULL,
    cliente_id integer,
    contrato_id integer,
    medicao_id integer,
    descricao character varying(180) NOT NULL,
    valor numeric(14,2) NOT NULL,
    data_vencimento date NOT NULL,
    data_recebimento date,
    status character varying(30) DEFAULT 'em_aberto'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    categoria_financeira_id integer,
    centro_custo_id integer,
    fatura_id integer,
    data_competencia date,
    numero_documento character varying(60)
);


--
-- Name: contas_receber_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.contas_receber_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: contas_receber_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.contas_receber_id_seq OWNED BY public.contas_receber.id;


--
-- Name: contratos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.contratos (
    id integer NOT NULL,
    cliente_id integer NOT NULL,
    numero_contrato character varying(60) NOT NULL,
    descricao text,
    valor_total numeric(14,2) NOT NULL,
    data_assinatura date,
    data_inicio date,
    data_fim date,
    status character varying(30) DEFAULT 'ativo'::character varying NOT NULL,
    arquivo_contrato character varying(255),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: contratos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.contratos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: contratos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.contratos_id_seq OWNED BY public.contratos.id;


--
-- Name: cotacoes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cotacoes (
    id integer NOT NULL,
    fornecedor_id integer NOT NULL,
    obra_id integer,
    descricao text,
    valor_total numeric(14,2),
    data_cotacao date,
    status character varying(30) DEFAULT 'aberta'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: cotacoes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cotacoes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cotacoes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cotacoes_id_seq OWNED BY public.cotacoes.id;


--
-- Name: cronogramas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.cronogramas (
    id integer NOT NULL,
    obra_id integer NOT NULL,
    atividade character varying(180) NOT NULL,
    data_inicio date,
    data_fim date,
    percentual_concluido numeric(5,2) DEFAULT 0 NOT NULL,
    status character varying(30) DEFAULT 'planejado'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    peso_percentual numeric(5,2) DEFAULT '0'::numeric NOT NULL,
    CONSTRAINT ck_cronograma_peso CHECK (((peso_percentual >= (0)::numeric) AND (peso_percentual <= (100)::numeric)))
);


--
-- Name: cronogramas_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.cronogramas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: cronogramas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.cronogramas_id_seq OWNED BY public.cronogramas.id;


--
-- Name: diarios_obra; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.diarios_obra (
    id integer NOT NULL,
    obra_id integer NOT NULL,
    funcionario_id integer,
    data_registro date NOT NULL,
    clima character varying(80),
    atividades text,
    ocorrencias text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: diarios_obra_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.diarios_obra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: diarios_obra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.diarios_obra_id_seq OWNED BY public.diarios_obra.id;


--
-- Name: faturas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.faturas (
    id integer NOT NULL,
    cliente_id integer NOT NULL,
    contrato_id integer,
    obra_id integer,
    medicao_id integer,
    numero_documento character varying(60) NOT NULL,
    data_emissao date NOT NULL,
    competencia character varying(7) NOT NULL,
    valor_bruto numeric(16,2) NOT NULL,
    impostos numeric(16,2) DEFAULT '0'::numeric NOT NULL,
    retencoes numeric(16,2) DEFAULT '0'::numeric NOT NULL,
    valor_liquido numeric(16,2) NOT NULL,
    data_vencimento date NOT NULL,
    status character varying(30) DEFAULT 'emitida'::character varying NOT NULL,
    observacao text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_fatura_valores CHECK (((valor_bruto >= (0)::numeric) AND (impostos >= (0)::numeric) AND (retencoes >= (0)::numeric) AND (valor_liquido >= (0)::numeric)))
);


--
-- Name: faturas_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.faturas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: faturas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.faturas_id_seq OWNED BY public.faturas.id;


--
-- Name: folha_pagamento; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.folha_pagamento (
    id integer NOT NULL,
    funcionario_id integer NOT NULL,
    competencia character varying(7) NOT NULL,
    salario_bruto numeric(14,2) NOT NULL,
    descontos numeric(14,2) DEFAULT 0 NOT NULL,
    salario_liquido numeric(14,2) NOT NULL,
    status character varying(30) DEFAULT 'aberta'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: folha_pagamento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.folha_pagamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: folha_pagamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.folha_pagamento_id_seq OWNED BY public.folha_pagamento.id;


--
-- Name: fornecedores; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.fornecedores (
    id integer NOT NULL,
    razao_social character varying(180) NOT NULL,
    nome_fantasia character varying(180),
    cnpj character varying(20),
    email character varying(180),
    telefone character varying(30),
    endereco text,
    status character varying(30) DEFAULT 'ativo'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: fornecedores_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.fornecedores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: fornecedores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.fornecedores_id_seq OWNED BY public.fornecedores.id;


--
-- Name: frotas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.frotas (
    id integer NOT NULL,
    identificacao character varying(120) NOT NULL,
    tipo character varying(80),
    placa character varying(12),
    status character varying(30) DEFAULT 'disponivel'::character varying NOT NULL,
    obra_id integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    marca character varying(80),
    modelo character varying(100),
    ano_fabricacao integer,
    data_aquisicao date,
    valor_aquisicao numeric(16,2),
    horimetro_atual numeric(14,2)
);


--
-- Name: frotas_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.frotas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: frotas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.frotas_id_seq OWNED BY public.frotas.id;


--
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.funcionarios (
    id integer NOT NULL,
    nome character varying(160) NOT NULL,
    cpf character varying(14),
    rg character varying(20),
    data_nascimento date,
    email_corporativo character varying(180) NOT NULL,
    telefone character varying(30),
    cargo character varying(120),
    setor character varying(80),
    data_admissao date,
    data_demissao date,
    salario_base numeric(14,2),
    status character varying(30) DEFAULT 'ativo'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: funcionarios_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.funcionarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: funcionarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.funcionarios_id_seq OWNED BY public.funcionarios.id;


--
-- Name: historicos_status; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.historicos_status (
    id integer NOT NULL,
    entidade character varying(80) NOT NULL,
    entidade_id integer NOT NULL,
    status_anterior character varying(30),
    status_novo character varying(30) NOT NULL,
    data_alteracao timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    usuario_id integer,
    observacao text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: historicos_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.historicos_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: historicos_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.historicos_status_id_seq OWNED BY public.historicos_status.id;


--
-- Name: insumos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.insumos (
    id integer NOT NULL,
    nome character varying(160) NOT NULL,
    descricao text,
    unidade_medida character varying(20) DEFAULT 'un'::character varying NOT NULL,
    quantidade_atual numeric(14,3) DEFAULT 0 NOT NULL,
    estoque_minimo numeric(14,3) DEFAULT 0 NOT NULL,
    valor_unitario numeric(14,2),
    status character varying(30) DEFAULT 'ativo'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: insumos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.insumos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: insumos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.insumos_id_seq OWNED BY public.insumos.id;


--
-- Name: itens_orcamento; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.itens_orcamento (
    id integer NOT NULL,
    orcamento_base_id integer NOT NULL,
    categoria_financeira_id integer,
    codigo character varying(40) NOT NULL,
    etapa character varying(120),
    descricao character varying(200) NOT NULL,
    unidade_medida character varying(20) DEFAULT 'un'::character varying NOT NULL,
    quantidade numeric(16,3) DEFAULT '1'::numeric NOT NULL,
    valor_unitario numeric(16,2) DEFAULT '0'::numeric NOT NULL,
    valor_total numeric(16,2) DEFAULT '0'::numeric NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_item_orcamento_valores CHECK (((quantidade >= (0)::numeric) AND (valor_unitario >= (0)::numeric) AND (valor_total >= (0)::numeric)))
);


--
-- Name: itens_orcamento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.itens_orcamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: itens_orcamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.itens_orcamento_id_seq OWNED BY public.itens_orcamento.id;


--
-- Name: itens_ordem_compra; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.itens_ordem_compra (
    id integer NOT NULL,
    ordem_compra_id integer NOT NULL,
    insumo_id integer,
    descricao character varying(180) NOT NULL,
    quantidade numeric(14,3) NOT NULL,
    valor_unitario numeric(14,2) NOT NULL,
    valor_total numeric(14,2) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: itens_ordem_compra_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.itens_ordem_compra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: itens_ordem_compra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.itens_ordem_compra_id_seq OWNED BY public.itens_ordem_compra.id;


--
-- Name: logs_auditoria; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.logs_auditoria (
    id integer NOT NULL,
    usuario_id integer,
    modulo character varying(80) NOT NULL,
    acao character varying(80) NOT NULL,
    entidade character varying(120),
    entidade_id integer,
    nivel character varying(30) DEFAULT 'info'::character varying NOT NULL,
    descricao text,
    ip_origem character varying(80),
    user_agent text,
    dados_anteriores jsonb,
    dados_novos jsonb,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: logs_auditoria_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.logs_auditoria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: logs_auditoria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.logs_auditoria_id_seq OWNED BY public.logs_auditoria.id;


--
-- Name: manutencoes_frota; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.manutencoes_frota (
    id integer NOT NULL,
    frota_id integer NOT NULL,
    fornecedor_id integer,
    obra_id integer,
    tipo character varying(30) NOT NULL,
    descricao text NOT NULL,
    data_entrada date NOT NULL,
    data_saida date,
    custo numeric(16,2) DEFAULT '0'::numeric NOT NULL,
    horimetro numeric(14,2),
    status character varying(30) DEFAULT 'aberta'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_manutencao_custo CHECK ((custo >= (0)::numeric))
);


--
-- Name: manutencoes_frota_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.manutencoes_frota_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: manutencoes_frota_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.manutencoes_frota_id_seq OWNED BY public.manutencoes_frota.id;


--
-- Name: medicoes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.medicoes (
    id integer NOT NULL,
    obra_id integer NOT NULL,
    contrato_id integer,
    competencia character varying(7) NOT NULL,
    valor_medido numeric(14,2) NOT NULL,
    data_medicao date,
    status character varying(30) DEFAULT 'pendente'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: medicoes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.medicoes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: medicoes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.medicoes_id_seq OWNED BY public.medicoes.id;


--
-- Name: metas_indicadores; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.metas_indicadores (
    id integer NOT NULL,
    codigo_indicador character varying(60) NOT NULL,
    nome character varying(140) NOT NULL,
    competencia character varying(7) NOT NULL,
    valor_meta numeric(18,4) NOT NULL,
    unidade character varying(30) DEFAULT 'numero'::character varying NOT NULL,
    centro_custo_id integer,
    obra_id integer,
    observacao text,
    ativo boolean DEFAULT true NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


--
-- Name: metas_indicadores_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.metas_indicadores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: metas_indicadores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.metas_indicadores_id_seq OWNED BY public.metas_indicadores.id;


--
-- Name: movimentacoes_caixa; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.movimentacoes_caixa (
    id integer NOT NULL,
    conta_bancaria_id integer NOT NULL,
    conta_pagar_id integer,
    conta_receber_id integer,
    fatura_id integer,
    categoria_financeira_id integer NOT NULL,
    centro_custo_id integer,
    tipo character varying(10) NOT NULL,
    data_movimentacao date NOT NULL,
    valor numeric(16,2) NOT NULL,
    descricao character varying(200) NOT NULL,
    forma_pagamento character varying(40),
    conciliado boolean DEFAULT false NOT NULL,
    data_conciliacao date,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_movimentacao_caixa_tipo CHECK (((tipo)::text = ANY ((ARRAY['entrada'::character varying, 'saida'::character varying])::text[]))),
    CONSTRAINT ck_movimentacao_caixa_valor CHECK ((valor > (0)::numeric))
);


--
-- Name: movimentacoes_caixa_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.movimentacoes_caixa_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: movimentacoes_caixa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.movimentacoes_caixa_id_seq OWNED BY public.movimentacoes_caixa.id;


--
-- Name: movimentacoes_estoque; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.movimentacoes_estoque (
    id integer NOT NULL,
    insumo_id integer NOT NULL,
    obra_id integer,
    tipo character varying(20) NOT NULL,
    quantidade numeric(14,3) NOT NULL,
    data_movimentacao date,
    observacao text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: movimentacoes_estoque_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.movimentacoes_estoque_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: movimentacoes_estoque_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.movimentacoes_estoque_id_seq OWNED BY public.movimentacoes_estoque.id;


--
-- Name: obras; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.obras (
    id integer NOT NULL,
    contrato_id integer NOT NULL,
    projeto_id integer NOT NULL,
    nome character varying(160) NOT NULL,
    descricao text,
    endereco text,
    cidade character varying(100),
    estado character varying(2),
    cep character varying(12),
    responsavel_id integer,
    data_inicio date,
    data_previsao_fim date,
    data_fim date,
    status character varying(30) DEFAULT 'planejada'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    percentual_fisico numeric(5,2) DEFAULT '0'::numeric NOT NULL,
    CONSTRAINT ck_obra_percentual_fisico CHECK (((percentual_fisico >= (0)::numeric) AND (percentual_fisico <= (100)::numeric)))
);


--
-- Name: obras_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.obras_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: obras_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.obras_id_seq OWNED BY public.obras.id;


--
-- Name: orcamentos_base; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.orcamentos_base (
    id integer NOT NULL,
    obra_id integer NOT NULL,
    versao integer DEFAULT 1 NOT NULL,
    descricao text,
    valor_total numeric(14,2) NOT NULL,
    data_aprovacao date,
    aprovado_por_id integer,
    status character varying(30) DEFAULT 'vigente'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: orcamentos_base_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.orcamentos_base_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: orcamentos_base_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.orcamentos_base_id_seq OWNED BY public.orcamentos_base.id;


--
-- Name: ordens_compra; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ordens_compra (
    id integer NOT NULL,
    fornecedor_id integer NOT NULL,
    obra_id integer,
    numero character varying(60) NOT NULL,
    data_emissao date,
    valor_total numeric(14,2) NOT NULL,
    status character varying(30) DEFAULT 'aberta'::character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    cotacao_id integer,
    data_aprovacao date,
    data_recebimento date
);


--
-- Name: ordens_compra_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ordens_compra_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ordens_compra_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ordens_compra_id_seq OWNED BY public.ordens_compra.id;


--
-- Name: perfil_permissao; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.perfil_permissao (
    id integer NOT NULL,
    perfil_id integer NOT NULL,
    permissao_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: perfil_permissao_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.perfil_permissao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: perfil_permissao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.perfil_permissao_id_seq OWNED BY public.perfil_permissao.id;


--
-- Name: perfis; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.perfis (
    id integer NOT NULL,
    nome character varying(80) NOT NULL,
    descricao text,
    nivel_acesso integer DEFAULT 1 NOT NULL,
    ativo boolean DEFAULT true NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: perfis_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.perfis_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: perfis_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.perfis_id_seq OWNED BY public.perfis.id;


--
-- Name: permissoes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.permissoes (
    id integer NOT NULL,
    modulo character varying(80) NOT NULL,
    acao character varying(80) NOT NULL,
    descricao text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: permissoes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.permissoes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: permissoes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.permissoes_id_seq OWNED BY public.permissoes.id;


--
-- Name: projetos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projetos (
    id integer NOT NULL,
    contrato_id integer NOT NULL,
    responsavel_id integer,
    nome character varying(160) NOT NULL,
    descricao text,
    tipo_projeto character varying(80),
    data_inicio date,
    data_previsao_entrega date,
    data_entrega date,
    status character varying(30) DEFAULT 'em_elaboracao'::character varying NOT NULL,
    arquivo_projeto character varying(255),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: projetos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.projetos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: projetos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.projetos_id_seq OWNED BY public.projetos.id;


--
-- Name: registro_ponto; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.registro_ponto (
    id integer NOT NULL,
    funcionario_id integer NOT NULL,
    data date NOT NULL,
    entrada time without time zone,
    saida_intervalo time without time zone,
    retorno_intervalo time without time zone,
    saida time without time zone,
    observacao text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: registro_ponto_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.registro_ponto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: registro_ponto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.registro_ponto_id_seq OWNED BY public.registro_ponto.id;


--
-- Name: revisoes_projeto; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.revisoes_projeto (
    id integer NOT NULL,
    projeto_id integer NOT NULL,
    responsavel_id integer,
    numero_revisao integer NOT NULL,
    descricao text,
    motivo text,
    arquivo_revisao character varying(255),
    data_revisao date,
    aprovado boolean DEFAULT false NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: revisoes_projeto_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.revisoes_projeto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: revisoes_projeto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.revisoes_projeto_id_seq OWNED BY public.revisoes_projeto.id;


--
-- Name: sessoes_usuario; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sessoes_usuario (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    token_sessao_hash character varying(255) NOT NULL,
    ip_origem character varying(80),
    user_agent text,
    data_login timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    data_expiracao timestamp without time zone NOT NULL,
    ativo boolean DEFAULT true NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: sessoes_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.sessoes_usuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: sessoes_usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.sessoes_usuario_id_seq OWNED BY public.sessoes_usuario.id;


--
-- Name: tokens_refresh; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tokens_refresh (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    token_hash character varying(255) NOT NULL,
    data_criacao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    data_expiracao timestamp without time zone NOT NULL,
    revogado boolean DEFAULT false NOT NULL,
    ip_origem character varying(80),
    user_agent text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: tokens_refresh_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tokens_refresh_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tokens_refresh_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tokens_refresh_id_seq OWNED BY public.tokens_refresh.id;


--
-- Name: usuario_perfil; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.usuario_perfil (
    id integer NOT NULL,
    usuario_id integer NOT NULL,
    perfil_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: usuario_perfil_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.usuario_perfil_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: usuario_perfil_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.usuario_perfil_id_seq OWNED BY public.usuario_perfil.id;


--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.usuarios (
    id integer NOT NULL,
    funcionario_id integer NOT NULL,
    username character varying(80) NOT NULL,
    email character varying(180) NOT NULL,
    senha_hash character varying(255) NOT NULL,
    ativo boolean DEFAULT true NOT NULL,
    bloqueado boolean DEFAULT false NOT NULL,
    tentativas_login integer DEFAULT 0 NOT NULL,
    ultimo_login timestamp without time zone,
    data_criacao timestamp without time zone,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


--
-- Name: usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;


--
-- Name: utilizacoes_frota; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.utilizacoes_frota (
    id integer NOT NULL,
    frota_id integer NOT NULL,
    obra_id integer,
    funcionario_id integer,
    data_utilizacao date NOT NULL,
    horas_utilizadas numeric(10,2) NOT NULL,
    horimetro_inicial numeric(14,2),
    horimetro_final numeric(14,2),
    custo_hora numeric(14,2) DEFAULT '0'::numeric NOT NULL,
    observacao text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT ck_utilizacao_frota_valores CHECK (((horas_utilizadas >= (0)::numeric) AND (custo_hora >= (0)::numeric)))
);


--
-- Name: utilizacoes_frota_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.utilizacoes_frota_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: utilizacoes_frota_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.utilizacoes_frota_id_seq OWNED BY public.utilizacoes_frota.id;


--
-- Name: abastecimentos_frota id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abastecimentos_frota ALTER COLUMN id SET DEFAULT nextval('public.abastecimentos_frota_id_seq'::regclass);


--
-- Name: agenda_visitas id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.agenda_visitas ALTER COLUMN id SET DEFAULT nextval('public.agenda_visitas_id_seq'::regclass);


--
-- Name: alocacoes_funcionario_obra id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alocacoes_funcionario_obra ALTER COLUMN id SET DEFAULT nextval('public.alocacoes_funcionario_obra_id_seq'::regclass);


--
-- Name: apropriacoes_custo id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo ALTER COLUMN id SET DEFAULT nextval('public.apropriacoes_custo_id_seq'::regclass);


--
-- Name: categorias_financeiras id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias_financeiras ALTER COLUMN id SET DEFAULT nextval('public.categorias_financeiras_id_seq'::regclass);


--
-- Name: centros_custo id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.centros_custo ALTER COLUMN id SET DEFAULT nextval('public.centros_custo_id_seq'::regclass);


--
-- Name: chamados_tecnicos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chamados_tecnicos ALTER COLUMN id SET DEFAULT nextval('public.chamados_tecnicos_id_seq'::regclass);


--
-- Name: clientes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clientes ALTER COLUMN id SET DEFAULT nextval('public.clientes_id_seq'::regclass);


--
-- Name: contas_bancarias id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_bancarias ALTER COLUMN id SET DEFAULT nextval('public.contas_bancarias_id_seq'::regclass);


--
-- Name: contas_pagar id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_pagar ALTER COLUMN id SET DEFAULT nextval('public.contas_pagar_id_seq'::regclass);


--
-- Name: contas_receber id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber ALTER COLUMN id SET DEFAULT nextval('public.contas_receber_id_seq'::regclass);


--
-- Name: contratos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contratos ALTER COLUMN id SET DEFAULT nextval('public.contratos_id_seq'::regclass);


--
-- Name: cotacoes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cotacoes ALTER COLUMN id SET DEFAULT nextval('public.cotacoes_id_seq'::regclass);


--
-- Name: cronogramas id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cronogramas ALTER COLUMN id SET DEFAULT nextval('public.cronogramas_id_seq'::regclass);


--
-- Name: diarios_obra id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.diarios_obra ALTER COLUMN id SET DEFAULT nextval('public.diarios_obra_id_seq'::regclass);


--
-- Name: faturas id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faturas ALTER COLUMN id SET DEFAULT nextval('public.faturas_id_seq'::regclass);


--
-- Name: folha_pagamento id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.folha_pagamento ALTER COLUMN id SET DEFAULT nextval('public.folha_pagamento_id_seq'::regclass);


--
-- Name: fornecedores id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fornecedores ALTER COLUMN id SET DEFAULT nextval('public.fornecedores_id_seq'::regclass);


--
-- Name: frotas id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frotas ALTER COLUMN id SET DEFAULT nextval('public.frotas_id_seq'::regclass);


--
-- Name: funcionarios id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funcionarios ALTER COLUMN id SET DEFAULT nextval('public.funcionarios_id_seq'::regclass);


--
-- Name: historicos_status id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historicos_status ALTER COLUMN id SET DEFAULT nextval('public.historicos_status_id_seq'::regclass);


--
-- Name: insumos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.insumos ALTER COLUMN id SET DEFAULT nextval('public.insumos_id_seq'::regclass);


--
-- Name: itens_orcamento id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_orcamento ALTER COLUMN id SET DEFAULT nextval('public.itens_orcamento_id_seq'::regclass);


--
-- Name: itens_ordem_compra id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_ordem_compra ALTER COLUMN id SET DEFAULT nextval('public.itens_ordem_compra_id_seq'::regclass);


--
-- Name: logs_auditoria id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.logs_auditoria ALTER COLUMN id SET DEFAULT nextval('public.logs_auditoria_id_seq'::regclass);


--
-- Name: manutencoes_frota id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.manutencoes_frota ALTER COLUMN id SET DEFAULT nextval('public.manutencoes_frota_id_seq'::regclass);


--
-- Name: medicoes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.medicoes ALTER COLUMN id SET DEFAULT nextval('public.medicoes_id_seq'::regclass);


--
-- Name: metas_indicadores id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.metas_indicadores ALTER COLUMN id SET DEFAULT nextval('public.metas_indicadores_id_seq'::regclass);


--
-- Name: movimentacoes_caixa id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa ALTER COLUMN id SET DEFAULT nextval('public.movimentacoes_caixa_id_seq'::regclass);


--
-- Name: movimentacoes_estoque id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_estoque ALTER COLUMN id SET DEFAULT nextval('public.movimentacoes_estoque_id_seq'::regclass);


--
-- Name: obras id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.obras ALTER COLUMN id SET DEFAULT nextval('public.obras_id_seq'::regclass);


--
-- Name: orcamentos_base id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orcamentos_base ALTER COLUMN id SET DEFAULT nextval('public.orcamentos_base_id_seq'::regclass);


--
-- Name: ordens_compra id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ordens_compra ALTER COLUMN id SET DEFAULT nextval('public.ordens_compra_id_seq'::regclass);


--
-- Name: perfil_permissao id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perfil_permissao ALTER COLUMN id SET DEFAULT nextval('public.perfil_permissao_id_seq'::regclass);


--
-- Name: perfis id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perfis ALTER COLUMN id SET DEFAULT nextval('public.perfis_id_seq'::regclass);


--
-- Name: permissoes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.permissoes ALTER COLUMN id SET DEFAULT nextval('public.permissoes_id_seq'::regclass);


--
-- Name: projetos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projetos ALTER COLUMN id SET DEFAULT nextval('public.projetos_id_seq'::regclass);


--
-- Name: registro_ponto id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.registro_ponto ALTER COLUMN id SET DEFAULT nextval('public.registro_ponto_id_seq'::regclass);


--
-- Name: revisoes_projeto id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.revisoes_projeto ALTER COLUMN id SET DEFAULT nextval('public.revisoes_projeto_id_seq'::regclass);


--
-- Name: sessoes_usuario id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sessoes_usuario ALTER COLUMN id SET DEFAULT nextval('public.sessoes_usuario_id_seq'::regclass);


--
-- Name: tokens_refresh id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tokens_refresh ALTER COLUMN id SET DEFAULT nextval('public.tokens_refresh_id_seq'::regclass);


--
-- Name: usuario_perfil id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario_perfil ALTER COLUMN id SET DEFAULT nextval('public.usuario_perfil_id_seq'::regclass);


--
-- Name: usuarios id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);


--
-- Name: utilizacoes_frota id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilizacoes_frota ALTER COLUMN id SET DEFAULT nextval('public.utilizacoes_frota_id_seq'::regclass);


--
-- Name: abastecimentos_frota abastecimentos_frota_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abastecimentos_frota
    ADD CONSTRAINT abastecimentos_frota_pkey PRIMARY KEY (id);


--
-- Name: agenda_visitas agenda_visitas_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.agenda_visitas
    ADD CONSTRAINT agenda_visitas_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: alocacoes_funcionario_obra alocacoes_funcionario_obra_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alocacoes_funcionario_obra
    ADD CONSTRAINT alocacoes_funcionario_obra_pkey PRIMARY KEY (id);


--
-- Name: apropriacoes_custo apropriacoes_custo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT apropriacoes_custo_pkey PRIMARY KEY (id);


--
-- Name: categorias_financeiras categorias_financeiras_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias_financeiras
    ADD CONSTRAINT categorias_financeiras_pkey PRIMARY KEY (id);


--
-- Name: centros_custo centros_custo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.centros_custo
    ADD CONSTRAINT centros_custo_pkey PRIMARY KEY (id);


--
-- Name: chamados_tecnicos chamados_tecnicos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chamados_tecnicos
    ADD CONSTRAINT chamados_tecnicos_pkey PRIMARY KEY (id);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- Name: contas_bancarias contas_bancarias_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_bancarias
    ADD CONSTRAINT contas_bancarias_pkey PRIMARY KEY (id);


--
-- Name: contas_pagar contas_pagar_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_pagar
    ADD CONSTRAINT contas_pagar_pkey PRIMARY KEY (id);


--
-- Name: contas_receber contas_receber_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber
    ADD CONSTRAINT contas_receber_pkey PRIMARY KEY (id);


--
-- Name: contratos contratos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contratos
    ADD CONSTRAINT contratos_pkey PRIMARY KEY (id);


--
-- Name: cotacoes cotacoes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cotacoes
    ADD CONSTRAINT cotacoes_pkey PRIMARY KEY (id);


--
-- Name: cronogramas cronogramas_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cronogramas
    ADD CONSTRAINT cronogramas_pkey PRIMARY KEY (id);


--
-- Name: diarios_obra diarios_obra_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.diarios_obra
    ADD CONSTRAINT diarios_obra_pkey PRIMARY KEY (id);


--
-- Name: faturas faturas_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faturas
    ADD CONSTRAINT faturas_pkey PRIMARY KEY (id);


--
-- Name: folha_pagamento folha_pagamento_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.folha_pagamento
    ADD CONSTRAINT folha_pagamento_pkey PRIMARY KEY (id);


--
-- Name: fornecedores fornecedores_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.fornecedores
    ADD CONSTRAINT fornecedores_pkey PRIMARY KEY (id);


--
-- Name: frotas frotas_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frotas
    ADD CONSTRAINT frotas_pkey PRIMARY KEY (id);


--
-- Name: funcionarios funcionarios_email_corporativo_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_email_corporativo_key UNIQUE (email_corporativo);


--
-- Name: funcionarios funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (id);


--
-- Name: historicos_status historicos_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historicos_status
    ADD CONSTRAINT historicos_status_pkey PRIMARY KEY (id);


--
-- Name: insumos insumos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.insumos
    ADD CONSTRAINT insumos_pkey PRIMARY KEY (id);


--
-- Name: itens_orcamento itens_orcamento_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_orcamento
    ADD CONSTRAINT itens_orcamento_pkey PRIMARY KEY (id);


--
-- Name: itens_ordem_compra itens_ordem_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_ordem_compra
    ADD CONSTRAINT itens_ordem_compra_pkey PRIMARY KEY (id);


--
-- Name: logs_auditoria logs_auditoria_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.logs_auditoria
    ADD CONSTRAINT logs_auditoria_pkey PRIMARY KEY (id);


--
-- Name: manutencoes_frota manutencoes_frota_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.manutencoes_frota
    ADD CONSTRAINT manutencoes_frota_pkey PRIMARY KEY (id);


--
-- Name: medicoes medicoes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.medicoes
    ADD CONSTRAINT medicoes_pkey PRIMARY KEY (id);


--
-- Name: metas_indicadores metas_indicadores_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.metas_indicadores
    ADD CONSTRAINT metas_indicadores_pkey PRIMARY KEY (id);


--
-- Name: movimentacoes_caixa movimentacoes_caixa_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa
    ADD CONSTRAINT movimentacoes_caixa_pkey PRIMARY KEY (id);


--
-- Name: movimentacoes_estoque movimentacoes_estoque_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_estoque
    ADD CONSTRAINT movimentacoes_estoque_pkey PRIMARY KEY (id);


--
-- Name: obras obras_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.obras
    ADD CONSTRAINT obras_pkey PRIMARY KEY (id);


--
-- Name: orcamentos_base orcamentos_base_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orcamentos_base
    ADD CONSTRAINT orcamentos_base_pkey PRIMARY KEY (id);


--
-- Name: ordens_compra ordens_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ordens_compra
    ADD CONSTRAINT ordens_compra_pkey PRIMARY KEY (id);


--
-- Name: perfil_permissao perfil_permissao_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perfil_permissao
    ADD CONSTRAINT perfil_permissao_pkey PRIMARY KEY (id);


--
-- Name: perfis perfis_nome_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perfis
    ADD CONSTRAINT perfis_nome_key UNIQUE (nome);


--
-- Name: perfis perfis_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perfis
    ADD CONSTRAINT perfis_pkey PRIMARY KEY (id);


--
-- Name: permissoes permissoes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.permissoes
    ADD CONSTRAINT permissoes_pkey PRIMARY KEY (id);


--
-- Name: projetos projetos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projetos
    ADD CONSTRAINT projetos_pkey PRIMARY KEY (id);


--
-- Name: registro_ponto registro_ponto_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.registro_ponto
    ADD CONSTRAINT registro_ponto_pkey PRIMARY KEY (id);


--
-- Name: revisoes_projeto revisoes_projeto_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.revisoes_projeto
    ADD CONSTRAINT revisoes_projeto_pkey PRIMARY KEY (id);


--
-- Name: sessoes_usuario sessoes_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sessoes_usuario
    ADD CONSTRAINT sessoes_usuario_pkey PRIMARY KEY (id);


--
-- Name: tokens_refresh tokens_refresh_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tokens_refresh
    ADD CONSTRAINT tokens_refresh_pkey PRIMARY KEY (id);


--
-- Name: categorias_financeiras uq_categoria_financeira_codigo; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias_financeiras
    ADD CONSTRAINT uq_categoria_financeira_codigo UNIQUE (codigo);


--
-- Name: categorias_financeiras uq_categoria_financeira_nome; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias_financeiras
    ADD CONSTRAINT uq_categoria_financeira_nome UNIQUE (nome);


--
-- Name: centros_custo uq_centro_custo_codigo; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.centros_custo
    ADD CONSTRAINT uq_centro_custo_codigo UNIQUE (codigo);


--
-- Name: centros_custo uq_centro_custo_obra; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.centros_custo
    ADD CONSTRAINT uq_centro_custo_obra UNIQUE (obra_id);


--
-- Name: contas_bancarias uq_conta_bancaria_identificacao; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_bancarias
    ADD CONSTRAINT uq_conta_bancaria_identificacao UNIQUE (banco, agencia, numero_conta);


--
-- Name: faturas uq_fatura_numero_documento; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faturas
    ADD CONSTRAINT uq_fatura_numero_documento UNIQUE (numero_documento);


--
-- Name: itens_orcamento uq_item_orcamento_codigo; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_orcamento
    ADD CONSTRAINT uq_item_orcamento_codigo UNIQUE (orcamento_base_id, codigo);


--
-- Name: permissoes uq_permissao_modulo_acao; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.permissoes
    ADD CONSTRAINT uq_permissao_modulo_acao UNIQUE (modulo, acao);


--
-- Name: usuario_perfil usuario_perfil_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario_perfil
    ADD CONSTRAINT usuario_perfil_pkey PRIMARY KEY (id);


--
-- Name: usuarios usuarios_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_email_key UNIQUE (email);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);


--
-- Name: usuarios usuarios_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_username_key UNIQUE (username);


--
-- Name: utilizacoes_frota utilizacoes_frota_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilizacoes_frota
    ADD CONSTRAINT utilizacoes_frota_pkey PRIMARY KEY (id);


--
-- Name: ix_abastecimento_frota_data; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_abastecimento_frota_data ON public.abastecimentos_frota USING btree (frota_id, data_abastecimento);


--
-- Name: ix_alocacao_obra_ativo; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_alocacao_obra_ativo ON public.alocacoes_funcionario_obra USING btree (obra_id, ativo);


--
-- Name: ix_apropriacao_obra_competencia; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_apropriacao_obra_competencia ON public.apropriacoes_custo USING btree (obra_id, competencia);


--
-- Name: ix_categoria_financeira_tipo_ativo; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_categoria_financeira_tipo_ativo ON public.categorias_financeiras USING btree (tipo, ativo);


--
-- Name: ix_centro_custo_tipo_ativo; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_centro_custo_tipo_ativo ON public.centros_custo USING btree (tipo, ativo);


--
-- Name: ix_conta_pagar_competencia; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_conta_pagar_competencia ON public.contas_pagar USING btree (data_competencia);


--
-- Name: ix_conta_receber_competencia; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_conta_receber_competencia ON public.contas_receber USING btree (data_competencia);


--
-- Name: ix_fatura_competencia_status; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_fatura_competencia_status ON public.faturas USING btree (competencia, status);


--
-- Name: ix_fatura_obra; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_fatura_obra ON public.faturas USING btree (obra_id);


--
-- Name: ix_historico_entidade_data; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_historico_entidade_data ON public.historicos_status USING btree (entidade, entidade_id, data_alteracao);


--
-- Name: ix_item_orcamento_etapa; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_item_orcamento_etapa ON public.itens_orcamento USING btree (orcamento_base_id, etapa);


--
-- Name: ix_manutencao_frota_data; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_manutencao_frota_data ON public.manutencoes_frota USING btree (frota_id, data_entrada);


--
-- Name: ix_meta_indicador_competencia; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_meta_indicador_competencia ON public.metas_indicadores USING btree (codigo_indicador, competencia);


--
-- Name: ix_movimento_caixa_centro; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_movimento_caixa_centro ON public.movimentacoes_caixa USING btree (centro_custo_id);


--
-- Name: ix_movimento_caixa_data_tipo; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_movimento_caixa_data_tipo ON public.movimentacoes_caixa USING btree (data_movimentacao, tipo);


--
-- Name: ix_utilizacao_frota_data; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_utilizacao_frota_data ON public.utilizacoes_frota USING btree (frota_id, data_utilizacao);


--
-- Name: abastecimentos_frota fk_abastecimento_frota; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abastecimentos_frota
    ADD CONSTRAINT fk_abastecimento_frota FOREIGN KEY (frota_id) REFERENCES public.frotas(id) ON DELETE CASCADE;


--
-- Name: abastecimentos_frota fk_abastecimento_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abastecimentos_frota
    ADD CONSTRAINT fk_abastecimento_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE SET NULL;


--
-- Name: abastecimentos_frota fk_abastecimento_responsavel; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abastecimentos_frota
    ADD CONSTRAINT fk_abastecimento_responsavel FOREIGN KEY (responsavel_id) REFERENCES public.funcionarios(id) ON DELETE SET NULL;


--
-- Name: agenda_visitas fk_agenda_visitas_cliente_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.agenda_visitas
    ADD CONSTRAINT fk_agenda_visitas_cliente_id FOREIGN KEY (cliente_id) REFERENCES public.clientes(id);


--
-- Name: agenda_visitas fk_agenda_visitas_funcionario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.agenda_visitas
    ADD CONSTRAINT fk_agenda_visitas_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id);


--
-- Name: alocacoes_funcionario_obra fk_alocacao_centro_custo; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alocacoes_funcionario_obra
    ADD CONSTRAINT fk_alocacao_centro_custo FOREIGN KEY (centro_custo_id) REFERENCES public.centros_custo(id) ON DELETE SET NULL;


--
-- Name: alocacoes_funcionario_obra fk_alocacao_funcionario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alocacoes_funcionario_obra
    ADD CONSTRAINT fk_alocacao_funcionario FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id) ON DELETE CASCADE;


--
-- Name: alocacoes_funcionario_obra fk_alocacao_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alocacoes_funcionario_obra
    ADD CONSTRAINT fk_alocacao_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE CASCADE;


--
-- Name: apropriacoes_custo fk_apropriacao_categoria; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT fk_apropriacao_categoria FOREIGN KEY (categoria_financeira_id) REFERENCES public.categorias_financeiras(id) ON DELETE RESTRICT;


--
-- Name: apropriacoes_custo fk_apropriacao_centro; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT fk_apropriacao_centro FOREIGN KEY (centro_custo_id) REFERENCES public.centros_custo(id) ON DELETE SET NULL;


--
-- Name: apropriacoes_custo fk_apropriacao_conta_pagar; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT fk_apropriacao_conta_pagar FOREIGN KEY (conta_pagar_id) REFERENCES public.contas_pagar(id) ON DELETE SET NULL;


--
-- Name: apropriacoes_custo fk_apropriacao_frota; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT fk_apropriacao_frota FOREIGN KEY (frota_id) REFERENCES public.frotas(id) ON DELETE SET NULL;


--
-- Name: apropriacoes_custo fk_apropriacao_funcionario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT fk_apropriacao_funcionario FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id) ON DELETE SET NULL;


--
-- Name: apropriacoes_custo fk_apropriacao_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT fk_apropriacao_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE CASCADE;


--
-- Name: apropriacoes_custo fk_apropriacao_ordem; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.apropriacoes_custo
    ADD CONSTRAINT fk_apropriacao_ordem FOREIGN KEY (ordem_compra_id) REFERENCES public.ordens_compra(id) ON DELETE SET NULL;


--
-- Name: categorias_financeiras fk_categoria_pai; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.categorias_financeiras
    ADD CONSTRAINT fk_categoria_pai FOREIGN KEY (categoria_pai_id) REFERENCES public.categorias_financeiras(id) ON DELETE SET NULL;


--
-- Name: centros_custo fk_centro_custo_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.centros_custo
    ADD CONSTRAINT fk_centro_custo_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE SET NULL;


--
-- Name: centros_custo fk_centro_custo_responsavel; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.centros_custo
    ADD CONSTRAINT fk_centro_custo_responsavel FOREIGN KEY (responsavel_id) REFERENCES public.funcionarios(id) ON DELETE SET NULL;


--
-- Name: chamados_tecnicos fk_chamados_tecnicos_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chamados_tecnicos
    ADD CONSTRAINT fk_chamados_tecnicos_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: chamados_tecnicos fk_chamados_tecnicos_solicitante_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chamados_tecnicos
    ADD CONSTRAINT fk_chamados_tecnicos_solicitante_id FOREIGN KEY (solicitante_id) REFERENCES public.funcionarios(id);


--
-- Name: contas_pagar fk_conta_pagar_categoria; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_pagar
    ADD CONSTRAINT fk_conta_pagar_categoria FOREIGN KEY (categoria_financeira_id) REFERENCES public.categorias_financeiras(id) ON DELETE SET NULL;


--
-- Name: contas_pagar fk_conta_pagar_centro; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_pagar
    ADD CONSTRAINT fk_conta_pagar_centro FOREIGN KEY (centro_custo_id) REFERENCES public.centros_custo(id) ON DELETE SET NULL;


--
-- Name: contas_receber fk_conta_receber_categoria; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber
    ADD CONSTRAINT fk_conta_receber_categoria FOREIGN KEY (categoria_financeira_id) REFERENCES public.categorias_financeiras(id) ON DELETE SET NULL;


--
-- Name: contas_receber fk_conta_receber_centro; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber
    ADD CONSTRAINT fk_conta_receber_centro FOREIGN KEY (centro_custo_id) REFERENCES public.centros_custo(id) ON DELETE SET NULL;


--
-- Name: contas_receber fk_conta_receber_fatura; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber
    ADD CONSTRAINT fk_conta_receber_fatura FOREIGN KEY (fatura_id) REFERENCES public.faturas(id) ON DELETE SET NULL;


--
-- Name: contas_pagar fk_contas_pagar_fornecedor_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_pagar
    ADD CONSTRAINT fk_contas_pagar_fornecedor_id FOREIGN KEY (fornecedor_id) REFERENCES public.fornecedores(id);


--
-- Name: contas_pagar fk_contas_pagar_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_pagar
    ADD CONSTRAINT fk_contas_pagar_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: contas_pagar fk_contas_pagar_ordem_compra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_pagar
    ADD CONSTRAINT fk_contas_pagar_ordem_compra_id FOREIGN KEY (ordem_compra_id) REFERENCES public.ordens_compra(id);


--
-- Name: contas_receber fk_contas_receber_cliente_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber
    ADD CONSTRAINT fk_contas_receber_cliente_id FOREIGN KEY (cliente_id) REFERENCES public.clientes(id);


--
-- Name: contas_receber fk_contas_receber_contrato_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber
    ADD CONSTRAINT fk_contas_receber_contrato_id FOREIGN KEY (contrato_id) REFERENCES public.contratos(id);


--
-- Name: contas_receber fk_contas_receber_medicao_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contas_receber
    ADD CONSTRAINT fk_contas_receber_medicao_id FOREIGN KEY (medicao_id) REFERENCES public.medicoes(id);


--
-- Name: contratos fk_contratos_cliente_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.contratos
    ADD CONSTRAINT fk_contratos_cliente_id FOREIGN KEY (cliente_id) REFERENCES public.clientes(id);


--
-- Name: cotacoes fk_cotacoes_fornecedor_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cotacoes
    ADD CONSTRAINT fk_cotacoes_fornecedor_id FOREIGN KEY (fornecedor_id) REFERENCES public.fornecedores(id);


--
-- Name: cotacoes fk_cotacoes_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cotacoes
    ADD CONSTRAINT fk_cotacoes_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: cronogramas fk_cronogramas_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.cronogramas
    ADD CONSTRAINT fk_cronogramas_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: diarios_obra fk_diarios_obra_funcionario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.diarios_obra
    ADD CONSTRAINT fk_diarios_obra_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id);


--
-- Name: diarios_obra fk_diarios_obra_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.diarios_obra
    ADD CONSTRAINT fk_diarios_obra_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: faturas fk_fatura_cliente; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faturas
    ADD CONSTRAINT fk_fatura_cliente FOREIGN KEY (cliente_id) REFERENCES public.clientes(id) ON DELETE RESTRICT;


--
-- Name: faturas fk_fatura_contrato; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faturas
    ADD CONSTRAINT fk_fatura_contrato FOREIGN KEY (contrato_id) REFERENCES public.contratos(id) ON DELETE SET NULL;


--
-- Name: faturas fk_fatura_medicao; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faturas
    ADD CONSTRAINT fk_fatura_medicao FOREIGN KEY (medicao_id) REFERENCES public.medicoes(id) ON DELETE SET NULL;


--
-- Name: faturas fk_fatura_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.faturas
    ADD CONSTRAINT fk_fatura_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE SET NULL;


--
-- Name: folha_pagamento fk_folha_pagamento_funcionario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.folha_pagamento
    ADD CONSTRAINT fk_folha_pagamento_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id);


--
-- Name: frotas fk_frotas_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.frotas
    ADD CONSTRAINT fk_frotas_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: historicos_status fk_historico_status_usuario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historicos_status
    ADD CONSTRAINT fk_historico_status_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id) ON DELETE SET NULL;


--
-- Name: itens_orcamento fk_item_orcamento_base; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_orcamento
    ADD CONSTRAINT fk_item_orcamento_base FOREIGN KEY (orcamento_base_id) REFERENCES public.orcamentos_base(id) ON DELETE CASCADE;


--
-- Name: itens_orcamento fk_item_orcamento_categoria; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_orcamento
    ADD CONSTRAINT fk_item_orcamento_categoria FOREIGN KEY (categoria_financeira_id) REFERENCES public.categorias_financeiras(id) ON DELETE SET NULL;


--
-- Name: itens_ordem_compra fk_itens_ordem_compra_insumo_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_ordem_compra
    ADD CONSTRAINT fk_itens_ordem_compra_insumo_id FOREIGN KEY (insumo_id) REFERENCES public.insumos(id);


--
-- Name: itens_ordem_compra fk_itens_ordem_compra_ordem_compra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.itens_ordem_compra
    ADD CONSTRAINT fk_itens_ordem_compra_ordem_compra_id FOREIGN KEY (ordem_compra_id) REFERENCES public.ordens_compra(id);


--
-- Name: manutencoes_frota fk_manutencao_fornecedor; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.manutencoes_frota
    ADD CONSTRAINT fk_manutencao_fornecedor FOREIGN KEY (fornecedor_id) REFERENCES public.fornecedores(id) ON DELETE SET NULL;


--
-- Name: manutencoes_frota fk_manutencao_frota; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.manutencoes_frota
    ADD CONSTRAINT fk_manutencao_frota FOREIGN KEY (frota_id) REFERENCES public.frotas(id) ON DELETE CASCADE;


--
-- Name: manutencoes_frota fk_manutencao_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.manutencoes_frota
    ADD CONSTRAINT fk_manutencao_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE SET NULL;


--
-- Name: medicoes fk_medicoes_contrato_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.medicoes
    ADD CONSTRAINT fk_medicoes_contrato_id FOREIGN KEY (contrato_id) REFERENCES public.contratos(id);


--
-- Name: medicoes fk_medicoes_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.medicoes
    ADD CONSTRAINT fk_medicoes_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: metas_indicadores fk_meta_centro_custo; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.metas_indicadores
    ADD CONSTRAINT fk_meta_centro_custo FOREIGN KEY (centro_custo_id) REFERENCES public.centros_custo(id) ON DELETE SET NULL;


--
-- Name: metas_indicadores fk_meta_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.metas_indicadores
    ADD CONSTRAINT fk_meta_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE SET NULL;


--
-- Name: movimentacoes_estoque fk_movimentacoes_estoque_insumo_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_estoque
    ADD CONSTRAINT fk_movimentacoes_estoque_insumo_id FOREIGN KEY (insumo_id) REFERENCES public.insumos(id);


--
-- Name: movimentacoes_estoque fk_movimentacoes_estoque_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_estoque
    ADD CONSTRAINT fk_movimentacoes_estoque_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: movimentacoes_caixa fk_movimento_categoria; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa
    ADD CONSTRAINT fk_movimento_categoria FOREIGN KEY (categoria_financeira_id) REFERENCES public.categorias_financeiras(id) ON DELETE RESTRICT;


--
-- Name: movimentacoes_caixa fk_movimento_centro; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa
    ADD CONSTRAINT fk_movimento_centro FOREIGN KEY (centro_custo_id) REFERENCES public.centros_custo(id) ON DELETE SET NULL;


--
-- Name: movimentacoes_caixa fk_movimento_conta_bancaria; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa
    ADD CONSTRAINT fk_movimento_conta_bancaria FOREIGN KEY (conta_bancaria_id) REFERENCES public.contas_bancarias(id) ON DELETE RESTRICT;


--
-- Name: movimentacoes_caixa fk_movimento_conta_pagar; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa
    ADD CONSTRAINT fk_movimento_conta_pagar FOREIGN KEY (conta_pagar_id) REFERENCES public.contas_pagar(id) ON DELETE SET NULL;


--
-- Name: movimentacoes_caixa fk_movimento_conta_receber; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa
    ADD CONSTRAINT fk_movimento_conta_receber FOREIGN KEY (conta_receber_id) REFERENCES public.contas_receber(id) ON DELETE SET NULL;


--
-- Name: movimentacoes_caixa fk_movimento_fatura; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.movimentacoes_caixa
    ADD CONSTRAINT fk_movimento_fatura FOREIGN KEY (fatura_id) REFERENCES public.faturas(id) ON DELETE SET NULL;


--
-- Name: obras fk_obras_contrato_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.obras
    ADD CONSTRAINT fk_obras_contrato_id FOREIGN KEY (contrato_id) REFERENCES public.contratos(id);


--
-- Name: obras fk_obras_projeto_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.obras
    ADD CONSTRAINT fk_obras_projeto_id FOREIGN KEY (projeto_id) REFERENCES public.projetos(id);


--
-- Name: obras fk_obras_responsavel_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.obras
    ADD CONSTRAINT fk_obras_responsavel_id FOREIGN KEY (responsavel_id) REFERENCES public.funcionarios(id);


--
-- Name: orcamentos_base fk_orcamentos_base_aprovado_por_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orcamentos_base
    ADD CONSTRAINT fk_orcamentos_base_aprovado_por_id FOREIGN KEY (aprovado_por_id) REFERENCES public.funcionarios(id);


--
-- Name: orcamentos_base fk_orcamentos_base_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.orcamentos_base
    ADD CONSTRAINT fk_orcamentos_base_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: ordens_compra fk_ordem_compra_cotacao; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ordens_compra
    ADD CONSTRAINT fk_ordem_compra_cotacao FOREIGN KEY (cotacao_id) REFERENCES public.cotacoes(id) ON DELETE SET NULL;


--
-- Name: ordens_compra fk_ordens_compra_fornecedor_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ordens_compra
    ADD CONSTRAINT fk_ordens_compra_fornecedor_id FOREIGN KEY (fornecedor_id) REFERENCES public.fornecedores(id);


--
-- Name: ordens_compra fk_ordens_compra_obra_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ordens_compra
    ADD CONSTRAINT fk_ordens_compra_obra_id FOREIGN KEY (obra_id) REFERENCES public.obras(id);


--
-- Name: projetos fk_projetos_contrato_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projetos
    ADD CONSTRAINT fk_projetos_contrato_id FOREIGN KEY (contrato_id) REFERENCES public.contratos(id);


--
-- Name: projetos fk_projetos_responsavel_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projetos
    ADD CONSTRAINT fk_projetos_responsavel_id FOREIGN KEY (responsavel_id) REFERENCES public.funcionarios(id);


--
-- Name: registro_ponto fk_registro_ponto_funcionario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.registro_ponto
    ADD CONSTRAINT fk_registro_ponto_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id);


--
-- Name: revisoes_projeto fk_revisoes_projeto_projeto_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.revisoes_projeto
    ADD CONSTRAINT fk_revisoes_projeto_projeto_id FOREIGN KEY (projeto_id) REFERENCES public.projetos(id);


--
-- Name: revisoes_projeto fk_revisoes_projeto_responsavel_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.revisoes_projeto
    ADD CONSTRAINT fk_revisoes_projeto_responsavel_id FOREIGN KEY (responsavel_id) REFERENCES public.funcionarios(id);


--
-- Name: utilizacoes_frota fk_utilizacao_frota; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilizacoes_frota
    ADD CONSTRAINT fk_utilizacao_frota FOREIGN KEY (frota_id) REFERENCES public.frotas(id) ON DELETE CASCADE;


--
-- Name: utilizacoes_frota fk_utilizacao_funcionario; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilizacoes_frota
    ADD CONSTRAINT fk_utilizacao_funcionario FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id) ON DELETE SET NULL;


--
-- Name: utilizacoes_frota fk_utilizacao_obra; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.utilizacoes_frota
    ADD CONSTRAINT fk_utilizacao_obra FOREIGN KEY (obra_id) REFERENCES public.obras(id) ON DELETE SET NULL;


--
-- Name: logs_auditoria logs_auditoria_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.logs_auditoria
    ADD CONSTRAINT logs_auditoria_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: perfil_permissao perfil_permissao_perfil_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perfil_permissao
    ADD CONSTRAINT perfil_permissao_perfil_id_fkey FOREIGN KEY (perfil_id) REFERENCES public.perfis(id);


--
-- Name: perfil_permissao perfil_permissao_permissao_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.perfil_permissao
    ADD CONSTRAINT perfil_permissao_permissao_id_fkey FOREIGN KEY (permissao_id) REFERENCES public.permissoes(id);


--
-- Name: sessoes_usuario sessoes_usuario_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sessoes_usuario
    ADD CONSTRAINT sessoes_usuario_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: tokens_refresh tokens_refresh_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tokens_refresh
    ADD CONSTRAINT tokens_refresh_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: usuario_perfil usuario_perfil_perfil_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario_perfil
    ADD CONSTRAINT usuario_perfil_perfil_id_fkey FOREIGN KEY (perfil_id) REFERENCES public.perfis(id);


--
-- Name: usuario_perfil usuario_perfil_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario_perfil
    ADD CONSTRAINT usuario_perfil_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: usuarios usuarios_funcionario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_funcionario_id_fkey FOREIGN KEY (funcionario_id) REFERENCES public.funcionarios(id);


--
-- PostgreSQL database dump complete
--

\unrestrict EBxyVRYnVuMR1mAi3mH5zzSadkvsKrfPJmhhUg9yytaBdE1oSPlWDr5rnpIz45h

