    CREATE TABLE IF NOT EXISTS funcionarios (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(160) NOT NULL,
        cpf VARCHAR(14) NULL,
        rg VARCHAR(20) NULL,
        data_nascimento DATE NULL,
        email_corporativo VARCHAR(180) NOT NULL UNIQUE,
        telefone VARCHAR(30) NULL,
        cargo VARCHAR(120) NULL,
        setor VARCHAR(80) NULL,
        data_admissao DATE NULL,
        data_demissao DATE NULL,
        salario_base NUMERIC(14, 2) NULL,
        status VARCHAR(30) NOT NULL DEFAULT 'ativo',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        funcionario_id INTEGER NOT NULL REFERENCES funcionarios(id),
        username VARCHAR(80) NOT NULL UNIQUE,
        email VARCHAR(180) NOT NULL UNIQUE,
        senha_hash VARCHAR(255) NOT NULL,
        ativo BOOLEAN NOT NULL DEFAULT true,
        bloqueado BOOLEAN NOT NULL DEFAULT false,
        tentativas_login INTEGER NOT NULL DEFAULT 0,
        ultimo_login TIMESTAMP NULL,
        data_criacao TIMESTAMP NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS perfis (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(80) NOT NULL UNIQUE,
        descricao TEXT NULL,
        nivel_acesso INTEGER NOT NULL DEFAULT 1,
        ativo BOOLEAN NOT NULL DEFAULT true,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS permissoes (
        id SERIAL PRIMARY KEY,
        modulo VARCHAR(80) NOT NULL,
        acao VARCHAR(80) NOT NULL,
        descricao TEXT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT uq_permissao_modulo_acao UNIQUE (modulo, acao)
    );
    CREATE TABLE IF NOT EXISTS perfil_permissao (
        id SERIAL PRIMARY KEY,
        perfil_id INTEGER NOT NULL REFERENCES perfis(id),
        permissao_id INTEGER NOT NULL REFERENCES permissoes(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS usuario_perfil (
        id SERIAL PRIMARY KEY,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
        perfil_id INTEGER NOT NULL REFERENCES perfis(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS sessoes_usuario (
        id SERIAL PRIMARY KEY,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
        token_sessao_hash VARCHAR(255) NOT NULL,
        ip_origem VARCHAR(80) NULL,
        user_agent TEXT NULL,
        data_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        data_expiracao TIMESTAMP NOT NULL,
        ativo BOOLEAN NOT NULL DEFAULT true,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS tokens_refresh (
        id SERIAL PRIMARY KEY,
        usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
        token_hash VARCHAR(255) NOT NULL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        data_expiracao TIMESTAMP NOT NULL,
        revogado BOOLEAN NOT NULL DEFAULT false,
        ip_origem VARCHAR(80) NULL,
        user_agent TEXT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS logs_auditoria (
        id SERIAL PRIMARY KEY,
        usuario_id INTEGER NULL REFERENCES usuarios(id),
        modulo VARCHAR(80) NOT NULL,
        acao VARCHAR(80) NOT NULL,
        entidade VARCHAR(120) NULL,
        entidade_id INTEGER NULL,
        nivel VARCHAR(30) NOT NULL DEFAULT 'info',
        descricao TEXT NULL,
        ip_origem VARCHAR(80) NULL,
        user_agent TEXT NULL,
        dados_anteriores JSONB NULL,
        dados_novos JSONB NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );


CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(160) NOT NULL,
    tipo_pessoa VARCHAR(20) NOT NULL DEFAULT 'juridica',
    cpf_cnpj VARCHAR(20) NULL,
    email VARCHAR(180) NULL,
    telefone VARCHAR(30) NULL,
    endereco TEXT NULL,
    cidade VARCHAR(100) NULL,
    estado VARCHAR(2) NULL,
    cep VARCHAR(12) NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'ativo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contratos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    numero_contrato VARCHAR(60) NOT NULL,
    descricao TEXT NULL,
    valor_total NUMERIC(14, 2) NOT NULL,
    data_assinatura DATE NULL,
    data_inicio DATE NULL,
    data_fim DATE NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'ativo',
    arquivo_contrato VARCHAR(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS agenda_visitas (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    funcionario_id INTEGER NULL,
    data_visita DATE NOT NULL,
    horario TIME NULL,
    local_visita VARCHAR(180) NULL,
    observacoes TEXT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'agendada',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS projetos (
    id SERIAL PRIMARY KEY,
    contrato_id INTEGER NOT NULL,
    responsavel_id INTEGER NULL,
    nome VARCHAR(160) NOT NULL,
    descricao TEXT NULL,
    tipo_projeto VARCHAR(80) NULL,
    data_inicio DATE NULL,
    data_previsao_entrega DATE NULL,
    data_entrega DATE NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'em_elaboracao',
    arquivo_projeto VARCHAR(255) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS revisoes_projeto (
    id SERIAL PRIMARY KEY,
    projeto_id INTEGER NOT NULL,
    responsavel_id INTEGER NULL,
    numero_revisao INTEGER NOT NULL,
    descricao TEXT NULL,
    motivo TEXT NULL,
    arquivo_revisao VARCHAR(255) NULL,
    data_revisao DATE NULL,
    aprovado BOOLEAN NOT NULL DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS obras (
    id SERIAL PRIMARY KEY,
    contrato_id INTEGER NOT NULL,
    projeto_id INTEGER NOT NULL,
    nome VARCHAR(160) NOT NULL,
    descricao TEXT NULL,
    endereco TEXT NULL,
    cidade VARCHAR(100) NULL,
    estado VARCHAR(2) NULL,
    cep VARCHAR(12) NULL,
    responsavel_id INTEGER NULL,
    data_inicio DATE NULL,
    data_previsao_fim DATE NULL,
    data_fim DATE NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'planejada',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS diarios_obra (
    id SERIAL PRIMARY KEY,
    obra_id INTEGER NOT NULL,
    funcionario_id INTEGER NULL,
    data_registro DATE NOT NULL,
    clima VARCHAR(80) NULL,
    atividades TEXT NULL,
    ocorrencias TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS medicoes (
    id SERIAL PRIMARY KEY,
    obra_id INTEGER NOT NULL,
    contrato_id INTEGER NULL,
    competencia VARCHAR(7) NOT NULL,
    valor_medido NUMERIC(14, 2) NOT NULL,
    data_medicao DATE NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'pendente',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chamados_tecnicos (
    id SERIAL PRIMARY KEY,
    obra_id INTEGER NOT NULL,
    solicitante_id INTEGER NULL,
    titulo VARCHAR(160) NOT NULL,
    descricao TEXT NULL,
    prioridade VARCHAR(30) NOT NULL DEFAULT 'media',
    status VARCHAR(30) NOT NULL DEFAULT 'aberto',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orcamentos_base (
    id SERIAL PRIMARY KEY,
    obra_id INTEGER NOT NULL,
    versao INTEGER NOT NULL DEFAULT 1,
    descricao TEXT NULL,
    valor_total NUMERIC(14, 2) NOT NULL,
    data_aprovacao DATE NULL,
    aprovado_por_id INTEGER NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'vigente',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contas_pagar (
    id SERIAL PRIMARY KEY,
    fornecedor_id INTEGER NULL,
    ordem_compra_id INTEGER NULL,
    obra_id INTEGER NULL,
    descricao VARCHAR(180) NOT NULL,
    valor NUMERIC(14, 2) NOT NULL,
    data_vencimento DATE NOT NULL,
    data_pagamento DATE NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'em_aberto',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contas_receber (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NULL,
    contrato_id INTEGER NULL,
    medicao_id INTEGER NULL,
    descricao VARCHAR(180) NOT NULL,
    valor NUMERIC(14, 2) NOT NULL,
    data_vencimento DATE NOT NULL,
    data_recebimento DATE NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'em_aberto',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS insumos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(160) NOT NULL,
    descricao TEXT NULL,
    unidade_medida VARCHAR(20) NOT NULL DEFAULT 'un',
    quantidade_atual NUMERIC(14, 3) NOT NULL DEFAULT 0,
    estoque_minimo NUMERIC(14, 3) NOT NULL DEFAULT 0,
    valor_unitario NUMERIC(14, 2) NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'ativo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS movimentacoes_estoque (
    id SERIAL PRIMARY KEY,
    insumo_id INTEGER NOT NULL,
    obra_id INTEGER NULL,
    tipo VARCHAR(20) NOT NULL,
    quantidade NUMERIC(14, 3) NOT NULL,
    data_movimentacao DATE NULL,
    observacao TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS fornecedores (
    id SERIAL PRIMARY KEY,
    razao_social VARCHAR(180) NOT NULL,
    nome_fantasia VARCHAR(180) NULL,
    cnpj VARCHAR(20) NULL,
    email VARCHAR(180) NULL,
    telefone VARCHAR(30) NULL,
    endereco TEXT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'ativo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cotacoes (
    id SERIAL PRIMARY KEY,
    fornecedor_id INTEGER NOT NULL,
    obra_id INTEGER NULL,
    descricao TEXT NULL,
    valor_total NUMERIC(14, 2) NULL,
    data_cotacao DATE NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'aberta',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ordens_compra (
    id SERIAL PRIMARY KEY,
    fornecedor_id INTEGER NOT NULL,
    obra_id INTEGER NULL,
    numero VARCHAR(60) NOT NULL,
    data_emissao DATE NULL,
    valor_total NUMERIC(14, 2) NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'aberta',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS itens_ordem_compra (
    id SERIAL PRIMARY KEY,
    ordem_compra_id INTEGER NOT NULL,
    insumo_id INTEGER NULL,
    descricao VARCHAR(180) NOT NULL,
    quantidade NUMERIC(14, 3) NOT NULL,
    valor_unitario NUMERIC(14, 2) NOT NULL,
    valor_total NUMERIC(14, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS frotas (
    id SERIAL PRIMARY KEY,
    identificacao VARCHAR(120) NOT NULL,
    tipo VARCHAR(80) NULL,
    placa VARCHAR(12) NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'disponivel',
    obra_id INTEGER NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cronogramas (
    id SERIAL PRIMARY KEY,
    obra_id INTEGER NOT NULL,
    atividade VARCHAR(180) NOT NULL,
    data_inicio DATE NULL,
    data_fim DATE NULL,
    percentual_concluido NUMERIC(5, 2) NOT NULL DEFAULT 0,
    status VARCHAR(30) NOT NULL DEFAULT 'planejado',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS folha_pagamento (
    id SERIAL PRIMARY KEY,
    funcionario_id INTEGER NOT NULL,
    competencia VARCHAR(7) NOT NULL,
    salario_bruto NUMERIC(14, 2) NOT NULL,
    descontos NUMERIC(14, 2) NOT NULL DEFAULT 0,
    salario_liquido NUMERIC(14, 2) NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'aberta',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS registro_ponto (
    id SERIAL PRIMARY KEY,
    funcionario_id INTEGER NOT NULL,
    data DATE NOT NULL,
    entrada TIME NULL,
    saida_intervalo TIME NULL,
    retorno_intervalo TIME NULL,
    saida TIME NULL,
    observacao TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE contratos ADD CONSTRAINT fk_contratos_cliente_id FOREIGN KEY (cliente_id) REFERENCES clientes(id);
ALTER TABLE agenda_visitas ADD CONSTRAINT fk_agenda_visitas_cliente_id FOREIGN KEY (cliente_id) REFERENCES clientes(id);
ALTER TABLE agenda_visitas ADD CONSTRAINT fk_agenda_visitas_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id);
ALTER TABLE projetos ADD CONSTRAINT fk_projetos_contrato_id FOREIGN KEY (contrato_id) REFERENCES contratos(id);
ALTER TABLE projetos ADD CONSTRAINT fk_projetos_responsavel_id FOREIGN KEY (responsavel_id) REFERENCES funcionarios(id);
ALTER TABLE revisoes_projeto ADD CONSTRAINT fk_revisoes_projeto_projeto_id FOREIGN KEY (projeto_id) REFERENCES projetos(id);
ALTER TABLE revisoes_projeto ADD CONSTRAINT fk_revisoes_projeto_responsavel_id FOREIGN KEY (responsavel_id) REFERENCES funcionarios(id);
ALTER TABLE obras ADD CONSTRAINT fk_obras_contrato_id FOREIGN KEY (contrato_id) REFERENCES contratos(id);
ALTER TABLE obras ADD CONSTRAINT fk_obras_projeto_id FOREIGN KEY (projeto_id) REFERENCES projetos(id);
ALTER TABLE obras ADD CONSTRAINT fk_obras_responsavel_id FOREIGN KEY (responsavel_id) REFERENCES funcionarios(id);
ALTER TABLE diarios_obra ADD CONSTRAINT fk_diarios_obra_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE diarios_obra ADD CONSTRAINT fk_diarios_obra_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id);
ALTER TABLE medicoes ADD CONSTRAINT fk_medicoes_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE medicoes ADD CONSTRAINT fk_medicoes_contrato_id FOREIGN KEY (contrato_id) REFERENCES contratos(id);
ALTER TABLE chamados_tecnicos ADD CONSTRAINT fk_chamados_tecnicos_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE chamados_tecnicos ADD CONSTRAINT fk_chamados_tecnicos_solicitante_id FOREIGN KEY (solicitante_id) REFERENCES funcionarios(id);
ALTER TABLE orcamentos_base ADD CONSTRAINT fk_orcamentos_base_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE orcamentos_base ADD CONSTRAINT fk_orcamentos_base_aprovado_por_id FOREIGN KEY (aprovado_por_id) REFERENCES funcionarios(id);
ALTER TABLE contas_pagar ADD CONSTRAINT fk_contas_pagar_fornecedor_id FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id);
ALTER TABLE contas_pagar ADD CONSTRAINT fk_contas_pagar_ordem_compra_id FOREIGN KEY (ordem_compra_id) REFERENCES ordens_compra(id);
ALTER TABLE contas_pagar ADD CONSTRAINT fk_contas_pagar_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE contas_receber ADD CONSTRAINT fk_contas_receber_cliente_id FOREIGN KEY (cliente_id) REFERENCES clientes(id);
ALTER TABLE contas_receber ADD CONSTRAINT fk_contas_receber_contrato_id FOREIGN KEY (contrato_id) REFERENCES contratos(id);
ALTER TABLE contas_receber ADD CONSTRAINT fk_contas_receber_medicao_id FOREIGN KEY (medicao_id) REFERENCES medicoes(id);
ALTER TABLE movimentacoes_estoque ADD CONSTRAINT fk_movimentacoes_estoque_insumo_id FOREIGN KEY (insumo_id) REFERENCES insumos(id);
ALTER TABLE movimentacoes_estoque ADD CONSTRAINT fk_movimentacoes_estoque_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE cotacoes ADD CONSTRAINT fk_cotacoes_fornecedor_id FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id);
ALTER TABLE cotacoes ADD CONSTRAINT fk_cotacoes_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE ordens_compra ADD CONSTRAINT fk_ordens_compra_fornecedor_id FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id);
ALTER TABLE ordens_compra ADD CONSTRAINT fk_ordens_compra_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE itens_ordem_compra ADD CONSTRAINT fk_itens_ordem_compra_ordem_compra_id FOREIGN KEY (ordem_compra_id) REFERENCES ordens_compra(id);
ALTER TABLE itens_ordem_compra ADD CONSTRAINT fk_itens_ordem_compra_insumo_id FOREIGN KEY (insumo_id) REFERENCES insumos(id);
ALTER TABLE frotas ADD CONSTRAINT fk_frotas_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE cronogramas ADD CONSTRAINT fk_cronogramas_obra_id FOREIGN KEY (obra_id) REFERENCES obras(id);
ALTER TABLE folha_pagamento ADD CONSTRAINT fk_folha_pagamento_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id);
ALTER TABLE registro_ponto ADD CONSTRAINT fk_registro_ponto_funcionario_id FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id);
