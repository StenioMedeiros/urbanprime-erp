--
-- PostgreSQL database dump
--

\restrict kEnrZ1dLv3HQOEk7klLjRNlyjZ1tNceI9xCh8dnetOuQktOD6kPV77QjasNVjma

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

--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (2, 'Família Almeida', 'juridica', '90.000.000/0001-01', 'contato.cliente01@exemplo.com', '(11) 3100-0001', 'Rua Doutor José Mariano, 120 - Heliópolis', 'Garanhuns', 'PE', '55291-001', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (3, 'Agreste Distribuidora', 'juridica', '90.000.000/0001-02', 'contato.cliente02@exemplo.com', '(11) 3100-0002', 'Distrito Industrial de Garanhuns, lote 18', 'Garanhuns', 'PE', '55292-002', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (4, 'Clínica Santa Luzia', 'juridica', '90.000.000/0001-03', 'contato.cliente03@exemplo.com', '(11) 3100-0003', 'Avenida Rui Barbosa, 640 - Heliópolis', 'Garanhuns', 'PE', '55293-003', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (5, 'Grupo Sete Colinas', 'juridica', '90.000.000/0001-04', 'contato.cliente04@exemplo.com', '(11) 3100-0004', 'Rua São Vicente, 310 - Centro', 'Garanhuns', 'PE', '55294-004', 'inativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (6, 'Comercial Rui Barbosa', 'juridica', '90.000.000/0001-05', 'contato.cliente05@exemplo.com', '(11) 3100-0005', 'Avenida Rui Barbosa, 980 - Heliópolis', 'Garanhuns', 'PE', '55295-005', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (7, 'Colégio Sementinha', 'juridica', '90.000.000/0001-06', 'contato.cliente06@exemplo.com', '(11) 3100-0006', 'Rua Melo Peixoto, 85 - Boa Vista', 'Garanhuns', 'PE', '55296-006', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (8, 'Residencial Parque das Acácias', 'juridica', '90.000.000/0001-07', 'contato.cliente07@exemplo.com', '(11) 3100-0007', 'Avenida Caruaru, 1450 - São José', 'Garanhuns', 'PE', '55297-007', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (9, 'Hotel Encantos do Agreste', 'juridica', '90.000.000/0001-08', 'contato.cliente08@exemplo.com', '(11) 3100-0008', 'Praça Souto Filho, 22 - Centro', 'Garanhuns', 'PE', '55298-008', 'inativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (10, 'Laticínios Serra Branca', 'juridica', '90.000.000/0001-09', 'contato.cliente09@exemplo.com', '(11) 3100-0009', 'Rodovia BR-423, km 94 - Zona Rural', 'Garanhuns', 'PE', '55299-009', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (11, 'Família Nogueira', 'juridica', '90.000.000/0001-10', 'contato.cliente10@exemplo.com', '(11) 3100-0010', 'Sítio Vale Verde - Zona Rural', 'Garanhuns', 'PE', '55290-010', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (12, 'Centro Empresarial Heliópolis', 'juridica', '90.000.000/0001-11', 'contato.cliente11@exemplo.com', '(11) 3100-0011', 'Rua Treze de Maio, 455 - Heliópolis', 'Garanhuns', 'PE', '55291-011', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (13, 'Instituto Educacional Boa Vista', 'juridica', '90.000.000/0001-12', 'contato.cliente12@exemplo.com', '(11) 3100-0012', 'Rua Antônio Cesário, 190 - Boa Vista', 'Garanhuns', 'PE', '55292-012', 'inativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.clientes (id, nome, tipo_pessoa, cpf_cnpj, email, telefone, endereco, cidade, estado, cep, status, created_at, updated_at) VALUES (1, 'Mercado São Cristóvão Ltda.', 'juridica', '90.000.013/0001-01', 'contato@mercadosaocristovao.exemplo', '(87) 3761-1300', 'Rua São Cristóvão, 310 - Boa Vista', 'Garanhuns', 'PE', '55292-310', 'ativo', '2026-06-20 04:20:24.436069', '2026-08-05 15:48:15.755339');


--
-- Data for Name: contratos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (2, 2, 'UP-2026-001', 'Contrato para construção de residência em heliópolis.', 487500.00, '2026-02-04', '2026-04-05', '2027-06-08', 'ativo', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (3, 3, 'UP-2026-002', 'Contrato para construção de galpão logístico.', 525000.00, '2026-02-05', '2026-04-06', '2027-06-18', 'em_aberto', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (4, 4, 'UP-2026-003', 'Contrato para reforma e ampliação de clínica.', 562500.00, '2026-02-06', '2026-04-07', '2027-06-28', 'concluido', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (5, 5, 'UP-2026-004', 'Contrato para construção do residencial sete colinas.', 600000.00, '2026-02-07', '2026-04-08', '2027-07-08', 'ativo', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (6, 6, 'UP-2026-005', 'Contrato para construção de centro comercial.', 637500.00, '2026-02-08', '2026-04-09', '2027-07-18', 'em_aberto', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (7, 7, 'UP-2026-006', 'Contrato para ampliação de escola particular.', 675000.00, '2026-02-09', '2026-04-10', '2027-07-28', 'concluido', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (8, 8, 'UP-2026-007', 'Contrato para infraestrutura do parque das acácias.', 712500.00, '2026-02-10', '2026-04-11', '2027-08-07', 'ativo', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (9, 9, 'UP-2026-008', 'Contrato para reforma do hotel encantos do agreste.', 750000.00, '2026-02-11', '2026-04-12', '2027-08-17', 'em_aberto', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (10, 10, 'UP-2026-009', 'Contrato para construção de unidade agroindustrial.', 787500.00, '2026-02-12', '2026-04-13', '2027-08-27', 'concluido', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (11, 11, 'UP-2026-010', 'Contrato para construção de casa de campo.', 825000.00, '2026-02-13', '2026-04-14', '2027-09-06', 'ativo', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (12, 12, 'UP-2026-011', 'Contrato para construção do centro empresarial heliópolis.', 862500.00, '2026-02-14', '2026-04-15', '2027-09-16', 'em_aberto', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (13, 13, 'UP-2026-012', 'Contrato para construção da creche escola boa vista.', 900000.00, '2026-02-15', '2026-04-16', '2027-09-26', 'concluido', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.contratos (id, cliente_id, numero_contrato, descricao, valor_total, data_assinatura, data_inicio, data_fim, status, arquivo_contrato, created_at, updated_at) VALUES (1, 1, 'UP-2026-013', 'Contrato para reforma e ampliação do Mercado São Cristóvão.', 150000.00, '2026-06-15', '2026-06-20', '2026-12-20', 'ativo', NULL, '2026-06-20 04:20:24.446482', '2026-08-05 15:48:15.755339');


--
-- Data for Name: funcionarios; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (1, 'Administrador UrbanPrime', NULL, NULL, NULL, 'admin@urbanprime.com', NULL, 'Administrador do Sistema', 'administrativo', NULL, NULL, NULL, 'ativo', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (6, 'Ana Paula Rodrigues', '90000000001', 'DEMORG00001', '1983-02-06', 'ana.rodrigues@urbanprime.com', '(11) 99000-0001', 'Engenheira civil', 'engenharia', '2022-02-01', NULL, 3925.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (7, 'Bruno Henrique Alves', '90000000002', 'DEMORG00002', '1984-03-07', 'bruno.alves@urbanprime.com', '(11) 99000-0002', 'Mestre de obras', 'obras', '2022-03-01', NULL, 4350.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (8, 'Camila Ferreira Melo', '90000000003', 'DEMORG00003', '1985-04-08', 'camila.melo@urbanprime.com', '(11) 99000-0003', 'Analista financeira', 'financeiro', '2022-04-01', NULL, 4775.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (9, 'Diego Moura Cavalcanti', '90000000004', 'DEMORG00004', '1986-05-09', 'diego.cavalcanti@urbanprime.com', '(11) 99000-0004', 'Analista de compras', 'compras', '2022-05-01', NULL, 5200.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (10, 'Edson José da Silva', '90000000005', 'DEMORG00005', '1987-06-10', 'edson.silva@urbanprime.com', '(11) 99000-0005', 'Técnico de segurança', 'rh', '2022-06-01', NULL, 5625.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (11, 'Fernanda Lima Barros', '90000000006', 'DEMORG00006', '1988-07-11', 'fernanda.barros@urbanprime.com', '(11) 99000-0006', 'Arquiteta', 'engenharia', '2022-07-01', NULL, 6050.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (12, 'Gabriel Nunes Costa', '90000000007', 'DEMORG00007', '1989-08-12', 'gabriel.costa@urbanprime.com', '(11) 99000-0007', 'Encarregado de obras', 'obras', '2022-08-01', NULL, 6475.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (13, 'Helena Maria Souza', '90000000008', 'DEMORG00008', '1990-09-13', 'helena.souza@urbanprime.com', '(11) 99000-0008', 'Assistente administrativa', 'administrativo', '2022-09-01', NULL, 6900.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (14, 'Igor Matheus Ribeiro', '90000000009', 'DEMORG00009', '1991-10-14', 'igor.ribeiro@urbanprime.com', '(11) 99000-0009', 'Almoxarife', 'compras', '2022-10-01', NULL, 7325.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (15, 'Juliana Alves Monteiro', '90000000010', 'DEMORG00010', '1992-11-15', 'juliana.monteiro@urbanprime.com', '(11) 99000-0010', 'Coordenadora de projetos', 'engenharia', '2022-11-01', NULL, 7750.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (16, 'Lucas Vinícius Santos', '90000000011', 'DEMORG00011', '1993-12-16', 'lucas.santos@urbanprime.com', '(11) 99000-0011', 'Eletricista', 'obras', '2022-12-01', NULL, 8175.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (17, 'Mariana Bezerra Oliveira', '90000000012', 'DEMORG00012', '1994-01-17', 'mariana.oliveira@urbanprime.com', '(11) 99000-0012', 'Analista de RH', 'rh', '2022-01-01', NULL, 8600.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.funcionarios (id, nome, cpf, rg, data_nascimento, email_corporativo, telefone, cargo, setor, data_admissao, data_demissao, salario_base, status, created_at, updated_at) VALUES (4, 'Rafael Henrique Melo', '000.000.013-04', '13.000.004-PE', '1992-04-18', 'rafael.melo@urbanprime.com', '(87) 99913-0404', 'Engenheiro civil', 'engenharia', '2025-01-06', NULL, 9200.00, 'ativo', '2026-06-20 04:20:24.428857', '2026-08-05 15:48:15.755339');


--
-- Data for Name: projetos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (2, 2, 6, 'Residência unifamiliar em Heliópolis', 'Projeto executivo para construção de residência em heliópolis em Garanhuns.', 'residencial', '2026-05-04', '2026-12-01', NULL, 'em_elaboracao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (3, 3, 7, 'Galpão logístico do Distrito Industrial', 'Projeto executivo para construção de galpão logístico em Garanhuns.', 'industrial', '2026-05-04', '2026-12-02', NULL, 'em_revisao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (4, 4, 8, 'Modernização da Clínica Santa Luzia', 'Projeto executivo para reforma e ampliação de clínica em Garanhuns.', 'hospitalar', '2026-05-04', '2026-12-03', NULL, 'aprovado', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (5, 5, 9, 'Edifício Residencial Sete Colinas', 'Projeto executivo para construção do residencial sete colinas em Garanhuns.', 'residencial', '2026-05-04', '2026-12-04', NULL, 'em_elaboracao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (6, 6, 10, 'Centro Comercial Rui Barbosa', 'Projeto executivo para construção de centro comercial em Garanhuns.', 'comercial', '2026-05-04', '2026-12-05', NULL, 'em_revisao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (7, 7, 11, 'Ampliação do Colégio Sementinha', 'Projeto executivo para ampliação de escola particular em Garanhuns.', 'educacional', '2026-05-04', '2026-12-06', NULL, 'aprovado', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (8, 8, 12, 'Condomínio Parque das Acácias', 'Projeto executivo para infraestrutura do parque das acácias em Garanhuns.', 'residencial', '2026-05-04', '2026-12-07', NULL, 'em_elaboracao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (9, 9, 13, 'Revitalização do Hotel Encantos', 'Projeto executivo para reforma do hotel encantos do agreste em Garanhuns.', 'hoteleiro', '2026-05-04', '2026-12-08', NULL, 'em_revisao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (10, 10, 14, 'Unidade Agroindustrial Serra Branca', 'Projeto executivo para construção de unidade agroindustrial em Garanhuns.', 'industrial', '2026-05-04', '2026-12-09', NULL, 'aprovado', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (11, 11, 15, 'Casa de campo Vale Verde', 'Projeto executivo para construção de casa de campo em Garanhuns.', 'residencial', '2026-05-04', '2026-12-10', NULL, 'em_elaboracao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (12, 12, 16, 'Centro Empresarial Heliópolis', 'Projeto executivo para construção do centro empresarial heliópolis em Garanhuns.', 'comercial', '2026-05-04', '2026-12-11', NULL, 'em_revisao', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (13, 13, 17, 'Creche Escola Boa Vista', 'Projeto executivo para construção da creche escola boa vista em Garanhuns.', 'educacional', '2026-05-04', '2026-12-12', NULL, 'aprovado', NULL, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.projetos (id, contrato_id, responsavel_id, nome, descricao, tipo_projeto, data_inicio, data_previsao_entrega, data_entrega, status, arquivo_projeto, created_at, updated_at) VALUES (1, 1, 4, 'Reforma do Mercado São Cristóvão', 'Projeto executivo para reforma e ampliação comercial em Garanhuns.', 'comercial', '2026-06-20', '2026-11-30', NULL, 'em_elaboracao', NULL, '2026-06-20 04:20:24.457554', '2026-08-05 15:48:15.755339');


--
-- Data for Name: obras; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (2, 2, 2, 'Construção de residência em Heliópolis', 'Construção de residência em Heliópolis, localizada em Garanhuns - PE.', 'Rua Doutor José Mariano, 120 - Heliópolis', 'Garanhuns', 'PE', '55291-101', 6, '2026-06-02', '2027-03-31', NULL, 'planejada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 7.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (3, 3, 3, 'Construção de galpão logístico', 'Construção de galpão logístico, localizada em Garanhuns - PE.', 'Distrito Industrial de Garanhuns, lote 18', 'Garanhuns', 'PE', '55292-102', 7, '2026-06-01', '2027-04-01', NULL, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 51.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (4, 4, 4, 'Reforma e ampliação de clínica', 'Reforma e ampliação de clínica, localizada em Garanhuns - PE.', 'Avenida Rui Barbosa, 640 - Heliópolis', 'Garanhuns', 'PE', '55293-103', 8, '2026-05-31', '2027-04-02', NULL, 'concluida', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (13, 13, 13, 'Construção da Creche Escola Boa Vista', 'Construção da Creche Escola Boa Vista, localizada em Garanhuns - PE.', 'Rua Antônio Cesário, 190 - Boa Vista', 'Garanhuns', 'PE', '55292-112', 17, '2026-05-22', '2027-04-11', NULL, 'concluida', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 0.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (6, 6, 6, 'Construção de centro comercial', 'Construção de centro comercial, localizada em Garanhuns - PE.', 'Avenida Rui Barbosa, 980 - Heliópolis', 'Garanhuns', 'PE', '55295-105', 10, '2026-05-29', '2027-04-04', NULL, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 60.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (7, 7, 7, 'Ampliação de escola particular', 'Ampliação de escola particular, localizada em Garanhuns - PE.', 'Rua Melo Peixoto, 85 - Boa Vista', 'Garanhuns', 'PE', '55296-106', 11, '2026-05-28', '2027-04-05', NULL, 'concluida', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (8, 8, 8, 'Infraestrutura do Parque das Acácias', 'Infraestrutura do Parque das Acácias, localizada em Garanhuns - PE.', 'Avenida Caruaru, 1450 - São José', 'Garanhuns', 'PE', '55297-107', 12, '2026-05-27', '2027-04-06', NULL, 'planejada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 13.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (9, 9, 9, 'Reforma do Hotel Encantos do Agreste', 'Reforma do Hotel Encantos do Agreste, localizada em Garanhuns - PE.', 'Praça Souto Filho, 22 - Centro', 'Garanhuns', 'PE', '55298-108', 13, '2026-05-26', '2027-04-07', NULL, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 69.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (10, 10, 10, 'Construção de unidade agroindustrial', 'Construção de unidade agroindustrial, localizada em Garanhuns - PE.', 'Rodovia BR-423, km 94 - Zona Rural', 'Garanhuns', 'PE', '55299-109', 14, '2026-05-25', '2027-04-08', NULL, 'concluida', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (11, 11, 11, 'Construção de casa de campo', 'Construção de casa de campo, localizada em Garanhuns - PE.', 'Sítio Vale Verde - Zona Rural', 'Garanhuns', 'PE', '55290-110', 15, '2026-05-24', '2027-04-09', NULL, 'planejada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 16.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (12, 12, 12, 'Construção do Centro Empresarial Heliópolis', 'Construção do Centro Empresarial Heliópolis, localizada em Garanhuns - PE.', 'Rua Treze de Maio, 455 - Heliópolis', 'Garanhuns', 'PE', '55291-111', 16, '2026-05-23', '2027-04-10', NULL, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 78.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (1, 1, 1, 'Reforma e ampliação do Mercado São Cristóvão', 'Reforma do salão de vendas, depósito e área administrativa.', 'Rua São Cristóvão, 310 - Boa Vista', 'Garanhuns', 'PE', '55292-310', 4, '2026-07-01', '2026-12-15', NULL, 'planejada', '2026-06-20 04:20:24.467108', '2026-08-05 15:48:15.755339', 6.00);
INSERT INTO public.obras (id, contrato_id, projeto_id, nome, descricao, endereco, cidade, estado, cep, responsavel_id, data_inicio, data_previsao_fim, data_fim, status, created_at, updated_at, percentual_fisico) VALUES (5, 5, 5, 'Construção do Residencial Sete Colinas', 'Construção do Residencial Sete Colinas, localizada em Garanhuns - PE.', 'Rua São Vicente, 310 - Centro', 'Garanhuns', 'PE', '55294-104', 9, '2026-05-30', '2027-04-03', NULL, 'planejada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 10.00);


--
-- Data for Name: frotas; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (1, 'FROTA-UP-01', 'caminhão', 'DMO1A01', 'em_uso', 2, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Mercedes-Benz', 'Atego', 2019, '2022-01-10', 113500.00, 975.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (2, 'FROTA-UP-02', 'utilitário', 'DMO2A02', 'disponivel', 3, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Volkswagen', 'Delivery', 2020, '2022-02-10', 132000.00, 1100.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (3, 'FROTA-UP-03', 'escavadeira', 'DMO3A03', 'em_uso', 4, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Caterpillar', '320', 2021, '2022-03-10', 150500.00, 1225.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (4, 'FROTA-UP-04', 'caminhão', 'DMO4A04', 'disponivel', 5, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'JCB', '3CX', 2022, '2022-04-10', 169000.00, 1350.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (5, 'FROTA-UP-05', 'utilitário', 'DMO5A05', 'em_uso', 6, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Mercedes-Benz', 'Atego', 2023, '2022-05-10', 187500.00, 1475.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (6, 'FROTA-UP-06', 'escavadeira', 'DMO6A06', 'disponivel', 7, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Volkswagen', 'Delivery', 2024, '2022-06-10', 206000.00, 1600.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (7, 'FROTA-UP-07', 'caminhão', 'DMO7A07', 'em_uso', 8, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Caterpillar', '320', 2018, '2022-07-10', 224500.00, 1725.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (8, 'FROTA-UP-08', 'utilitário', 'DMO8A08', 'disponivel', 9, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'JCB', '3CX', 2019, '2022-08-10', 243000.00, 1850.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (9, 'FROTA-UP-09', 'escavadeira', 'DMO9A09', 'em_uso', 10, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Mercedes-Benz', 'Atego', 2020, '2022-09-10', 261500.00, 1975.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (10, 'FROTA-UP-10', 'caminhão', 'DMO10A10', 'disponivel', 11, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Volkswagen', 'Delivery', 2021, '2022-10-10', 280000.00, 2100.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (11, 'FROTA-UP-11', 'utilitário', 'DMO11A11', 'em_uso', 12, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'Caterpillar', '320', 2022, '2022-11-10', 298500.00, 2225.00);
INSERT INTO public.frotas (id, identificacao, tipo, placa, status, obra_id, created_at, updated_at, marca, modelo, ano_fabricacao, data_aquisicao, valor_aquisicao, horimetro_atual) VALUES (12, 'FROTA-UP-12', 'escavadeira', 'DMO12A12', 'disponivel', 13, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 'JCB', '3CX', 2023, '2022-12-10', 317000.00, 2350.00);


--
-- Data for Name: abastecimentos_frota; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (1, 1, 1, 1, '2026-01-12', 68.000, 412.00, 1020.00, 'Abastecimento mensal de FROTA-UP-01 — 2026-01', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (2, 2, 2, 4, '2026-02-12', 71.000, 434.00, 1140.00, 'Abastecimento mensal de FROTA-UP-02 — 2026-02', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (3, 3, 3, 6, '2026-03-12', 74.000, 456.00, 1260.00, 'Abastecimento mensal de FROTA-UP-03 — 2026-03', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (4, 4, 4, 7, '2026-04-12', 77.000, 478.00, 1380.00, 'Abastecimento mensal de FROTA-UP-04 — 2026-04', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (5, 5, 5, 8, '2026-05-12', 80.000, 500.00, 1500.00, 'Abastecimento mensal de FROTA-UP-05 — 2026-05', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (6, 6, 6, 9, '2026-06-12', 83.000, 522.00, 1620.00, 'Abastecimento mensal de FROTA-UP-06 — 2026-06', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (7, 7, 7, 10, '2026-07-12', 86.000, 544.00, 1740.00, 'Abastecimento mensal de FROTA-UP-07 — 2026-07', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (8, 8, 8, 11, '2026-08-12', 89.000, 566.00, 1860.00, 'Abastecimento mensal de FROTA-UP-08 — 2026-08', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (9, 9, 9, 12, '2026-09-12', 92.000, 588.00, 1980.00, 'Abastecimento mensal de FROTA-UP-09 — 2026-09', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (10, 10, 10, 13, '2026-10-12', 95.000, 610.00, 2100.00, 'Abastecimento mensal de FROTA-UP-10 — 2026-10', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (11, 11, 11, 14, '2026-11-12', 98.000, 632.00, 2220.00, 'Abastecimento mensal de FROTA-UP-11 — 2026-11', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.abastecimentos_frota (id, frota_id, obra_id, responsavel_id, data_abastecimento, litros, valor_total, quilometragem_horimetro, observacao, created_at, updated_at) VALUES (12, 12, 12, 15, '2026-12-12', 101.000, 654.00, 2340.00, 'Abastecimento mensal de FROTA-UP-12 — 2026-12', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Data for Name: agenda_visitas; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (1, 2, 6, '2026-08-03', '10:00:00', 'Rua Doutor José Mariano, 120 - Heliópolis', 'Visita de acompanhamento: Construção de residência em Heliópolis.', 'agendada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (2, 3, 7, '2026-08-04', '11:00:00', 'Distrito Industrial de Garanhuns, lote 18', 'Visita de acompanhamento: Construção de galpão logístico.', 'realizada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (3, 4, 8, '2026-08-05', '12:00:00', 'Avenida Rui Barbosa, 640 - Heliópolis', 'Visita de acompanhamento: Reforma e ampliação de clínica.', 'cancelada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (4, 5, 9, '2026-08-06', '13:00:00', 'Rua São Vicente, 310 - Centro', 'Visita de acompanhamento: Construção do Residencial Sete Colinas.', 'agendada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (5, 6, 10, '2026-08-07', '14:00:00', 'Avenida Rui Barbosa, 980 - Heliópolis', 'Visita de acompanhamento: Construção de centro comercial.', 'realizada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (6, 7, 11, '2026-08-08', '15:00:00', 'Rua Melo Peixoto, 85 - Boa Vista', 'Visita de acompanhamento: Ampliação de escola particular.', 'cancelada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (7, 8, 12, '2026-08-09', '09:00:00', 'Avenida Caruaru, 1450 - São José', 'Visita de acompanhamento: Infraestrutura do Parque das Acácias.', 'agendada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (8, 9, 13, '2026-08-10', '10:00:00', 'Praça Souto Filho, 22 - Centro', 'Visita de acompanhamento: Reforma do Hotel Encantos do Agreste.', 'realizada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (9, 10, 14, '2026-08-11', '11:00:00', 'Rodovia BR-423, km 94 - Zona Rural', 'Visita de acompanhamento: Construção de unidade agroindustrial.', 'cancelada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (10, 11, 15, '2026-08-12', '12:00:00', 'Sítio Vale Verde - Zona Rural', 'Visita de acompanhamento: Construção de casa de campo.', 'agendada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (11, 12, 16, '2026-08-13', '13:00:00', 'Rua Treze de Maio, 455 - Heliópolis', 'Visita de acompanhamento: Construção do Centro Empresarial Heliópolis.', 'realizada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.agenda_visitas (id, cliente_id, funcionario_id, data_visita, horario, local_visita, observacoes, status, created_at, updated_at) VALUES (12, 13, 17, '2026-08-14', '14:00:00', 'Rua Antônio Cesário, 190 - Boa Vista', 'Visita de acompanhamento: Construção da Creche Escola Boa Vista.', 'cancelada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.alembic_version (version_num) VALUES ('0002_financial_analytics');


--
-- Data for Name: centros_custo; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (2, 'OBRA-002', 'Construção de residência em Heliópolis', 'obra', 2, 6, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (3, 'OBRA-003', 'Construção de galpão logístico', 'obra', 3, 7, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (4, 'OBRA-004', 'Reforma e ampliação de clínica', 'obra', 4, 8, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (5, 'OBRA-005', 'Construção do Residencial Sete Colinas', 'obra', 5, 9, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (6, 'OBRA-006', 'Construção de centro comercial', 'obra', 6, 10, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (7, 'OBRA-007', 'Ampliação de escola particular', 'obra', 7, 11, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (8, 'OBRA-008', 'Infraestrutura do Parque das Acácias', 'obra', 8, 12, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (9, 'OBRA-009', 'Reforma do Hotel Encantos do Agreste', 'obra', 9, 13, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (10, 'OBRA-010', 'Construção de unidade agroindustrial', 'obra', 10, 14, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (11, 'OBRA-011', 'Construção de casa de campo', 'obra', 11, 15, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (12, 'OBRA-012', 'Construção do Centro Empresarial Heliópolis', 'obra', 12, 16, 'Centro de custo exclusivo da obra.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (13, 'ADMIN-001', 'Administração central', 'administrativo', NULL, NULL, 'Custos gerais do escritório.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (14, 'FROTA-001', 'Frota e equipamentos', 'frota', NULL, NULL, 'Custos compartilhados da frota.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (15, 'ALMOX-001', 'Almoxarifado central', 'estoque', NULL, NULL, 'Custos de estoque e logística.', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (1, 'OBRA-001', 'Reforma e ampliação do Mercado São Cristóvão', 'obra', 1, 4, 'Centro de custo exclusivo da reforma comercial.', true, '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.centros_custo (id, codigo, nome, tipo, obra_id, responsavel_id, descricao, ativo, created_at, updated_at) VALUES (17, 'OBRA-013', 'Construção da Creche Escola Boa Vista', 'obra', 13, 17, 'Centro de custo exclusivo da obra.', true, '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');


--
-- Data for Name: alocacoes_funcionario_obra; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (1, 1, 1, 1, 'Administrador do Sistema — equipe 01', '2026-01-01', NULL, 0.00, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (2, 4, 2, 2, 'Analista — equipe 02', '2026-01-02', NULL, 0.00, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (3, 6, 3, 3, 'Engenheira civil — equipe 03', '2026-01-03', NULL, 17.84, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (4, 7, 4, 4, 'Mestre de obras — equipe 04', '2026-01-04', NULL, 19.77, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (5, 8, 5, 5, 'Analista financeira — equipe 05', '2026-01-05', NULL, 21.70, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (6, 9, 6, 6, 'Analista de compras — equipe 06', '2026-01-06', NULL, 23.64, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (7, 10, 7, 7, 'Técnico de segurança — equipe 07', '2026-01-07', NULL, 25.57, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (8, 11, 8, 8, 'Arquiteta — equipe 08', '2026-01-08', NULL, 27.50, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (9, 12, 9, 9, 'Encarregado de obras — equipe 09', '2026-01-09', NULL, 29.43, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (10, 13, 10, 10, 'Assistente administrativa — equipe 10', '2026-01-10', NULL, 31.36, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (11, 14, 11, 11, 'Almoxarife — equipe 11', '2026-01-11', NULL, 33.30, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.alocacoes_funcionario_obra (id, funcionario_id, obra_id, centro_custo_id, funcao, data_inicio, data_fim, custo_hora, ativo, created_at, updated_at) VALUES (12, 15, 12, 12, 'Coordenadora de projetos — equipe 12', '2026-01-12', NULL, 35.23, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Data for Name: categorias_financeiras; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (1, 'REC_MEDICOES', 'Receita de medições', 'receita', NULL, 'Categoria gerencial: receita de medições.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (2, 'REC_SERVICOS', 'Receita de serviços', 'receita', NULL, 'Categoria gerencial: receita de serviços.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (3, 'REC_OUTRAS', 'Outras receitas operacionais', 'receita', NULL, 'Categoria gerencial: outras receitas operacionais.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (4, 'DES_MATERIAIS', 'Materiais de construção', 'despesa', NULL, 'Categoria gerencial: materiais de construção.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (5, 'DES_MAO_OBRA', 'Mão de obra', 'despesa', NULL, 'Categoria gerencial: mão de obra.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (6, 'DES_EQUIPAMENTOS', 'Equipamentos e locações', 'despesa', NULL, 'Categoria gerencial: equipamentos e locações.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (7, 'DES_COMBUSTIVEL', 'Combustíveis', 'despesa', NULL, 'Categoria gerencial: combustíveis.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (8, 'DES_MANUTENCAO', 'Manutenção de frota', 'despesa', NULL, 'Categoria gerencial: manutenção de frota.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (9, 'DES_TERCEIROS', 'Serviços terceirizados', 'despesa', NULL, 'Categoria gerencial: serviços terceirizados.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (10, 'DES_IMPOSTOS', 'Impostos e retenções', 'despesa', NULL, 'Categoria gerencial: impostos e retenções.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (11, 'DES_ADMIN', 'Despesas administrativas', 'despesa', NULL, 'Categoria gerencial: despesas administrativas.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (12, 'DES_LOGISTICA', 'Fretes e logística', 'despesa', NULL, 'Categoria gerencial: fretes e logística.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (13, 'DES_SEGUROS', 'Seguros', 'despesa', NULL, 'Categoria gerencial: seguros.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.categorias_financeiras (id, codigo, nome, tipo, categoria_pai_id, descricao, contabilizavel, ativo, created_at, updated_at) VALUES (14, 'DES_FINANCEIRAS', 'Despesas financeiras', 'despesa', NULL, 'Categoria gerencial: despesas financeiras.', true, true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Data for Name: fornecedores; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (2, 'Casa do Cimento Garanhuns', 'Casa do Cimento Garanhuns', '91.000.000/0001-01', 'vendas01@fornecedor-agreste.com', '(11) 3200-0001', 'Garanhuns - Pernambuco, ponto comercial 1', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (3, 'Aço Forte do Agreste', 'Aço Forte do Agreste', '91.000.000/0001-02', 'vendas02@fornecedor-agreste.com', '(11) 3200-0002', 'Garanhuns - Pernambuco, ponto comercial 2', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (4, 'Madeireira Sete Colinas', 'Madeireira Sete Colinas', '91.000.000/0001-03', 'vendas03@fornecedor-agreste.com', '(11) 3200-0003', 'Garanhuns - Pernambuco, ponto comercial 3', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (5, 'Elétrica Heliópolis', 'Elétrica Heliópolis', '91.000.000/0001-04', 'vendas04@fornecedor-agreste.com', '(11) 3200-0004', 'Garanhuns - Pernambuco, ponto comercial 4', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (6, 'Hidrocenter Garanhuns', 'Hidrocenter Garanhuns', '91.000.000/0001-05', 'vendas05@fornecedor-agreste.com', '(11) 3200-0005', 'Garanhuns - Pernambuco, ponto comercial 5', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (7, 'Tintas Agreste', 'Tintas Agreste', '91.000.000/0001-06', 'vendas06@fornecedor-agreste.com', '(11) 3200-0006', 'Garanhuns - Pernambuco, ponto comercial 6', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (8, 'Cerâmica Vale do Mundaú', 'Cerâmica Vale do Mundaú', '91.000.000/0001-07', 'vendas07@fornecedor-agreste.com', '(11) 3200-0007', 'Garanhuns - Pernambuco, ponto comercial 7', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (9, 'Locadora Boa Vista', 'Locadora Boa Vista', '91.000.000/0001-08', 'vendas08@fornecedor-agreste.com', '(11) 3200-0008', 'Garanhuns - Pernambuco, ponto comercial 8', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (10, 'Ferragens Magano', 'Ferragens Magano', '91.000.000/0001-09', 'vendas09@fornecedor-agreste.com', '(11) 3200-0009', 'Garanhuns - Pernambuco, ponto comercial 9', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (11, 'Concreto Serra Branca', 'Concreto Serra Branca', '91.000.000/0001-10', 'vendas10@fornecedor-agreste.com', '(11) 3200-0010', 'Garanhuns - Pernambuco, ponto comercial 10', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (12, 'Vidraçaria São José', 'Vidraçaria São José', '91.000.000/0001-11', 'vendas11@fornecedor-agreste.com', '(11) 3200-0011', 'Garanhuns - Pernambuco, ponto comercial 11', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (13, 'Pernambuco EPI e Ferramentas', 'Pernambuco EPI e Ferramentas', '91.000.000/0001-12', 'vendas12@fornecedor-agreste.com', '(11) 3200-0012', 'Garanhuns - Pernambuco, ponto comercial 12', 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.fornecedores (id, razao_social, nome_fantasia, cnpj, email, telefone, endereco, status, created_at, updated_at) VALUES (1, 'Materiais São Cristóvão Ltda.', 'Depósito São Cristóvão', '90.000.014/0001-02', 'vendas@depositosaocristovao.exemplo', '(87) 3761-1310', 'Avenida Caruaru, 820 - São José, Garanhuns - PE', 'ativo', '2026-06-20 04:20:24.488001', '2026-08-05 15:48:15.755339');


--
-- Data for Name: cotacoes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (1, 2, 2, 'Cotação de materiais — Construção de residência em Heliópolis', 8700.00, '2026-07-31', 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (2, 3, 3, 'Cotação de materiais — Construção de galpão logístico', 9400.00, '2026-07-29', 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (3, 4, 4, 'Cotação de materiais — Reforma e ampliação de clínica', 10100.00, '2026-07-27', 'recusada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (4, 5, 5, 'Cotação de materiais — Construção do Residencial Sete Colinas', 10800.00, '2026-07-25', 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (5, 6, 6, 'Cotação de materiais — Construção de centro comercial', 11500.00, '2026-07-23', 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (6, 7, 7, 'Cotação de materiais — Ampliação de escola particular', 12200.00, '2026-07-21', 'recusada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (7, 8, 8, 'Cotação de materiais — Infraestrutura do Parque das Acácias', 12900.00, '2026-07-19', 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (8, 9, 9, 'Cotação de materiais — Reforma do Hotel Encantos do Agreste', 13600.00, '2026-07-17', 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (9, 10, 10, 'Cotação de materiais — Construção de unidade agroindustrial', 14300.00, '2026-07-15', 'recusada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (10, 11, 11, 'Cotação de materiais — Construção de casa de campo', 15000.00, '2026-07-13', 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (11, 12, 12, 'Cotação de materiais — Construção do Centro Empresarial Heliópolis', 15700.00, '2026-07-11', 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (12, 13, 13, 'Cotação de materiais — Construção da Creche Escola Boa Vista', 16400.00, '2026-07-09', 'recusada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.cotacoes (id, fornecedor_id, obra_id, descricao, valor_total, data_cotacao, status, created_at, updated_at) VALUES (14, 1, 1, 'Cotação de materiais — Reforma e ampliação do Mercado São Cristóvão', 500.00, '2026-06-20', 'aprovada', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');


--
-- Data for Name: ordens_compra; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (2, 2, 2, 'OC-2026-001', '2026-08-01', 5650.00, 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 1, '2026-08-03', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (3, 3, 3, 'OC-2026-002', '2026-07-31', 6300.00, 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 2, '2026-08-02', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (4, 4, 4, 'OC-2026-003', '2026-07-30', 6950.00, 'recebida', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 3, '2026-08-01', '2026-08-09');
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (5, 5, 5, 'OC-2026-004', '2026-07-29', 7600.00, 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 4, '2026-07-31', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (6, 6, 6, 'OC-2026-005', '2026-07-28', 8250.00, 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 5, '2026-07-30', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (7, 7, 7, 'OC-2026-006', '2026-07-27', 8900.00, 'recebida', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 6, '2026-07-29', '2026-08-06');
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (8, 8, 8, 'OC-2026-007', '2026-07-26', 9550.00, 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 7, '2026-07-28', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (9, 9, 9, 'OC-2026-008', '2026-07-25', 10200.00, 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 8, '2026-07-27', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (10, 10, 10, 'OC-2026-009', '2026-07-24', 10850.00, 'recebida', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 9, '2026-07-26', '2026-08-03');
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (11, 11, 11, 'OC-2026-010', '2026-07-23', 11500.00, 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 10, '2026-07-25', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (12, 12, 12, 'OC-2026-011', '2026-07-22', 12150.00, 'aprovada', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 11, '2026-07-24', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (1, 1, 1, 'OC-2026-013', '2026-06-20', 500.00, 'aprovada', '2026-06-20 04:20:24.503632', '2026-08-05 15:48:15.755339', 14, '2026-06-21', NULL);
INSERT INTO public.ordens_compra (id, fornecedor_id, obra_id, numero, data_emissao, valor_total, status, created_at, updated_at, cotacao_id, data_aprovacao, data_recebimento) VALUES (13, 13, 13, 'OC-2026-012', '2026-07-21', 12800.00, 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 12, '2026-07-23', NULL);


--
-- Data for Name: contas_pagar; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (13, 13, 13, 13, 'Pagamento de materiais — Construção da Creche Escola Boa Vista', 12800.00, '2026-09-07', '2026-07-21', 'pago', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 4, 17, '2026-09-07', 'DOC-PAG-2026-0013');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (2, 2, 2, 2, 'Pagamento de materiais — Construção de residência em Heliópolis', 5650.00, '2026-08-05', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 9, 2, '2026-08-05', 'DOC-PAG-2026-0002');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (3, 3, 3, 3, 'Pagamento de materiais — Construção de galpão logístico', 6300.00, '2026-08-08', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 6, 3, '2026-08-08', 'DOC-PAG-2026-0003');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (4, 4, 4, 4, 'Pagamento de materiais — Reforma e ampliação de clínica', 6950.00, '2026-08-11', '2026-07-30', 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 7, 4, '2026-08-11', 'DOC-PAG-2026-0004');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (5, 5, 5, 5, 'Pagamento de materiais — Construção do Residencial Sete Colinas', 7600.00, '2026-08-14', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 4, 5, '2026-08-14', 'DOC-PAG-2026-0005');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (6, 6, 6, 6, 'Pagamento de materiais — Construção de centro comercial', 8250.00, '2026-08-17', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 9, 6, '2026-08-17', 'DOC-PAG-2026-0006');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (7, 7, 7, 7, 'Pagamento de materiais — Ampliação de escola particular', 8900.00, '2026-08-20', '2026-07-27', 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 6, 7, '2026-08-20', 'DOC-PAG-2026-0007');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (8, 8, 8, 8, 'Pagamento de materiais — Infraestrutura do Parque das Acácias', 9550.00, '2026-08-23', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 7, 8, '2026-08-23', 'DOC-PAG-2026-0008');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (9, 9, 9, 9, 'Pagamento de materiais — Reforma do Hotel Encantos do Agreste', 10200.00, '2026-08-26', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 4, 9, '2026-08-26', 'DOC-PAG-2026-0009');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (10, 10, 10, 10, 'Pagamento de materiais — Construção de unidade agroindustrial', 10850.00, '2026-08-29', '2026-07-24', 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 9, 10, '2026-08-29', 'DOC-PAG-2026-0010');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (11, 11, 11, 11, 'Pagamento de materiais — Construção de casa de campo', 11500.00, '2026-09-01', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 6, 11, '2026-09-01', 'DOC-PAG-2026-0011');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (12, 12, 12, 12, 'Pagamento de materiais — Construção do Centro Empresarial Heliópolis', 12150.00, '2026-09-04', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 7, 12, '2026-09-04', 'DOC-PAG-2026-0012');
INSERT INTO public.contas_pagar (id, fornecedor_id, ordem_compra_id, obra_id, descricao, valor, data_vencimento, data_pagamento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, data_competencia, numero_documento) VALUES (1, 1, 1, 1, 'Compra de aditivo impermeabilizante — Mercado São Cristóvão', 500.00, '2026-06-20', NULL, 'em_aberto', '2026-06-20 04:20:24.51505', '2026-08-05 15:48:15.755339', 4, 1, '2026-06-20', 'DOC-PAG-2026-0001');


--
-- Data for Name: apropriacoes_custo; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (2, 2, 2, 9, 2, NULL, NULL, NULL, '2026-02', '2026-02-15', 'direto', 'Apropriação de custo 02 — obra Construção de residência em Heliópolis', 1.000, 5650.00, 5650.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (3, 3, 3, 6, 3, NULL, NULL, NULL, '2026-03', '2026-03-15', 'direto', 'Apropriação de custo 03 — obra Construção de galpão logístico', 1.000, 6300.00, 6300.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (4, 4, 4, 7, 4, NULL, NULL, NULL, '2026-04', '2026-04-15', 'direto', 'Apropriação de custo 04 — obra Reforma e ampliação de clínica', 1.000, 6950.00, 6950.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (5, 5, 5, 4, 5, NULL, NULL, NULL, '2026-05', '2026-05-15', 'direto', 'Apropriação de custo 05 — obra Construção do Residencial Sete Colinas', 1.000, 7600.00, 7600.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (6, 6, 6, 9, 6, NULL, NULL, NULL, '2026-06', '2026-06-15', 'direto', 'Apropriação de custo 06 — obra Construção de centro comercial', 1.000, 8250.00, 8250.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (7, 7, 7, 6, 7, NULL, NULL, NULL, '2026-07', '2026-07-15', 'direto', 'Apropriação de custo 07 — obra Ampliação de escola particular', 1.000, 8900.00, 8900.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (8, 8, 8, 7, 8, NULL, NULL, NULL, '2026-08', '2026-08-15', 'direto', 'Apropriação de custo 08 — obra Infraestrutura do Parque das Acácias', 1.000, 9550.00, 9550.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (9, 9, 9, 4, 9, NULL, NULL, NULL, '2026-09', '2026-09-15', 'direto', 'Apropriação de custo 09 — obra Reforma do Hotel Encantos do Agreste', 1.000, 10200.00, 10200.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (10, 10, 10, 9, 10, NULL, NULL, NULL, '2026-10', '2026-10-15', 'direto', 'Apropriação de custo 10 — obra Construção de unidade agroindustrial', 1.000, 10850.00, 10850.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (11, 11, 11, 6, 11, NULL, NULL, NULL, '2026-11', '2026-11-15', 'direto', 'Apropriação de custo 11 — obra Construção de casa de campo', 1.000, 11500.00, 11500.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (12, 12, 12, 7, 12, NULL, NULL, NULL, '2026-12', '2026-12-15', 'direto', 'Apropriação de custo 12 — obra Construção do Centro Empresarial Heliópolis', 1.000, 12150.00, 12150.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.apropriacoes_custo (id, obra_id, centro_custo_id, categoria_financeira_id, conta_pagar_id, ordem_compra_id, funcionario_id, frota_id, competencia, data_apropriacao, tipo_custo, descricao, quantidade, valor_unitario, valor_total, origem, created_at, updated_at) VALUES (1, 1, 1, 4, 1, NULL, NULL, NULL, '2026-01', '2026-01-15', 'direto', 'Apropriação de custo — Reforma do Mercado São Cristóvão', 1.000, 500.00, 500.00, 'conta_pagar', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');


--
-- Data for Name: chamados_tecnicos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (1, 2, 6, 'Verificação técnica — Construção de residência em Heliópolis', 'Verificação técnica demonstrativa da obra 1', 'baixa', 'aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (2, 3, 7, 'Verificação técnica — Construção de galpão logístico', 'Verificação técnica demonstrativa da obra 2', 'media', 'em_atendimento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (3, 4, 8, 'Verificação técnica — Reforma e ampliação de clínica', 'Verificação técnica demonstrativa da obra 3', 'alta', 'resolvido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (4, 5, 9, 'Verificação técnica — Construção do Residencial Sete Colinas', 'Verificação técnica demonstrativa da obra 4', 'critica', 'aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (5, 6, 10, 'Verificação técnica — Construção de centro comercial', 'Verificação técnica demonstrativa da obra 5', 'baixa', 'em_atendimento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (6, 7, 11, 'Verificação técnica — Ampliação de escola particular', 'Verificação técnica demonstrativa da obra 6', 'media', 'resolvido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (7, 8, 12, 'Verificação técnica — Infraestrutura do Parque das Acácias', 'Verificação técnica demonstrativa da obra 7', 'alta', 'aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (8, 9, 13, 'Verificação técnica — Reforma do Hotel Encantos do Agreste', 'Verificação técnica demonstrativa da obra 8', 'critica', 'em_atendimento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (9, 10, 14, 'Verificação técnica — Construção de unidade agroindustrial', 'Verificação técnica demonstrativa da obra 9', 'baixa', 'resolvido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (10, 11, 15, 'Verificação técnica — Construção de casa de campo', 'Verificação técnica demonstrativa da obra 10', 'media', 'aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (11, 12, 16, 'Verificação técnica — Construção do Centro Empresarial Heliópolis', 'Verificação técnica demonstrativa da obra 11', 'alta', 'em_atendimento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.chamados_tecnicos (id, obra_id, solicitante_id, titulo, descricao, prioridade, status, created_at, updated_at) VALUES (12, 13, 17, 'Verificação técnica — Construção da Creche Escola Boa Vista', 'Verificação técnica demonstrativa da obra 12', 'critica', 'resolvido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');


--
-- Data for Name: contas_bancarias; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (1, 'Banco do Brasil', '1234-5', '10001-1', 'corrente', 'Operacional', 25000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (2, 'Caixa Econômica Federal', '0067', '20002-2', 'corrente', 'Recebimentos de obras', 50000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (3, 'Santander', '4040', '30003-3', 'corrente', 'Folha de pagamento', 75000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (4, 'Sicredi', '2201', '40004-4', 'corrente', 'Reserva e investimentos', 100000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (5, 'Itaú', '1678', '50005-5', 'corrente', 'Recebimentos comerciais', 125000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (6, 'Bradesco', '3120', '60006-6', 'corrente', 'Pagamentos a fornecedores', 150000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (7, 'Nubank PJ', '0001', '70007-7', 'corrente', 'Despesas administrativas', 175000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (8, 'Banco do Nordeste', '0088', '80008-8', 'corrente', 'Financiamento de equipamentos', 200000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (9, 'Sicoob', '4410', '90009-9', 'corrente', 'Conta de obras', 225000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.contas_bancarias (id, banco, agencia, numero_conta, tipo_conta, descricao, saldo_inicial, data_saldo_inicial, ativo, created_at, updated_at) VALUES (10, 'Caixa interno', NULL, 'CAIXA-001', 'caixa', 'Pequenas despesas', 250000.00, '2026-01-01', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Data for Name: medicoes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (1, 2, 2, '2026-01', 37750.00, '2026-07-30', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (2, 3, 3, '2026-02', 40500.00, '2026-07-27', 'faturada', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (3, 4, 4, '2026-03', 43250.00, '2026-07-24', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (4, 5, 5, '2026-04', 46000.00, '2026-07-21', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (5, 6, 6, '2026-05', 48750.00, '2026-07-18', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (6, 7, 7, '2026-06', 51500.00, '2026-07-15', 'faturada', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (7, 8, 8, '2026-07', 54250.00, '2026-07-12', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (8, 9, 9, '2026-08', 57000.00, '2026-07-09', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (9, 10, 10, '2026-09', 59750.00, '2026-07-06', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (10, 11, 11, '2026-10', 62500.00, '2026-07-03', 'faturada', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (11, 12, 12, '2026-11', 65250.00, '2026-06-30', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');
INSERT INTO public.medicoes (id, obra_id, contrato_id, competencia, valor_medido, data_medicao, status, created_at, updated_at) VALUES (12, 13, 13, '2026-12', 68000.00, '2026-06-27', 'recebida', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339');


--
-- Data for Name: faturas; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (11, 12, 12, 12, 11, 'NF-UP-2026-0011', '2026-11-05', '2026-11', 65250.00, 1305.00, 1957.50, 61987.50, '2026-12-05', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (8, 9, 9, 9, 8, 'NF-UP-2026-0008', '2026-08-05', '2026-08', 57000.00, 1140.00, 1710.00, 54150.00, '2026-09-04', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (9, 10, 10, 10, 9, 'NF-UP-2026-0009', '2026-09-05', '2026-09', 59750.00, 1195.00, 1792.50, 56762.50, '2026-10-05', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (7, 8, 8, 8, 7, 'NF-UP-2026-0007', '2026-07-05', '2026-07', 54250.00, 1085.00, 1627.50, 51537.50, '2026-08-04', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (1, 2, 2, 2, 1, 'NF-UP-2026-0001', '2026-01-05', '2026-01', 37750.00, 755.00, 1132.50, 35862.50, '2026-02-04', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (5, 6, 6, 6, 5, 'NF-UP-2026-0005', '2026-05-05', '2026-05', 48750.00, 975.00, 1462.50, 46312.50, '2026-06-04', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (4, 5, 5, 5, 4, 'NF-UP-2026-0004', '2026-04-05', '2026-04', 46000.00, 920.00, 1380.00, 43700.00, '2026-05-05', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (12, 13, 13, 13, 12, 'NF-UP-2026-0012', '2026-12-05', '2026-12', 68000.00, 1360.00, 2040.00, 64600.00, '2027-01-04', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (3, 4, 4, 4, 3, 'NF-UP-2026-0003', '2026-03-05', '2026-03', 43250.00, 865.00, 1297.50, 41087.50, '2026-04-04', 'recebida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (2, 3, 3, 3, 2, 'NF-UP-2026-0002', '2026-02-05', '2026-02', 40500.00, 810.00, 1215.00, 38475.00, '2026-03-07', 'emitida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (6, 7, 7, 7, 6, 'NF-UP-2026-0006', '2026-06-05', '2026-06', 51500.00, 1030.00, 1545.00, 48925.00, '2026-07-05', 'emitida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.faturas (id, cliente_id, contrato_id, obra_id, medicao_id, numero_documento, data_emissao, competencia, valor_bruto, impostos, retencoes, valor_liquido, data_vencimento, status, observacao, created_at, updated_at) VALUES (10, 11, 11, 11, 10, 'NF-UP-2026-0010', '2026-10-05', '2026-10', 62500.00, 1250.00, 1875.00, 59375.00, '2026-11-04', 'emitida', 'Faturamento vinculado à medição da obra.', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');


--
-- Data for Name: contas_receber; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (1, 1, 1, NULL, 'Parcela contratual — Reforma do Mercado São Cristóvão', 1000.00, '2026-06-20', NULL, 'em_aberto', '2026-06-20 04:20:24.526549', '2026-08-05 15:48:15.755339', 2, 1, NULL, '2026-06-20', 'REC-UP-2026-0013');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (2, 2, 2, 1, 'Parcela de medição — Construção de residência em Heliópolis', 35862.50, '2026-08-06', '2026-01-20', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 1, 1, '2026-01-05', 'NF-UP-2026-0001');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (4, 4, 4, 3, 'Parcela de medição — Reforma e ampliação de clínica', 41087.50, '2026-08-14', '2026-03-20', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 3, 3, '2026-03-05', 'NF-UP-2026-0003');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (3, 3, 3, 2, 'Parcela de medição — Construção de galpão logístico', 38475.00, '2026-08-10', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 1, 2, 2, '2026-02-05', 'NF-UP-2026-0002');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (7, 7, 7, 6, 'Parcela de medição — Ampliação de escola particular', 48925.00, '2026-08-26', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 1, 6, 6, '2026-06-05', 'NF-UP-2026-0006');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (5, 5, 5, 4, 'Parcela de medição — Construção do Residencial Sete Colinas', 43700.00, '2026-08-18', '2026-07-29', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 4, 4, '2026-04-05', 'NF-UP-2026-0004');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (6, 6, 6, 5, 'Parcela de medição — Construção de centro comercial', 46312.50, '2026-08-22', '2026-05-20', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 5, 5, '2026-05-05', 'NF-UP-2026-0005');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (8, 8, 8, 7, 'Parcela de medição — Infraestrutura do Parque das Acácias', 51537.50, '2026-08-30', '2026-07-20', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 7, 7, '2026-07-05', 'NF-UP-2026-0007');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (9, 9, 9, 8, 'Parcela de medição — Reforma do Hotel Encantos do Agreste', 54150.00, '2026-09-03', '2026-07-25', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 8, 8, '2026-08-05', 'NF-UP-2026-0008');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (10, 10, 10, 9, 'Parcela de medição — Construção de unidade agroindustrial', 56762.50, '2026-09-07', '2026-09-20', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 9, 9, '2026-09-05', 'NF-UP-2026-0009');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (12, 12, 12, 11, 'Parcela de medição — Construção do Centro Empresarial Heliópolis', 61987.50, '2026-09-15', '2026-11-20', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 11, 11, '2026-11-05', 'NF-UP-2026-0011');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (13, 13, 13, 12, 'Parcela de medição — Construção da Creche Escola Boa Vista', 64600.00, '2026-09-19', '2026-07-21', 'recebido', '2026-08-02 01:16:25.25614', '2026-08-05 15:48:15.755339', 1, 12, 12, '2026-12-05', 'NF-UP-2026-0012');
INSERT INTO public.contas_receber (id, cliente_id, contrato_id, medicao_id, descricao, valor, data_vencimento, data_recebimento, status, created_at, updated_at, categoria_financeira_id, centro_custo_id, fatura_id, data_competencia, numero_documento) VALUES (11, 11, 11, 10, 'Parcela de medição — Construção de casa de campo', 59375.00, '2026-09-11', NULL, 'em_aberto', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 1, 10, 10, '2026-10-05', 'NF-UP-2026-0010');


--
-- Data for Name: cronogramas; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (1, 2, 'Etapa 01 — Construção de residência em Heliópolis', '2026-07-18', '2026-08-18', 8.00, 'planejado', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (2, 3, 'Etapa 02 — Construção de galpão logístico', '2026-07-18', '2026-08-19', 16.00, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (3, 4, 'Etapa 03 — Reforma e ampliação de clínica', '2026-07-18', '2026-08-20', 24.00, 'concluido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (4, 5, 'Etapa 04 — Construção do Residencial Sete Colinas', '2026-07-18', '2026-08-21', 32.00, 'planejado', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (5, 6, 'Etapa 05 — Construção de centro comercial', '2026-07-18', '2026-08-22', 40.00, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (6, 7, 'Etapa 06 — Ampliação de escola particular', '2026-07-18', '2026-08-23', 48.00, 'concluido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (7, 8, 'Etapa 07 — Infraestrutura do Parque das Acácias', '2026-07-18', '2026-08-24', 56.00, 'planejado', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (8, 9, 'Etapa 08 — Reforma do Hotel Encantos do Agreste', '2026-07-18', '2026-08-25', 64.00, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (9, 10, 'Etapa 09 — Construção de unidade agroindustrial', '2026-07-18', '2026-08-26', 72.00, 'concluido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (10, 11, 'Etapa 10 — Construção de casa de campo', '2026-07-18', '2026-08-27', 80.00, 'planejado', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (11, 12, 'Etapa 11 — Construção do Centro Empresarial Heliópolis', '2026-07-18', '2026-08-28', 88.00, 'em_andamento', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (12, 13, 'Etapa 12 — Construção da Creche Escola Boa Vista', '2026-07-18', '2026-08-29', 96.00, 'concluido', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614', 100.00);
INSERT INTO public.cronogramas (id, obra_id, atividade, data_inicio, data_fim, percentual_concluido, status, created_at, updated_at, peso_percentual) VALUES (14, 1, 'Mobilização e preparação do canteiro', '2026-07-01', '2026-07-15', 100.00, 'concluido', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339', 10.00);


--
-- Data for Name: diarios_obra; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (1, 2, 6, '2026-08-01', 'ensolarado', 'Execução e acompanhamento dos serviços de construção de residência em heliópolis', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (2, 3, 7, '2026-07-31', 'nublado', 'Execução e acompanhamento dos serviços de construção de galpão logístico', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (3, 4, 8, '2026-07-30', 'chuvoso', 'Execução e acompanhamento dos serviços de reforma e ampliação de clínica', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (4, 5, 9, '2026-07-29', 'ensolarado', 'Execução e acompanhamento dos serviços de construção do residencial sete colinas', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (5, 6, 10, '2026-07-28', 'nublado', 'Execução e acompanhamento dos serviços de construção de centro comercial', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (6, 7, 11, '2026-07-27', 'chuvoso', 'Execução e acompanhamento dos serviços de ampliação de escola particular', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (7, 8, 12, '2026-07-26', 'ensolarado', 'Execução e acompanhamento dos serviços de infraestrutura do parque das acácias', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (8, 9, 13, '2026-07-25', 'nublado', 'Execução e acompanhamento dos serviços de reforma do hotel encantos do agreste', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (9, 10, 14, '2026-07-24', 'chuvoso', 'Execução e acompanhamento dos serviços de construção de unidade agroindustrial', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (10, 11, 15, '2026-07-23', 'ensolarado', 'Execução e acompanhamento dos serviços de construção de casa de campo', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (11, 12, 16, '2026-07-22', 'nublado', 'Execução e acompanhamento dos serviços de construção do centro empresarial heliópolis', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (12, 13, 17, '2026-07-21', 'chuvoso', 'Execução e acompanhamento dos serviços de construção da creche escola boa vista', 'Operação normal, sem ocorrências críticas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.diarios_obra (id, obra_id, funcionario_id, data_registro, clima, atividades, ocorrencias, created_at, updated_at) VALUES (14, 1, 4, '2026-07-01', 'ensolarado', 'Mobilização da equipe e isolamento das áreas de intervenção.', 'Operação inicial sem ocorrências críticas.', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');


--
-- Data for Name: folha_pagamento; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (1, 6, '2025-01', 4800.00, 370.00, 4430.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (2, 7, '2025-02', 5100.00, 390.00, 4710.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (3, 8, '2025-03', 5400.00, 410.00, 4990.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (4, 9, '2025-04', 5700.00, 430.00, 5270.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (5, 10, '2025-05', 6000.00, 450.00, 5550.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (6, 11, '2025-06', 6300.00, 470.00, 5830.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (7, 12, '2025-07', 6600.00, 490.00, 6110.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (8, 13, '2025-08', 6900.00, 510.00, 6390.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (9, 14, '2025-09', 7200.00, 530.00, 6670.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (10, 15, '2025-10', 7500.00, 550.00, 6950.00, 'pago', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (11, 16, '2025-11', 7800.00, 570.00, 7230.00, 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.folha_pagamento (id, funcionario_id, competencia, salario_bruto, descontos, salario_liquido, status, created_at, updated_at) VALUES (12, 17, '2025-12', 8100.00, 590.00, 7510.00, 'aberta', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (2, 6, 'ana.rodrigues', 'ana.rodrigues@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-08-01 01:16:25.178945', '2026-04-03 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (3, 7, 'bruno.alves', 'bruno.alves@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-31 01:16:25.178945', '2026-04-02 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (4, 8, 'camila.melo', 'camila.melo@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-30 01:16:25.178945', '2026-04-01 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (5, 9, 'diego.cavalcanti', 'diego.cavalcanti@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-29 01:16:25.178945', '2026-03-31 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (6, 10, 'edson.silva', 'edson.silva@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-28 01:16:25.178945', '2026-03-30 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (7, 11, 'fernanda.barros', 'fernanda.barros@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-27 01:16:25.178945', '2026-03-29 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (8, 12, 'gabriel.costa', 'gabriel.costa@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-26 01:16:25.178945', '2026-03-28 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (9, 13, 'helena.souza', 'helena.souza@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-25 01:16:25.178945', '2026-03-27 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (10, 14, 'igor.ribeiro', 'igor.ribeiro@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-24 01:16:25.178945', '2026-03-26 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (11, 15, 'juliana.monteiro', 'juliana.monteiro@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-23 01:16:25.178945', '2026-03-25 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (12, 16, 'lucas.santos', 'lucas.santos@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-22 01:16:25.178945', '2026-03-24 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (13, 17, 'mariana.oliveira', 'mariana.oliveira@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-07-21 01:16:25.178945', '2026-03-23 01:16:25.178945', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.usuarios (id, funcionario_id, username, email, senha_hash, ativo, bloqueado, tentativas_login, ultimo_login, data_criacao, created_at, updated_at) VALUES (1, 1, 'admin', 'admin@urbanprime.com', '$2b$12$piATzKHrmrVlNKzZ/qai9.s9bANjv4sK6nDua/x1hAkOyYYnkWjPi', true, false, 0, '2026-08-10 20:00:21.726987', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367', '2026-08-10 20:00:21.26524');


--
-- Data for Name: historicos_status; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (2, 'obras', 2, NULL, 'planejada', '2026-02-01 00:00:00', 1, 'Situação inicial registrada para Construção de residência em Heliópolis', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (3, 'obras', 3, NULL, 'em_andamento', '2026-03-01 00:00:00', 1, 'Situação inicial registrada para Construção de galpão logístico', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (4, 'obras', 4, NULL, 'concluida', '2026-04-01 00:00:00', 1, 'Situação inicial registrada para Reforma e ampliação de clínica', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (5, 'obras', 5, NULL, 'planejada', '2026-05-01 00:00:00', 1, 'Situação inicial registrada para Construção do Residencial Sete Colinas', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (6, 'obras', 6, NULL, 'em_andamento', '2026-06-01 00:00:00', 1, 'Situação inicial registrada para Construção de centro comercial', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (7, 'obras', 7, NULL, 'concluida', '2026-07-01 00:00:00', 1, 'Situação inicial registrada para Ampliação de escola particular', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (8, 'obras', 8, NULL, 'planejada', '2026-08-01 00:00:00', 1, 'Situação inicial registrada para Infraestrutura do Parque das Acácias', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (9, 'obras', 9, NULL, 'em_andamento', '2026-09-01 00:00:00', 1, 'Situação inicial registrada para Reforma do Hotel Encantos do Agreste', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (10, 'obras', 10, NULL, 'concluida', '2026-10-01 00:00:00', 1, 'Situação inicial registrada para Construção de unidade agroindustrial', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (11, 'obras', 11, NULL, 'planejada', '2026-11-01 00:00:00', 1, 'Situação inicial registrada para Construção de casa de campo', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (12, 'obras', 12, NULL, 'em_andamento', '2026-12-01 00:00:00', 1, 'Situação inicial registrada para Construção do Centro Empresarial Heliópolis', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (1, 'obras', 1, NULL, 'planejada', '2026-01-01 00:00:00', 1, 'Situação inicial registrada para a Reforma do Mercado São Cristóvão', '2026-08-02 12:59:36.171538', '2026-08-05 15:48:15.755339');
INSERT INTO public.historicos_status (id, entidade, entidade_id, status_anterior, status_novo, data_alteracao, usuario_id, observacao, created_at, updated_at) VALUES (14, 'obras', 13, NULL, 'concluida', '2026-08-05 15:48:15.755339', NULL, 'Situação inicial registrada para Construção da Creche Escola Boa Vista', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');


--
-- Data for Name: insumos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (2, 'Cimento CP II 50 kg', 'Material de construção utilizado nas obras de Garanhuns (Cimento CP II 50 kg).', 'un', 115.000, 21.000, 12.50, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (3, 'Areia média lavada', 'Material de construção utilizado nas obras de Garanhuns (Areia média lavada).', 'kg', 130.000, 22.000, 25.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (4, 'Brita nº 1', 'Material de construção utilizado nas obras de Garanhuns (Brita nº 1).', 'm', 145.000, 23.000, 37.50, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (5, 'Bloco cerâmico 9x19x19', 'Material de construção utilizado nas obras de Garanhuns (Bloco cerâmico 9x19x19).', 'm²', 160.000, 24.000, 50.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (6, 'Vergalhão CA-50 10 mm', 'Material de construção utilizado nas obras de Garanhuns (Vergalhão CA-50 10 mm).', 'un', 175.000, 25.000, 62.50, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (7, 'Tijolo de oito furos', 'Material de construção utilizado nas obras de Garanhuns (Tijolo de oito furos).', 'kg', 190.000, 26.000, 75.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (8, 'Argamassa AC-II 20 kg', 'Material de construção utilizado nas obras de Garanhuns (Argamassa AC-II 20 kg).', 'm', 205.000, 27.000, 87.50, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (9, 'Tinta acrílica premium 18 L', 'Material de construção utilizado nas obras de Garanhuns (Tinta acrílica premium 18 L).', 'm²', 220.000, 28.000, 100.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (10, 'Cabo elétrico 2,5 mm²', 'Material de construção utilizado nas obras de Garanhuns (Cabo elétrico 2,5 mm²).', 'un', 235.000, 29.000, 112.50, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (11, 'Tubo PVC soldável 25 mm', 'Material de construção utilizado nas obras de Garanhuns (Tubo PVC soldável 25 mm).', 'kg', 250.000, 30.000, 125.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (12, 'Telha cerâmica colonial', 'Material de construção utilizado nas obras de Garanhuns (Telha cerâmica colonial).', 'm', 265.000, 31.000, 137.50, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (13, 'Piso porcelanato acetinado', 'Material de construção utilizado nas obras de Garanhuns (Piso porcelanato acetinado).', 'm²', 280.000, 32.000, 150.00, 'ativo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.insumos (id, nome, descricao, unidade_medida, quantidade_atual, estoque_minimo, valor_unitario, status, created_at, updated_at) VALUES (1, 'Aditivo impermeabilizante 18 L', 'Aditivo impermeabilizante para concretos e argamassas.', 'balde', 10.000, 2.000, 50.00, 'ativo', '2026-06-20 04:20:24.495719', '2026-08-05 15:48:15.755339');


--
-- Data for Name: orcamentos_base; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (2, 2, 1, 'Orçamento-base — Construção de residência em Heliópolis', 430000.00, '2026-05-24', 6, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (3, 3, 1, 'Orçamento-base — Construção de galpão logístico', 460000.00, '2026-05-24', 7, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (4, 4, 1, 'Orçamento-base — Reforma e ampliação de clínica', 490000.00, '2026-05-24', 8, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (5, 5, 1, 'Orçamento-base — Construção do Residencial Sete Colinas', 520000.00, '2026-05-24', 9, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (6, 6, 1, 'Orçamento-base — Construção de centro comercial', 550000.00, '2026-05-24', 10, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (7, 7, 1, 'Orçamento-base — Ampliação de escola particular', 580000.00, '2026-05-24', 11, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (8, 8, 1, 'Orçamento-base — Infraestrutura do Parque das Acácias', 610000.00, '2026-05-24', 12, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (9, 9, 1, 'Orçamento-base — Reforma do Hotel Encantos do Agreste', 640000.00, '2026-05-24', 13, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (10, 10, 1, 'Orçamento-base — Construção de unidade agroindustrial', 670000.00, '2026-05-24', 14, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (11, 11, 1, 'Orçamento-base — Construção de casa de campo', 700000.00, '2026-05-24', 15, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (12, 12, 1, 'Orçamento-base — Construção do Centro Empresarial Heliópolis', 730000.00, '2026-05-24', 16, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (13, 13, 1, 'Orçamento-base — Construção da Creche Escola Boa Vista', 760000.00, '2026-05-24', 17, 'vigente', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.orcamentos_base (id, obra_id, versao, descricao, valor_total, data_aprovacao, aprovado_por_id, status, created_at, updated_at) VALUES (1, 1, 1, 'Orçamento-base — Reforma do Mercado São Cristóvão', 150000.00, '2026-08-04', 1, 'vigente', '2026-06-20 04:20:24.479452', '2026-08-05 15:48:15.755339');


--
-- Data for Name: itens_orcamento; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (1, 1, 4, 'MAT-001', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 52500.00, 52500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (2, 1, 5, 'MAO-001', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 45000.00, 45000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (3, 1, 6, 'EQP-001', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 22500.00, 22500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (4, 1, 9, 'TER-001', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 30000.00, 30000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (5, 2, 4, 'MAT-002', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 150500.00, 150500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (6, 2, 5, 'MAO-002', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 129000.00, 129000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (7, 2, 6, 'EQP-002', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 64500.00, 64500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (8, 2, 9, 'TER-002', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 86000.00, 86000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (9, 3, 4, 'MAT-003', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 161000.00, 161000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (10, 3, 5, 'MAO-003', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 138000.00, 138000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (11, 3, 6, 'EQP-003', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 69000.00, 69000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (12, 3, 9, 'TER-003', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 92000.00, 92000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (13, 4, 4, 'MAT-004', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 171500.00, 171500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (14, 4, 5, 'MAO-004', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 147000.00, 147000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (15, 4, 6, 'EQP-004', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 73500.00, 73500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (16, 4, 9, 'TER-004', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 98000.00, 98000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (17, 5, 4, 'MAT-005', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 182000.00, 182000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (18, 5, 5, 'MAO-005', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 156000.00, 156000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (19, 5, 6, 'EQP-005', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 78000.00, 78000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (20, 5, 9, 'TER-005', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 104000.00, 104000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (21, 6, 4, 'MAT-006', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 192500.00, 192500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (22, 6, 5, 'MAO-006', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 165000.00, 165000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (23, 6, 6, 'EQP-006', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 82500.00, 82500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (24, 6, 9, 'TER-006', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 110000.00, 110000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (25, 7, 4, 'MAT-007', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 203000.00, 203000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (26, 7, 5, 'MAO-007', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 174000.00, 174000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (27, 7, 6, 'EQP-007', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 87000.00, 87000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (28, 7, 9, 'TER-007', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 116000.00, 116000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (29, 8, 4, 'MAT-008', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 213500.00, 213500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (30, 8, 5, 'MAO-008', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 183000.00, 183000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (31, 8, 6, 'EQP-008', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 91500.00, 91500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (32, 8, 9, 'TER-008', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 122000.00, 122000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (33, 9, 4, 'MAT-009', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 224000.00, 224000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (34, 9, 5, 'MAO-009', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 192000.00, 192000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (35, 9, 6, 'EQP-009', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 96000.00, 96000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (36, 9, 9, 'TER-009', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 128000.00, 128000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (37, 10, 4, 'MAT-010', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 234500.00, 234500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (38, 10, 5, 'MAO-010', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 201000.00, 201000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (39, 10, 6, 'EQP-010', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 100500.00, 100500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (40, 10, 9, 'TER-010', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 134000.00, 134000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (41, 11, 4, 'MAT-011', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 245000.00, 245000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (42, 11, 5, 'MAO-011', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 210000.00, 210000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (43, 11, 6, 'EQP-011', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 105000.00, 105000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (44, 11, 9, 'TER-011', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 140000.00, 140000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (45, 12, 4, 'MAT-012', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 255500.00, 255500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (46, 12, 5, 'MAO-012', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 219000.00, 219000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (47, 12, 6, 'EQP-012', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 109500.00, 109500.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (48, 12, 9, 'TER-012', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 146000.00, 146000.00, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (53, 13, 4, 'MAT-013', 'Materiais', 'Materiais e insumos', 'vb', 1.000, 266000.00, 266000.00, '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (54, 13, 5, 'MAO-013', 'Mão de obra', 'Mão de obra direta', 'vb', 1.000, 228000.00, 228000.00, '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (55, 13, 6, 'EQP-013', 'Equipamentos', 'Equipamentos e logística', 'vb', 1.000, 114000.00, 114000.00, '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.itens_orcamento (id, orcamento_base_id, categoria_financeira_id, codigo, etapa, descricao, unidade_medida, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (56, 13, 9, 'TER-013', 'Terceirizados', 'Serviços especializados', 'vb', 1.000, 152000.00, 152000.00, '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');


--
-- Data for Name: itens_ordem_compra; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (1, 2, 2, 'Cimento CP II 50 kg', 11.000, 26.00, 286.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (2, 3, 3, 'Areia média lavada', 12.000, 27.00, 324.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (3, 4, 4, 'Brita nº 1', 13.000, 28.00, 364.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (4, 5, 5, 'Bloco cerâmico 9x19x19', 14.000, 29.00, 406.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (5, 6, 6, 'Vergalhão CA-50 10 mm', 15.000, 30.00, 450.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (6, 7, 7, 'Tijolo de oito furos', 16.000, 31.00, 496.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (7, 8, 8, 'Argamassa AC-II 20 kg', 17.000, 32.00, 544.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (8, 9, 9, 'Tinta acrílica premium 18 L', 18.000, 33.00, 594.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (9, 10, 10, 'Cabo elétrico 2,5 mm²', 19.000, 34.00, 646.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (10, 11, 11, 'Tubo PVC soldável 25 mm', 20.000, 35.00, 700.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (11, 12, 12, 'Telha cerâmica colonial', 21.000, 36.00, 756.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (12, 13, 13, 'Piso porcelanato acetinado', 22.000, 37.00, 814.00, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.itens_ordem_compra (id, ordem_compra_id, insumo_id, descricao, quantidade, valor_unitario, valor_total, created_at, updated_at) VALUES (14, 1, 1, 'Aditivo impermeabilizante 18 L', 10.000, 50.00, 500.00, '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');


--
-- Data for Name: logs_auditoria; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (1, 1, 'auth', 'login', 'usuarios', 1, 'info', 'Login realizado', NULL, NULL, 'null', 'null', '2026-06-19 17:33:29.579386');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (2, 1, 'auth', 'login', 'usuarios', 1, 'info', 'Login realizado', NULL, NULL, 'null', 'null', '2026-06-20 03:58:26.564583');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (18, 1, 'auth', 'login', 'usuarios', 1, 'info', 'Login realizado', NULL, NULL, 'null', '{"origem": "streamlit", "username": "admin"}', '2026-08-10 17:04:00.645957');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (19, 1, 'auth', 'login', 'usuarios', 1, 'info', 'Login realizado', NULL, NULL, 'null', '{"origem": "streamlit", "username": "admin"}', '2026-08-10 17:05:15.843307');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (20, 1, 'auth', 'login', 'usuarios', 1, 'info', 'Login realizado', NULL, NULL, 'null', '{"origem": "streamlit", "username": "admin"}', '2026-08-10 17:08:22.653988');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (21, 1, 'auth', 'login', 'usuarios', 1, 'info', 'Login realizado', NULL, NULL, 'null', '{"origem": "streamlit", "username": "admin"}', '2026-08-10 17:37:56.968188');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (22, 1, 'auth', 'login', 'usuarios', 1, 'info', 'Login realizado', NULL, NULL, 'null', '{"origem": "streamlit", "username": "admin"}', '2026-08-10 20:00:21.26524');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (3, 2, 'engenharia', 'visualizar', 'cadastro', 1, 'info', 'Atualização de cadastro por Ana Paula Rodrigues', '192.0.2.1', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (4, 3, 'obras', 'criar', 'cadastro', 2, 'info', 'Atualização de cadastro por Bruno Henrique Alves', '192.0.2.2', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (5, 4, 'financeiro', 'editar', 'cadastro', 3, 'info', 'Atualização de cadastro por Camila Ferreira Melo', '192.0.2.3', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (6, 5, 'compras', 'visualizar', 'cadastro', 4, 'info', 'Atualização de cadastro por Diego Moura Cavalcanti', '192.0.2.4', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (7, 6, 'rh', 'criar', 'cadastro', 5, 'info', 'Atualização de cadastro por Edson José da Silva', '192.0.2.5', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (8, 7, 'administrativo', 'editar', 'cadastro', 6, 'info', 'Atualização de cadastro por Fernanda Lima Barros', '192.0.2.6', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (9, 8, 'engenharia', 'visualizar', 'cadastro', 7, 'info', 'Atualização de cadastro por Gabriel Nunes Costa', '192.0.2.7', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (10, 9, 'obras', 'criar', 'cadastro', 8, 'info', 'Atualização de cadastro por Helena Maria Souza', '192.0.2.8', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (11, 10, 'financeiro', 'editar', 'cadastro', 9, 'info', 'Atualização de cadastro por Igor Matheus Ribeiro', '192.0.2.9', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (12, 11, 'compras', 'visualizar', 'cadastro', 10, 'info', 'Atualização de cadastro por Juliana Alves Monteiro', '192.0.2.10', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (13, 12, 'rh', 'criar', 'cadastro', 11, 'info', 'Atualização de cadastro por Lucas Vinícius Santos', '192.0.2.11', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');
INSERT INTO public.logs_auditoria (id, usuario_id, modulo, acao, entidade, entidade_id, nivel, descricao, ip_origem, user_agent, dados_anteriores, dados_novos, created_at) VALUES (14, 13, 'administrativo', 'editar', 'cadastro', 12, 'info', 'Atualização de cadastro por Mariana Bezerra Oliveira', '192.0.2.12', 'UrbanPrime Demo Browser', NULL, NULL, '2026-08-02 01:16:25.25614');


--
-- Data for Name: manutencoes_frota; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (1, 1, 1, 1, 'preventiva', 'Revisão preventiva de FROTA-UP-01 — 2026', '2026-01-08', '2026-01-10', 970.00, 925.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (2, 2, 2, 2, 'preventiva', 'Revisão preventiva de FROTA-UP-02 — 2026', '2026-02-08', '2026-02-10', 1090.00, 1050.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (3, 3, 3, 3, 'preventiva', 'Revisão preventiva de FROTA-UP-03 — 2026', '2026-03-08', '2026-03-10', 1210.00, 1175.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (4, 4, 4, 4, 'preventiva', 'Revisão preventiva de FROTA-UP-04 — 2026', '2026-04-08', '2026-04-10', 1330.00, 1300.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (5, 5, 5, 5, 'preventiva', 'Revisão preventiva de FROTA-UP-05 — 2026', '2026-05-08', '2026-05-10', 1450.00, 1425.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (6, 6, 6, 6, 'preventiva', 'Revisão preventiva de FROTA-UP-06 — 2026', '2026-06-08', '2026-06-10', 1570.00, 1550.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (7, 7, 7, 7, 'preventiva', 'Revisão preventiva de FROTA-UP-07 — 2026', '2026-07-08', '2026-07-10', 1690.00, 1675.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (8, 8, 8, 8, 'preventiva', 'Revisão preventiva de FROTA-UP-08 — 2026', '2026-08-08', '2026-08-10', 1810.00, 1800.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (9, 9, 9, 9, 'preventiva', 'Revisão preventiva de FROTA-UP-09 — 2026', '2026-09-08', '2026-09-10', 1930.00, 1925.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (10, 10, 10, 10, 'preventiva', 'Revisão preventiva de FROTA-UP-10 — 2026', '2026-10-08', '2026-10-10', 2050.00, 2050.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (11, 11, 11, 11, 'preventiva', 'Revisão preventiva de FROTA-UP-11 — 2026', '2026-11-08', '2026-11-10', 2170.00, 2175.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.manutencoes_frota (id, frota_id, fornecedor_id, obra_id, tipo, descricao, data_entrada, data_saida, custo, horimetro, status, created_at, updated_at) VALUES (12, 12, 12, 12, 'preventiva', 'Revisão preventiva de FROTA-UP-12 — 2026', '2026-12-08', '2026-12-10', 2290.00, 2300.00, 'concluida', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Data for Name: metas_indicadores; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (1, 'FATURAMENTO', 'Faturamento mensal', '2026-01', 85000.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (2, 'MARGEM_BRUTA', 'Margem bruta', '2026-01', 22.0000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (3, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-01', 6.0000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (4, 'CUSTO_OBRAS', 'Custo realizado', '2026-01', 65000.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (5, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-01', 85.0000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (6, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-01', 15.0000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (7, 'FATURAMENTO', 'Faturamento mensal', '2026-02', 85850.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (8, 'MARGEM_BRUTA', 'Margem bruta', '2026-02', 22.2200, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (9, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-02', 6.0600, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (10, 'CUSTO_OBRAS', 'Custo realizado', '2026-02', 65650.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (11, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-02', 85.8500, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (12, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-02', 15.1500, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (13, 'FATURAMENTO', 'Faturamento mensal', '2026-03', 86700.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (14, 'MARGEM_BRUTA', 'Margem bruta', '2026-03', 22.4400, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (15, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-03', 6.1200, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (16, 'CUSTO_OBRAS', 'Custo realizado', '2026-03', 66300.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (17, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-03', 86.7000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (18, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-03', 15.3000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (19, 'FATURAMENTO', 'Faturamento mensal', '2026-04', 87550.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (20, 'MARGEM_BRUTA', 'Margem bruta', '2026-04', 22.6600, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (21, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-04', 6.1800, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (22, 'CUSTO_OBRAS', 'Custo realizado', '2026-04', 66950.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (23, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-04', 87.5500, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (24, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-04', 15.4500, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (25, 'FATURAMENTO', 'Faturamento mensal', '2026-05', 88400.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (26, 'MARGEM_BRUTA', 'Margem bruta', '2026-05', 22.8800, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (27, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-05', 6.2400, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (28, 'CUSTO_OBRAS', 'Custo realizado', '2026-05', 67600.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (29, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-05', 88.4000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (30, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-05', 15.6000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (31, 'FATURAMENTO', 'Faturamento mensal', '2026-06', 89250.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (32, 'MARGEM_BRUTA', 'Margem bruta', '2026-06', 23.1000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (33, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-06', 6.3000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (34, 'CUSTO_OBRAS', 'Custo realizado', '2026-06', 68250.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (35, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-06', 89.2500, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (36, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-06', 15.7500, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (37, 'FATURAMENTO', 'Faturamento mensal', '2026-07', 90100.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (38, 'MARGEM_BRUTA', 'Margem bruta', '2026-07', 23.3200, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (39, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-07', 6.3600, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (40, 'CUSTO_OBRAS', 'Custo realizado', '2026-07', 68900.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (41, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-07', 90.1000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (42, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-07', 15.9000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (43, 'FATURAMENTO', 'Faturamento mensal', '2026-08', 90950.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (44, 'MARGEM_BRUTA', 'Margem bruta', '2026-08', 23.5400, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (45, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-08', 6.4200, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (46, 'CUSTO_OBRAS', 'Custo realizado', '2026-08', 69550.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (47, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-08', 90.9500, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (48, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-08', 16.0500, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (49, 'FATURAMENTO', 'Faturamento mensal', '2026-09', 91800.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (50, 'MARGEM_BRUTA', 'Margem bruta', '2026-09', 23.7600, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (51, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-09', 6.4800, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (52, 'CUSTO_OBRAS', 'Custo realizado', '2026-09', 70200.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (53, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-09', 91.8000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (54, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-09', 16.2000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (55, 'FATURAMENTO', 'Faturamento mensal', '2026-10', 92650.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (56, 'MARGEM_BRUTA', 'Margem bruta', '2026-10', 23.9800, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (57, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-10', 6.5400, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (58, 'CUSTO_OBRAS', 'Custo realizado', '2026-10', 70850.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (59, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-10', 92.6500, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (60, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-10', 16.3500, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (61, 'FATURAMENTO', 'Faturamento mensal', '2026-11', 93500.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (62, 'MARGEM_BRUTA', 'Margem bruta', '2026-11', 24.2000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (63, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-11', 6.6000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (64, 'CUSTO_OBRAS', 'Custo realizado', '2026-11', 71500.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (65, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-11', 93.5000, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (66, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-11', 16.5000, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (67, 'FATURAMENTO', 'Faturamento mensal', '2026-12', 94350.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (68, 'MARGEM_BRUTA', 'Margem bruta', '2026-12', 24.4200, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (69, 'OBRAS_ATIVAS', 'Obras em andamento', '2026-12', 6.6600, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (70, 'CUSTO_OBRAS', 'Custo realizado', '2026-12', 72150.0000, 'reais', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (71, 'DISPONIBILIDADE_FROTA', 'Disponibilidade da frota', '2026-12', 94.3500, 'percentual', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.metas_indicadores (id, codigo_indicador, nome, competencia, valor_meta, unidade, centro_custo_id, obra_id, observacao, ativo, created_at, updated_at) VALUES (72, 'QUADRO_ATIVO', 'Funcionários ativos', '2026-12', 16.6500, 'numero', NULL, NULL, 'Meta corporativa mensal', true, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Data for Name: movimentacoes_caixa; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (2, 2, NULL, NULL, NULL, 9, 2, 'saida', '2026-02-20', 45500.00, 'Movimentação financeira histórica 02/2026', 'transferencia', true, '2026-02-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (4, 4, NULL, NULL, NULL, 7, 4, 'saida', '2026-04-20', 49000.00, 'Movimentação financeira histórica 04/2026', 'transferencia', true, '2026-04-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (6, 6, NULL, NULL, NULL, 9, 6, 'saida', '2026-06-20', 52500.00, 'Movimentação financeira histórica 06/2026', 'transferencia', true, '2026-06-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (8, 8, NULL, NULL, NULL, 7, 8, 'saida', '2026-08-20', 56000.00, 'Movimentação financeira histórica 08/2026', 'transferencia', true, '2026-08-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (10, 10, NULL, NULL, NULL, 9, 10, 'saida', '2026-10-20', 59500.00, 'Movimentação financeira histórica 10/2026', 'transferencia', false, NULL, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (12, 2, NULL, NULL, NULL, 7, 12, 'saida', '2026-12-20', 63000.00, 'Movimentação financeira histórica 12/2026', 'transferencia', false, NULL, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (20, 1, NULL, 5, 4, 1, 4, 'entrada', '2026-07-29', 43700.00, 'Recebimento NF-UP-2026-0004', 'transferencia', true, '2026-07-29', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (21, 1, NULL, 9, 8, 1, 8, 'entrada', '2026-07-25', 54150.00, 'Recebimento NF-UP-2026-0008', 'transferencia', true, '2026-07-25', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (22, 1, NULL, 13, 12, 1, 12, 'entrada', '2026-07-21', 64600.00, 'Recebimento NF-UP-2026-0012', 'transferencia', true, '2026-07-21', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (23, 1, 13, NULL, NULL, 4, 17, 'saida', '2026-07-21', 12800.00, 'Pagamento DOC-PAG-2026-0013', 'transferencia', true, '2026-07-21', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (24, 1, 4, NULL, NULL, 7, 4, 'saida', '2026-07-30', 6950.00, 'Pagamento DOC-PAG-2026-0004', 'transferencia', true, '2026-07-30', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (25, 1, 7, NULL, NULL, 6, 7, 'saida', '2026-07-27', 8900.00, 'Pagamento DOC-PAG-2026-0007', 'transferencia', true, '2026-07-27', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (26, 1, 10, NULL, NULL, 9, 10, 'saida', '2026-07-24', 10850.00, 'Pagamento DOC-PAG-2026-0010', 'transferencia', true, '2026-07-24', '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (1, 1, NULL, 2, 1, 1, 1, 'entrada', '2026-01-20', 43750.00, 'Movimentação financeira histórica 01/2026', 'transferencia', true, '2026-01-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (3, 3, NULL, 4, 3, 1, 3, 'entrada', '2026-03-20', 47250.00, 'Movimentação financeira histórica 03/2026', 'transferencia', true, '2026-03-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (5, 5, NULL, 6, 5, 1, 5, 'entrada', '2026-05-20', 50750.00, 'Movimentação financeira histórica 05/2026', 'transferencia', true, '2026-05-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (7, 7, NULL, 8, 7, 1, 7, 'entrada', '2026-07-20', 54250.00, 'Movimentação financeira histórica 07/2026', 'transferencia', true, '2026-07-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (9, 9, NULL, 10, 9, 1, 9, 'entrada', '2026-09-20', 57750.00, 'Movimentação financeira histórica 09/2026', 'transferencia', true, '2026-09-21', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.movimentacoes_caixa (id, conta_bancaria_id, conta_pagar_id, conta_receber_id, fatura_id, categoria_financeira_id, centro_custo_id, tipo, data_movimentacao, valor, descricao, forma_pagamento, conciliado, data_conciliacao, created_at, updated_at) VALUES (11, 1, NULL, 12, 11, 1, 11, 'entrada', '2026-11-20', 61250.00, 'Movimentação financeira histórica 11/2026', 'transferencia', false, NULL, '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Data for Name: movimentacoes_estoque; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (1, 2, 2, 'entrada', 6.000, '2026-08-01', 'Movimentação para Construção de residência em Heliópolis', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (2, 3, 3, 'saida', 7.000, '2026-07-31', 'Movimentação para Construção de galpão logístico', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (3, 4, 4, 'entrada', 8.000, '2026-07-30', 'Movimentação para Reforma e ampliação de clínica', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (4, 5, 5, 'saida', 9.000, '2026-07-29', 'Movimentação para Construção do Residencial Sete Colinas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (5, 6, 6, 'entrada', 10.000, '2026-07-28', 'Movimentação para Construção de centro comercial', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (6, 7, 7, 'saida', 11.000, '2026-07-27', 'Movimentação para Ampliação de escola particular', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (7, 8, 8, 'entrada', 12.000, '2026-07-26', 'Movimentação para Infraestrutura do Parque das Acácias', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (8, 9, 9, 'saida', 13.000, '2026-07-25', 'Movimentação para Reforma do Hotel Encantos do Agreste', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (9, 10, 10, 'entrada', 14.000, '2026-07-24', 'Movimentação para Construção de unidade agroindustrial', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (10, 11, 11, 'saida', 15.000, '2026-07-23', 'Movimentação para Construção de casa de campo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (11, 12, 12, 'entrada', 16.000, '2026-07-22', 'Movimentação para Construção do Centro Empresarial Heliópolis', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.movimentacoes_estoque (id, insumo_id, obra_id, tipo, quantidade, data_movimentacao, observacao, created_at, updated_at) VALUES (12, 13, 13, 'saida', 17.000, '2026-07-21', 'Movimentação para Construção da Creche Escola Boa Vista', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');


--
-- Data for Name: perfis; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (1, 'administrador', 'Acesso total ao ERP UrbanPrime', 100, true, '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (2, 'financeiro', 'Operacao financeira', 70, true, '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (3, 'engenharia', 'Projetos e obras', 60, true, '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (4, 'compras', 'Compras e fornecedores', 50, true, '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (5, 'rh', 'Recursos humanos', 50, true, '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (28, 'gestor_obras', 'Perfil de acesso para gestor obras', 52, true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (29, 'comercial', 'Perfil de acesso para comercial', 59, true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (30, 'almoxarifado', 'Perfil de acesso para almoxarifado', 66, true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (31, 'planejamento', 'Perfil de acesso para planejamento', 73, true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (32, 'auditoria', 'Perfil de acesso para auditoria', 80, true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (33, 'diretoria', 'Perfil de acesso para diretoria', 87, true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.perfis (id, nome, descricao, nivel_acesso, ativo, created_at, updated_at) VALUES (34, 'consulta', 'Perfil de acesso para consulta', 94, true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');


--
-- Data for Name: permissoes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (1, 'comercial', 'visualizar', 'Permite visualizar em comercial', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (2, 'comercial', 'criar', 'Permite criar em comercial', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (3, 'comercial', 'editar', 'Permite editar em comercial', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (4, 'comercial', 'excluir', 'Permite excluir em comercial', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (5, 'comercial', 'aprovar', 'Permite aprovar em comercial', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (6, 'comercial', 'cancelar', 'Permite cancelar em comercial', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (7, 'engenharia', 'visualizar', 'Permite visualizar em engenharia', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (8, 'engenharia', 'criar', 'Permite criar em engenharia', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (9, 'engenharia', 'editar', 'Permite editar em engenharia', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (10, 'engenharia', 'excluir', 'Permite excluir em engenharia', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (11, 'engenharia', 'aprovar', 'Permite aprovar em engenharia', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (12, 'engenharia', 'cancelar', 'Permite cancelar em engenharia', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (13, 'obras', 'visualizar', 'Permite visualizar em obras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (14, 'obras', 'criar', 'Permite criar em obras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (15, 'obras', 'editar', 'Permite editar em obras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (16, 'obras', 'excluir', 'Permite excluir em obras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (17, 'obras', 'aprovar', 'Permite aprovar em obras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (18, 'obras', 'cancelar', 'Permite cancelar em obras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (19, 'financeiro', 'visualizar', 'Permite visualizar em financeiro', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (20, 'financeiro', 'criar', 'Permite criar em financeiro', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (21, 'financeiro', 'editar', 'Permite editar em financeiro', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (22, 'financeiro', 'excluir', 'Permite excluir em financeiro', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (23, 'financeiro', 'aprovar', 'Permite aprovar em financeiro', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (24, 'financeiro', 'cancelar', 'Permite cancelar em financeiro', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (25, 'rh', 'visualizar', 'Permite visualizar em rh', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (26, 'rh', 'criar', 'Permite criar em rh', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (27, 'rh', 'editar', 'Permite editar em rh', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (28, 'rh', 'excluir', 'Permite excluir em rh', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (29, 'rh', 'aprovar', 'Permite aprovar em rh', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (30, 'rh', 'cancelar', 'Permite cancelar em rh', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (31, 'estoque', 'visualizar', 'Permite visualizar em estoque', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (32, 'estoque', 'criar', 'Permite criar em estoque', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (33, 'estoque', 'editar', 'Permite editar em estoque', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (34, 'estoque', 'excluir', 'Permite excluir em estoque', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (35, 'estoque', 'aprovar', 'Permite aprovar em estoque', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (36, 'estoque', 'cancelar', 'Permite cancelar em estoque', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (37, 'compras', 'visualizar', 'Permite visualizar em compras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (38, 'compras', 'criar', 'Permite criar em compras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (39, 'compras', 'editar', 'Permite editar em compras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (40, 'compras', 'excluir', 'Permite excluir em compras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (41, 'compras', 'aprovar', 'Permite aprovar em compras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (42, 'compras', 'cancelar', 'Permite cancelar em compras', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (43, 'planejamento', 'visualizar', 'Permite visualizar em planejamento', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (44, 'planejamento', 'criar', 'Permite criar em planejamento', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (45, 'planejamento', 'editar', 'Permite editar em planejamento', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (46, 'planejamento', 'excluir', 'Permite excluir em planejamento', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (47, 'planejamento', 'aprovar', 'Permite aprovar em planejamento', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (48, 'planejamento', 'cancelar', 'Permite cancelar em planejamento', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (49, 'auth', 'visualizar', 'Permite visualizar em auth', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (50, 'auth', 'criar', 'Permite criar em auth', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (51, 'auth', 'editar', 'Permite editar em auth', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (52, 'auth', 'excluir', 'Permite excluir em auth', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (53, 'auth', 'aprovar', 'Permite aprovar em auth', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (54, 'auth', 'cancelar', 'Permite cancelar em auth', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (55, 'usuarios', 'visualizar', 'Permite visualizar em usuarios', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (56, 'usuarios', 'criar', 'Permite criar em usuarios', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (57, 'usuarios', 'editar', 'Permite editar em usuarios', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (58, 'usuarios', 'excluir', 'Permite excluir em usuarios', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (59, 'usuarios', 'aprovar', 'Permite aprovar em usuarios', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (60, 'usuarios', 'cancelar', 'Permite cancelar em usuarios', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (61, 'perfis', 'visualizar', 'Permite visualizar em perfis', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (62, 'perfis', 'criar', 'Permite criar em perfis', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (63, 'perfis', 'editar', 'Permite editar em perfis', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (64, 'perfis', 'excluir', 'Permite excluir em perfis', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (65, 'perfis', 'aprovar', 'Permite aprovar em perfis', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (66, 'perfis', 'cancelar', 'Permite cancelar em perfis', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (67, 'auditoria', 'visualizar', 'Permite visualizar em auditoria', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (68, 'auditoria', 'criar', 'Permite criar em auditoria', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (69, 'auditoria', 'editar', 'Permite editar em auditoria', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (70, 'auditoria', 'excluir', 'Permite excluir em auditoria', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (71, 'auditoria', 'aprovar', 'Permite aprovar em auditoria', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');
INSERT INTO public.permissoes (id, modulo, acao, descricao, created_at, updated_at) VALUES (72, 'auditoria', 'cancelar', 'Permite cancelar em auditoria', '2026-06-19 17:31:06.688367', '2026-06-19 17:31:06.688367');


--
-- Data for Name: perfil_permissao; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (1, 1, 67, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (2, 1, 50, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (3, 1, 69, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (4, 1, 51, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (5, 1, 59, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (6, 1, 42, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (7, 1, 41, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (8, 1, 29, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (9, 1, 6, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (10, 1, 8, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (11, 1, 30, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (12, 1, 28, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (13, 1, 48, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (14, 1, 62, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (15, 1, 43, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (16, 1, 61, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (17, 1, 3, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (18, 1, 14, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (19, 1, 35, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (20, 1, 63, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (21, 1, 9, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (22, 1, 7, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (23, 1, 16, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (24, 1, 54, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (25, 1, 4, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (26, 1, 36, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (27, 1, 44, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (28, 1, 23, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (29, 1, 53, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (30, 1, 58, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (31, 1, 1, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (32, 1, 22, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (33, 1, 49, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (34, 1, 60, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (35, 1, 45, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (36, 1, 70, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (37, 1, 39, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (38, 1, 11, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (39, 1, 33, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (40, 1, 66, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (41, 1, 17, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (42, 1, 31, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (43, 1, 57, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (44, 1, 18, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (45, 1, 12, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (46, 1, 10, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (47, 1, 34, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (48, 1, 64, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (49, 1, 72, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (50, 1, 2, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (51, 1, 71, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (52, 1, 20, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (53, 1, 26, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (54, 1, 25, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (55, 1, 27, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (56, 1, 37, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (57, 1, 65, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (58, 1, 52, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (59, 1, 19, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (60, 1, 32, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (61, 1, 24, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (62, 1, 38, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (63, 1, 68, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (64, 1, 55, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (65, 1, 47, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (66, 1, 15, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (67, 1, 46, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (68, 1, 56, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (69, 1, 40, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (70, 1, 13, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (71, 1, 5, '2026-06-19 17:31:06.688367');
INSERT INTO public.perfil_permissao (id, perfil_id, permissao_id, created_at) VALUES (72, 1, 21, '2026-06-19 17:31:06.688367');


--
-- Data for Name: registro_ponto; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (1, 6, '2026-08-01', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção de residência em Heliópolis', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (2, 7, '2026-07-31', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção de galpão logístico', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (3, 8, '2026-07-30', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Reforma e ampliação de clínica', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (4, 9, '2026-07-29', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção do Residencial Sete Colinas', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (5, 10, '2026-07-28', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção de centro comercial', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (6, 11, '2026-07-27', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Ampliação de escola particular', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (7, 12, '2026-07-26', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Infraestrutura do Parque das Acácias', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (8, 13, '2026-07-25', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Reforma do Hotel Encantos do Agreste', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (9, 14, '2026-07-24', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção de unidade agroindustrial', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (10, 15, '2026-07-23', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção de casa de campo', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (11, 16, '2026-07-22', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção do Centro Empresarial Heliópolis', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.registro_ponto (id, funcionario_id, data, entrada, saida_intervalo, retorno_intervalo, saida, observacao, created_at, updated_at) VALUES (12, 17, '2026-07-21', '08:00:00', '12:00:00', '13:00:00', '17:00:00', 'Jornada na equipe de Construção da Creche Escola Boa Vista', '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');


--
-- Data for Name: revisoes_projeto; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (1, 2, 6, 1, 'Revisão demonstrativa 1', 'Compatibilização de disciplinas', 'demo/revisao-01.pdf', '2026-08-01', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (2, 3, 7, 2, 'Revisão demonstrativa 2', 'Compatibilização de disciplinas', 'demo/revisao-02.pdf', '2026-07-31', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (3, 4, 8, 3, 'Revisão demonstrativa 3', 'Compatibilização de disciplinas', 'demo/revisao-03.pdf', '2026-07-30', false, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (4, 5, 9, 4, 'Revisão demonstrativa 4', 'Compatibilização de disciplinas', 'demo/revisao-04.pdf', '2026-07-29', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (5, 6, 10, 5, 'Revisão demonstrativa 5', 'Compatibilização de disciplinas', 'demo/revisao-05.pdf', '2026-07-28', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (6, 7, 11, 6, 'Revisão demonstrativa 6', 'Compatibilização de disciplinas', 'demo/revisao-06.pdf', '2026-07-27', false, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (7, 8, 12, 7, 'Revisão demonstrativa 7', 'Compatibilização de disciplinas', 'demo/revisao-07.pdf', '2026-07-26', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (8, 9, 13, 8, 'Revisão demonstrativa 8', 'Compatibilização de disciplinas', 'demo/revisao-08.pdf', '2026-07-25', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (9, 10, 14, 9, 'Revisão demonstrativa 9', 'Compatibilização de disciplinas', 'demo/revisao-09.pdf', '2026-07-24', false, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (10, 11, 15, 10, 'Revisão demonstrativa 10', 'Compatibilização de disciplinas', 'demo/revisao-10.pdf', '2026-07-23', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (11, 12, 16, 11, 'Revisão demonstrativa 11', 'Compatibilização de disciplinas', 'demo/revisao-11.pdf', '2026-07-22', true, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (12, 13, 17, 12, 'Revisão demonstrativa 12', 'Compatibilização de disciplinas', 'demo/revisao-12.pdf', '2026-07-21', false, '2026-08-02 01:16:25.25614', '2026-08-02 01:16:25.25614');
INSERT INTO public.revisoes_projeto (id, projeto_id, responsavel_id, numero_revisao, descricao, motivo, arquivo_revisao, data_revisao, aprovado, created_at, updated_at) VALUES (14, 1, 4, 1, 'Revisão inicial — Reforma do Mercado São Cristóvão', 'Compatibilização inicial das disciplinas', 'demo/reforma-mercado-sao-cristovao-r01.pdf', '2026-06-25', false, '2026-08-05 15:48:15.755339', '2026-08-05 15:48:15.755339');


--
-- Data for Name: sessoes_usuario; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (1, 2, 'demo-session-hash-01', '192.0.2.1', 'UrbanPrime Demo Browser', '2026-08-02 00:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (2, 3, 'demo-session-hash-02', '192.0.2.2', 'UrbanPrime Demo Browser', '2026-08-01 23:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (3, 4, 'demo-session-hash-03', '192.0.2.3', 'UrbanPrime Demo Browser', '2026-08-01 22:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (4, 5, 'demo-session-hash-04', '192.0.2.4', 'UrbanPrime Demo Browser', '2026-08-01 21:16:25.178945', '2026-08-09 01:16:25.178945', false, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (5, 6, 'demo-session-hash-05', '192.0.2.5', 'UrbanPrime Demo Browser', '2026-08-01 20:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (6, 7, 'demo-session-hash-06', '192.0.2.6', 'UrbanPrime Demo Browser', '2026-08-01 19:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (7, 8, 'demo-session-hash-07', '192.0.2.7', 'UrbanPrime Demo Browser', '2026-08-01 18:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (8, 9, 'demo-session-hash-08', '192.0.2.8', 'UrbanPrime Demo Browser', '2026-08-01 17:16:25.178945', '2026-08-09 01:16:25.178945', false, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (9, 10, 'demo-session-hash-09', '192.0.2.9', 'UrbanPrime Demo Browser', '2026-08-01 16:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (10, 11, 'demo-session-hash-10', '192.0.2.10', 'UrbanPrime Demo Browser', '2026-08-01 15:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (11, 12, 'demo-session-hash-11', '192.0.2.11', 'UrbanPrime Demo Browser', '2026-08-01 14:16:25.178945', '2026-08-09 01:16:25.178945', true, '2026-08-02 01:16:25.25614');
INSERT INTO public.sessoes_usuario (id, usuario_id, token_sessao_hash, ip_origem, user_agent, data_login, data_expiracao, ativo, created_at) VALUES (12, 13, 'demo-session-hash-12', '192.0.2.12', 'UrbanPrime Demo Browser', '2026-08-01 13:16:25.178945', '2026-08-09 01:16:25.178945', false, '2026-08-02 01:16:25.25614');


--
-- Data for Name: tokens_refresh; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (1, 2, 'demo-refresh-hash-01', '2026-08-02 00:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.1', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (2, 3, 'demo-refresh-hash-02', '2026-08-01 23:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.2', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (3, 4, 'demo-refresh-hash-03', '2026-08-01 22:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.3', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (4, 5, 'demo-refresh-hash-04', '2026-08-01 21:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.4', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (5, 6, 'demo-refresh-hash-05', '2026-08-01 20:16:25.178945', '2026-09-01 01:16:25.178945', true, '192.0.2.5', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (6, 7, 'demo-refresh-hash-06', '2026-08-01 19:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.6', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (7, 8, 'demo-refresh-hash-07', '2026-08-01 18:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.7', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (8, 9, 'demo-refresh-hash-08', '2026-08-01 17:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.8', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (9, 10, 'demo-refresh-hash-09', '2026-08-01 16:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.9', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (10, 11, 'demo-refresh-hash-10', '2026-08-01 15:16:25.178945', '2026-09-01 01:16:25.178945', true, '192.0.2.10', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (11, 12, 'demo-refresh-hash-11', '2026-08-01 14:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.11', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');
INSERT INTO public.tokens_refresh (id, usuario_id, token_hash, data_criacao, data_expiracao, revogado, ip_origem, user_agent, created_at) VALUES (12, 13, 'demo-refresh-hash-12', '2026-08-01 13:16:25.178945', '2026-09-01 01:16:25.178945', false, '192.0.2.12', 'UrbanPrime Demo Browser', '2026-08-02 01:16:25.25614');


--
-- Data for Name: usuario_perfil; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (1, 1, 1, '2026-06-19 17:31:06.688367');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (2, 2, 2, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (3, 3, 3, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (4, 4, 4, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (5, 5, 5, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (6, 6, 28, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (7, 7, 29, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (8, 8, 30, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (9, 9, 31, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (10, 10, 32, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (11, 11, 33, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (12, 12, 34, '2026-08-02 01:16:25.25614');
INSERT INTO public.usuario_perfil (id, usuario_id, perfil_id, created_at) VALUES (13, 13, 1, '2026-08-02 01:16:25.25614');


--
-- Data for Name: utilizacoes_frota; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (1, 1, 1, 1, '2026-01-18', 76.00, 950.00, 1026.00, 100.00, 'Utilização mensal de FROTA-UP-01 — 2026-01', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (2, 2, 2, 4, '2026-02-18', 80.00, 1050.00, 1130.00, 105.00, 'Utilização mensal de FROTA-UP-02 — 2026-02', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (3, 3, 3, 6, '2026-03-18', 84.00, 1150.00, 1234.00, 110.00, 'Utilização mensal de FROTA-UP-03 — 2026-03', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (4, 4, 4, 7, '2026-04-18', 88.00, 1250.00, 1338.00, 115.00, 'Utilização mensal de FROTA-UP-04 — 2026-04', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (5, 5, 5, 8, '2026-05-18', 92.00, 1350.00, 1442.00, 120.00, 'Utilização mensal de FROTA-UP-05 — 2026-05', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (6, 6, 6, 9, '2026-06-18', 96.00, 1450.00, 1546.00, 125.00, 'Utilização mensal de FROTA-UP-06 — 2026-06', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (7, 7, 7, 10, '2026-07-18', 100.00, 1550.00, 1650.00, 130.00, 'Utilização mensal de FROTA-UP-07 — 2026-07', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (8, 8, 8, 11, '2026-08-18', 104.00, 1650.00, 1754.00, 135.00, 'Utilização mensal de FROTA-UP-08 — 2026-08', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (9, 9, 9, 12, '2026-09-18', 108.00, 1750.00, 1858.00, 140.00, 'Utilização mensal de FROTA-UP-09 — 2026-09', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (10, 10, 10, 13, '2026-10-18', 112.00, 1850.00, 1962.00, 145.00, 'Utilização mensal de FROTA-UP-10 — 2026-10', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (11, 11, 11, 14, '2026-11-18', 116.00, 1950.00, 2066.00, 150.00, 'Utilização mensal de FROTA-UP-11 — 2026-11', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');
INSERT INTO public.utilizacoes_frota (id, frota_id, obra_id, funcionario_id, data_utilizacao, horas_utilizadas, horimetro_inicial, horimetro_final, custo_hora, observacao, created_at, updated_at) VALUES (12, 12, 12, 15, '2026-12-18', 120.00, 2050.00, 2170.00, 155.00, 'Utilização mensal de FROTA-UP-12 — 2026-12', '2026-08-02 12:59:36.171538', '2026-08-02 12:59:36.171538');


--
-- Name: abastecimentos_frota_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.abastecimentos_frota_id_seq', 12, true);


--
-- Name: agenda_visitas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.agenda_visitas_id_seq', 12, true);


--
-- Name: alocacoes_funcionario_obra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.alocacoes_funcionario_obra_id_seq', 12, true);


--
-- Name: apropriacoes_custo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.apropriacoes_custo_id_seq', 12, true);


--
-- Name: categorias_financeiras_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.categorias_financeiras_id_seq', 14, true);


--
-- Name: centros_custo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.centros_custo_id_seq', 17, true);


--
-- Name: chamados_tecnicos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.chamados_tecnicos_id_seq', 12, true);


--
-- Name: clientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.clientes_id_seq', 14, true);


--
-- Name: contas_bancarias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.contas_bancarias_id_seq', 10, true);


--
-- Name: contas_pagar_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.contas_pagar_id_seq', 13, true);


--
-- Name: contas_receber_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.contas_receber_id_seq', 13, true);


--
-- Name: contratos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.contratos_id_seq', 13, true);


--
-- Name: cotacoes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cotacoes_id_seq', 14, true);


--
-- Name: cronogramas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.cronogramas_id_seq', 14, true);


--
-- Name: diarios_obra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.diarios_obra_id_seq', 14, true);


--
-- Name: faturas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.faturas_id_seq', 12, true);


--
-- Name: folha_pagamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.folha_pagamento_id_seq', 12, true);


--
-- Name: fornecedores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.fornecedores_id_seq', 13, true);


--
-- Name: frotas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.frotas_id_seq', 12, true);


--
-- Name: funcionarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.funcionarios_id_seq', 17, true);


--
-- Name: historicos_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.historicos_status_id_seq', 14, true);


--
-- Name: insumos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.insumos_id_seq', 13, true);


--
-- Name: itens_orcamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.itens_orcamento_id_seq', 56, true);


--
-- Name: itens_ordem_compra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.itens_ordem_compra_id_seq', 14, true);


--
-- Name: logs_auditoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.logs_auditoria_id_seq', 22, true);


--
-- Name: manutencoes_frota_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.manutencoes_frota_id_seq', 12, true);


--
-- Name: medicoes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.medicoes_id_seq', 12, true);


--
-- Name: metas_indicadores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.metas_indicadores_id_seq', 72, true);


--
-- Name: movimentacoes_caixa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movimentacoes_caixa_id_seq', 26, true);


--
-- Name: movimentacoes_estoque_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.movimentacoes_estoque_id_seq', 12, true);


--
-- Name: obras_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.obras_id_seq', 13, true);


--
-- Name: orcamentos_base_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.orcamentos_base_id_seq', 13, true);


--
-- Name: ordens_compra_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.ordens_compra_id_seq', 13, true);


--
-- Name: perfil_permissao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.perfil_permissao_id_seq', 72, true);


--
-- Name: perfis_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.perfis_id_seq', 34, true);


--
-- Name: permissoes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.permissoes_id_seq', 288, true);


--
-- Name: projetos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projetos_id_seq', 13, true);


--
-- Name: registro_ponto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.registro_ponto_id_seq', 12, true);


--
-- Name: revisoes_projeto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.revisoes_projeto_id_seq', 14, true);


--
-- Name: sessoes_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.sessoes_usuario_id_seq', 12, true);


--
-- Name: tokens_refresh_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.tokens_refresh_id_seq', 12, true);


--
-- Name: usuario_perfil_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.usuario_perfil_id_seq', 13, true);


--
-- Name: usuarios_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.usuarios_id_seq', 13, true);


--
-- Name: utilizacoes_frota_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.utilizacoes_frota_id_seq', 12, true);


--
-- PostgreSQL database dump complete
--

\unrestrict kEnrZ1dLv3HQOEk7klLjRNlyjZ1tNceI9xCh8dnetOuQktOD6kPV77QjasNVjma

