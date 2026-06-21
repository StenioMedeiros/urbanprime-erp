        INSERT INTO perfis (nome, descricao, nivel_acesso, ativo)
        VALUES
            ('administrador', 'Acesso total ao ERP UrbanPrime', 100, true),
            ('financeiro', 'Operacao financeira', 70, true),
            ('engenharia', 'Projetos e obras', 60, true),
            ('compras', 'Compras e fornecedores', 50, true),
            ('rh', 'Recursos humanos', 50, true)
        ON CONFLICT (nome) DO NOTHING;

        INSERT INTO permissoes (modulo, acao, descricao)
        VALUES
        ('comercial', 'visualizar', 'Permite visualizar em comercial'),
('comercial', 'criar', 'Permite criar em comercial'),
('comercial', 'editar', 'Permite editar em comercial'),
('comercial', 'excluir', 'Permite excluir em comercial'),
('comercial', 'aprovar', 'Permite aprovar em comercial'),
('comercial', 'cancelar', 'Permite cancelar em comercial'),
('engenharia', 'visualizar', 'Permite visualizar em engenharia'),
('engenharia', 'criar', 'Permite criar em engenharia'),
('engenharia', 'editar', 'Permite editar em engenharia'),
('engenharia', 'excluir', 'Permite excluir em engenharia'),
('engenharia', 'aprovar', 'Permite aprovar em engenharia'),
('engenharia', 'cancelar', 'Permite cancelar em engenharia'),
('obras', 'visualizar', 'Permite visualizar em obras'),
('obras', 'criar', 'Permite criar em obras'),
('obras', 'editar', 'Permite editar em obras'),
('obras', 'excluir', 'Permite excluir em obras'),
('obras', 'aprovar', 'Permite aprovar em obras'),
('obras', 'cancelar', 'Permite cancelar em obras'),
('financeiro', 'visualizar', 'Permite visualizar em financeiro'),
('financeiro', 'criar', 'Permite criar em financeiro'),
('financeiro', 'editar', 'Permite editar em financeiro'),
('financeiro', 'excluir', 'Permite excluir em financeiro'),
('financeiro', 'aprovar', 'Permite aprovar em financeiro'),
('financeiro', 'cancelar', 'Permite cancelar em financeiro'),
('rh', 'visualizar', 'Permite visualizar em rh'),
('rh', 'criar', 'Permite criar em rh'),
('rh', 'editar', 'Permite editar em rh'),
('rh', 'excluir', 'Permite excluir em rh'),
('rh', 'aprovar', 'Permite aprovar em rh'),
('rh', 'cancelar', 'Permite cancelar em rh'),
('estoque', 'visualizar', 'Permite visualizar em estoque'),
('estoque', 'criar', 'Permite criar em estoque'),
('estoque', 'editar', 'Permite editar em estoque'),
('estoque', 'excluir', 'Permite excluir em estoque'),
('estoque', 'aprovar', 'Permite aprovar em estoque'),
('estoque', 'cancelar', 'Permite cancelar em estoque'),
('compras', 'visualizar', 'Permite visualizar em compras'),
('compras', 'criar', 'Permite criar em compras'),
('compras', 'editar', 'Permite editar em compras'),
('compras', 'excluir', 'Permite excluir em compras'),
('compras', 'aprovar', 'Permite aprovar em compras'),
('compras', 'cancelar', 'Permite cancelar em compras'),
('planejamento', 'visualizar', 'Permite visualizar em planejamento'),
('planejamento', 'criar', 'Permite criar em planejamento'),
('planejamento', 'editar', 'Permite editar em planejamento'),
('planejamento', 'excluir', 'Permite excluir em planejamento'),
('planejamento', 'aprovar', 'Permite aprovar em planejamento'),
('planejamento', 'cancelar', 'Permite cancelar em planejamento'),
('auth', 'visualizar', 'Permite visualizar em auth'),
('auth', 'criar', 'Permite criar em auth'),
('auth', 'editar', 'Permite editar em auth'),
('auth', 'excluir', 'Permite excluir em auth'),
('auth', 'aprovar', 'Permite aprovar em auth'),
('auth', 'cancelar', 'Permite cancelar em auth'),
('usuarios', 'visualizar', 'Permite visualizar em usuarios'),
('usuarios', 'criar', 'Permite criar em usuarios'),
('usuarios', 'editar', 'Permite editar em usuarios'),
('usuarios', 'excluir', 'Permite excluir em usuarios'),
('usuarios', 'aprovar', 'Permite aprovar em usuarios'),
('usuarios', 'cancelar', 'Permite cancelar em usuarios'),
('perfis', 'visualizar', 'Permite visualizar em perfis'),
('perfis', 'criar', 'Permite criar em perfis'),
('perfis', 'editar', 'Permite editar em perfis'),
('perfis', 'excluir', 'Permite excluir em perfis'),
('perfis', 'aprovar', 'Permite aprovar em perfis'),
('perfis', 'cancelar', 'Permite cancelar em perfis'),
('auditoria', 'visualizar', 'Permite visualizar em auditoria'),
('auditoria', 'criar', 'Permite criar em auditoria'),
('auditoria', 'editar', 'Permite editar em auditoria'),
('auditoria', 'excluir', 'Permite excluir em auditoria'),
('auditoria', 'aprovar', 'Permite aprovar em auditoria'),
('auditoria', 'cancelar', 'Permite cancelar em auditoria')
        ON CONFLICT (modulo, acao) DO NOTHING;

        INSERT INTO perfil_permissao (perfil_id, permissao_id)
        SELECT p.id, pe.id FROM perfis p CROSS JOIN permissoes pe
        WHERE p.nome = 'administrador'
        AND NOT EXISTS (
            SELECT 1 FROM perfil_permissao pp WHERE pp.perfil_id = p.id AND pp.permissao_id = pe.id
        );

        INSERT INTO funcionarios (nome, email_corporativo, cargo, setor, status)
        VALUES ('Administrador UrbanPrime', 'admin@urbanprime.com', 'Administrador do Sistema', 'administrativo', 'ativo')
        ON CONFLICT (email_corporativo) DO NOTHING;

        INSERT INTO usuarios (funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, data_criacao)
SELECT f.id, 'admin', 'admin@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, CURRENT_TIMESTAMP
        FROM funcionarios f
        WHERE f.email_corporativo = 'admin@urbanprime.com'
        AND NOT EXISTS (SELECT 1 FROM usuarios u WHERE u.username = 'admin');

        INSERT INTO usuario_perfil (usuario_id, perfil_id)
        SELECT u.id, p.id FROM usuarios u, perfis p
        WHERE u.username = 'admin' AND p.nome = 'administrador'
        AND NOT EXISTS (
            SELECT 1 FROM usuario_perfil up WHERE up.usuario_id = u.id AND up.perfil_id = p.id
        );
