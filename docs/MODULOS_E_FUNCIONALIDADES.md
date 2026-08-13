# UrbanPrime ERP — Módulos e funcionalidades

## 1. Objetivo deste documento

Este documento apresenta, em linguagem simples, os módulos disponíveis no UrbanPrime ERP e explica para que serve cada funcionalidade do sistema.

O menu está dividido em nove áreas principais:

1. Dashboard;
2. Administrativo e Segurança;
3. Comercial;
4. Engenharia e Projetos;
5. Gestão de Obras;
6. Financeiro;
7. Compras e Estoque;
8. Frota e Equipamentos;
9. Recursos Humanos.

## 2. Recursos comuns das telas

Nas telas de cadastro e movimentação, o usuário pode, conforme suas permissões:

- consultar os registros existentes;
- pesquisar por informações fáceis de reconhecer, como nome, descrição ou número;
- aplicar filtros para reduzir os resultados;
- cadastrar um novo registro;
- editar um registro existente;
- excluir um registro quando a regra de negócio permitir;
- visualizar primeiro os registros mais recentes;
- relacionar informações sem precisar memorizar os códigos internos do banco.

## 3. Dashboard

O Dashboard é a central de acompanhamento gerencial do sistema. No topo da página, o usuário escolhe qual painel deseja consultar sem precisar sair dessa área.

### Painéis da central

- **Executivo — disponível:** consolida faturamento, recebimentos, gastos, caixa, carteira de contratos, obras, quadro de funcionários, estoque, frota, tendências, projeções e pontos de atenção. Os indicadores comparam o período selecionado com o período imediatamente anterior.
- **Financeiro e Fluxo de Caixa — disponível:** apresenta visão geral financeira, faturamento acumulado, rentabilidade, despesas, entradas e saídas, contas e vencimentos, metas e projeções. Pode ser filtrado por período, obra, cliente e categoria de despesa.
- **Obras e Engenharia — disponível:** consolida situação das obras, avanço físico, responsáveis, crescimento da carteira, cronograma, prazos, orçamento, custos, medições, chamados técnicos e revisões de projeto. Possui filtros por período, obra, responsável e situação, ranking gerencial e alertas de inconsistência cadastral.
- **Compras e Fornecedores — disponível:** consolida ordens de compra, valores em processamento e recebidos, andamento por situação, compras por obra, cotações, economia negociada, itens e desempenho dos fornecedores. Possui filtros por período, fornecedor, obra e situação, ranking gerencial, concentração de compras, prazo médio de recebimento e alertas de inconsistência cadastral.
- **Estoque — disponível:** apresenta saldos atuais, valor armazenado, estoque mínimo, entradas, saídas, consumo por obra, cobertura estimada, materiais sem movimentação e compras aguardando recebimento. Possui filtros por período, material, obra e tipo de movimentação, além de ranking gerencial e alertas de reposição.
- **Frota e Maquinário — próxima etapa:** reservado para disponibilidade, utilização, manutenção, combustível e custos.
- **Recursos Humanos — próxima etapa:** reservado para quadro de pessoal, folha, jornada, alocações e produtividade.

As projeções e os alertas são análises transversais. Projeções aparecem nos painéis Executivo e Financeiro; alertas específicos de prazo, execução, estoque e qualidade de dados aparecem também em Obras e Engenharia, Compras e Fornecedores e Estoque.

### Funcionalidades

- **Indicadores executivos:** apresenta faturamento, recebimentos, gastos, saldo operacional, obras, contratos, funcionários, estoque e frota.
- **Comparação entre períodos:** mostra crescimento ou queda em relação ao período anterior equivalente.
- **Tendências:** permite acompanhar faturamento, lucro ou perda, saldo de caixa e crescimento da quantidade de obras ao longo do tempo, sem considerar lançamentos futuros como realizados.
- **Projeções:** estima os próximos seis meses com base no histórico registrado. A projeção serve como apoio gerencial e não como garantia de resultado.
- **Pontos de atenção:** destaca obras atrasadas, contas vencidas, materiais críticos e equipamentos em manutenção.
- **Acompanhamento de compras:** apresenta ordens abertas, aprovadas e recebidas, valor aguardando recebimento, evolução mensal, compras por obra e ordens há mais de 30 dias sem recebimento.
- **Desempenho dos fornecedores:** mostra participação no valor comprado, concentração nos maiores fornecedores, quantidade de cotações e ordens, valor em aberto e prazo médio de recebimento.
- **Cotações e itens:** compara cotação e ordem vinculada, calcula a economia estimada e apresenta os itens adquiridos, mantendo os totais dos itens separados quando houver divergência cadastral.
- **Saúde do estoque:** compara o saldo atual com o estoque mínimo, calcula o valor armazenado e classifica cada material como adequado, sem saldo, abaixo do mínimo, em risco ou sem movimentação.
- **Cobertura estimada:** utiliza as saídas registradas nos últimos 30 dias para estimar o saldo futuro e os dias até o estoque mínimo. Quando não há consumo recente, o painel informa que não existe base suficiente para a previsão.
- **Movimentações e reposição:** apresenta entradas e saídas por período e obra, histórico detalhado e materiais vinculados a ordens de compra ainda abertas ou aprovadas.
- **Auditoria recente:** mostra as últimas atividades realizadas no sistema.

## 4. Administrativo e Segurança

Este módulo controla quem pode entrar no sistema, o que cada pessoa pode fazer e o histórico das operações realizadas.

### Gestão de usuários

Cria e administra as contas usadas para entrar no UrbanPrime ERP. Cada usuário pode ser vinculado a um funcionário e receber um ou mais perfis de acesso.

Principais usos:

- criar o nome de usuário e a senha de acesso;
- ativar ou desativar uma conta;
- vincular a conta ao funcionário correspondente;
- atribuir perfis ao usuário;
- consultar o último acesso realizado.

### Gestão de perfis

Define grupos de permissões, como Administrador, Financeiro, Engenharia ou Compras. O perfil determina quais áreas e ações ficam disponíveis para os usuários associados a ele.

Principais usos:

- criar perfis de acesso;
- definir as permissões de cada perfil;
- liberar ou restringir visualização, cadastro, edição e exclusão;
- reutilizar o mesmo conjunto de permissões para vários usuários.

**Diferença importante:** o usuário identifica a pessoa que entra no sistema; o perfil representa o conjunto de acessos concedidos a essa pessoa.

### Auditoria

Registra o histórico de segurança e das alterações efetuadas no ERP.

Principais usos:

- consultar logins realizados e tentativas de acesso;
- identificar quem criou, editou ou excluiu um registro;
- verificar data e horário da operação;
- consultar os dados anteriores e os dados novos de uma alteração;
- filtrar o histórico por usuário, módulo, ação ou período.

## 5. Comercial

Este módulo organiza o relacionamento inicial com o cliente, desde o cadastro e as visitas até a formalização do contrato.

### Clientes

Mantém o cadastro das pessoas físicas ou jurídicas atendidas pela empresa. O cliente é usado como referência em contratos, faturamento, contas a receber, projetos e análises financeiras.

### Contratos

Registra os acordos firmados com os clientes, incluindo número, valor, período e situação. O contrato serve de base comercial para o desenvolvimento do projeto e da obra.

### Agenda de visitas

Organiza visitas comerciais ou técnicas relacionadas aos clientes. Permite registrar data, horário, local, responsável, objetivo e situação da visita.

## 6. Engenharia e Projetos

Este módulo controla o desenvolvimento técnico que acontece depois da contratação e antes ou durante a execução da obra.

### Projetos

Registra os projetos vinculados aos contratos. Permite identificar o projeto pelo nome, tipo, descrição, responsável, datas e situação de desenvolvimento.

### Revisões de projeto

Mantém o histórico das versões e alterações técnicas de cada projeto. Evita que uma revisão anterior seja confundida com a versão atualmente aprovada para execução.

## 7. Gestão de Obras

Este módulo acompanha o planejamento, a execução, o orçamento e os acontecimentos de cada obra.

### Obras

Representa a execução física contratada. A obra pode ser vinculada ao cliente, contrato e projeto e contém informações como nome, endereço, período, situação e avanço físico.

### Cronogramas

Planeja as atividades e etapas da obra. Permite informar datas previstas, percentual concluído, peso da atividade e situação, facilitando a comparação entre o planejado e o executado.

### Diários de obra

Registra o que ocorreu diariamente no canteiro, incluindo atividades executadas, clima, equipe, ocorrências e observações. Funciona como memória operacional da obra.

### Medições

Registra a quantidade ou o valor do serviço executado em determinada competência. A medição normalmente passa pelas situações:

- **Pendente:** foi registrada, mas ainda aguarda análise;
- **Aprovada:** foi conferida e aceita, mas ainda pode não ter sido faturada;
- **Faturada:** gerou uma fatura ou documento de cobrança;
- **Recebida:** o pagamento do cliente foi efetivamente confirmado, quando esse controle estiver relacionado ao financeiro.

### Chamados técnicos

Controla problemas, solicitações e necessidades técnicas relacionados às obras. Permite informar prioridade, solicitante, responsável, situação e solução adotada.

### Orçamentos-base

Registra o orçamento oficial aprovado para a obra. Ele representa o valor planejado e serve de referência para comparar o custo previsto com o realizado.

### Itens do orçamento

Detalha o orçamento-base por etapa, categoria, material, serviço, quantidade e valor. Permite identificar onde o recurso foi planejado e analisar desvios durante a execução.

## 8. Financeiro

Este módulo reúne faturamento, receitas, despesas, caixa, custos, contas e análises financeiras da empresa.

### Área financeira

É a visão gerencial consolidada do módulo. Reúne informações de diferentes setores para analisar:

- faturamento bruto e líquido;
- custos operacionais;
- investimentos;
- lucro ou perda;
- margem financeira;
- saldo de caixa;
- despesas por categoria e origem;
- rentabilidade por obra, projeto ou cliente;
- séries históricas e projeções.

### Categorias financeiras

Forma o plano gerencial de receitas e despesas. Classifica cada lançamento, por exemplo, como material, mão de obra, combustível, manutenção, imposto ou receita de serviços.

### Centros de custo

Identifica a área responsável por um gasto ou receita. Pode representar uma obra, a administração, a frota ou outro setor, permitindo saber onde o recurso foi utilizado.

### Contas bancárias

Mantém as contas usadas pela empresa e seus saldos de referência. São utilizadas nas movimentações de caixa e na conciliação financeira.

### Faturas

Registra os documentos de faturamento emitidos para os clientes. Uma fatura representa um valor cobrado, mas não significa necessariamente que o dinheiro já foi recebido.

### Movimentações de caixa

Registra entradas e saídas efetivamente realizadas nas contas bancárias. É nessa funcionalidade que o sistema reconhece a movimentação real do dinheiro.

### Custos por obra

No sistema, esta funcionalidade aparece como **Apropriações de custo**. Ela atribui um custo realizado a uma obra, categoria e centro de custo, podendo também relacioná-lo a uma conta a pagar, ordem de compra, funcionário ou equipamento.

### Metas e indicadores

Registra objetivos financeiros ou operacionais por período. Permite comparar valores planejados com resultados realizados, como faturamento, margem, custo ou quantidade de obras.

### Contas a pagar

Controla as obrigações financeiras da empresa, como fornecedores, impostos, serviços, compras e outras despesas. Permite acompanhar vencimento, pagamento e situação.

### Contas a receber

Controla os valores que a empresa tem a receber de clientes. Pode ser relacionado a contrato, obra, medição ou faturamento e permite acompanhar vencimento e recebimento.

## 9. Compras e Estoque

Este módulo controla fornecedores, pesquisa de preços, compras, materiais armazenados e consumo nas obras.

### Fornecedores

Mantém o cadastro das empresas e profissionais que fornecem materiais ou serviços. O fornecedor pode ser relacionado a cotações, ordens de compra e contas a pagar.

### Cotações

Registra propostas e preços apresentados pelos fornecedores. Ajuda a comparar alternativas antes de autorizar uma compra.

### Ordens de compra

Formaliza a compra aprovada, indicando fornecedor, obra, datas, valores e situação. A ordem pode originar uma conta a pagar.

### Itens das ordens de compra

Detalha os materiais ou serviços incluídos em cada ordem, com quantidade, unidade e valor unitário.

### Insumos

Mantém o cadastro dos materiais utilizados pela empresa, suas unidades de medida, quantidades atuais e níveis mínimos de estoque.

### Movimentações de estoque

Registra entradas e saídas de insumos. Permite identificar quando um material foi recebido, consumido, transferido ou destinado a determinada obra.

## 10. Frota e Equipamentos

Este módulo acompanha veículos, máquinas e equipamentos utilizados pela empresa e pelas obras.

### Frotas

Mantém o cadastro de cada veículo ou equipamento, incluindo identificação, tipo, marca, modelo, situação, aquisição e obra de utilização.

### Manutenções da frota

Registra manutenções preventivas, corretivas ou preditivas, com datas, descrição, custo e ocorrência. Os custos podem alimentar as análises financeiras.

### Abastecimentos da frota

Controla combustível, quantidade abastecida, valor, quilometragem ou horímetro e obra relacionada. Permite analisar consumo e custo por equipamento.

### Utilização da frota

Registra as horas de uso, o custo por hora e a obra em que o equipamento trabalhou. Ajuda a calcular o custo operacional de máquinas e veículos.

## 11. Recursos Humanos

Este módulo organiza os colaboradores, a jornada, a folha e a distribuição das equipes pelas obras.

### Funcionários

Mantém o cadastro profissional e pessoal dos colaboradores, incluindo cargo, setor, admissão, contato, salário-base e situação. Um funcionário não precisa ter acesso ao sistema; para isso, é necessário criar também um usuário.

### Registro de ponto

Registra a jornada de trabalho, como entrada, saída para intervalo, retorno e encerramento do expediente.

### Folha de pagamento

Controla a remuneração por competência, incluindo salário bruto, descontos e salário líquido. Os valores podem participar da análise de custos da empresa e das obras.

### Alocação das equipes

Define em qual obra cada funcionário trabalha, sua função, período de atuação e percentual de dedicação. Essa relação permite distribuir corretamente os custos de mão de obra.

## 12. Fluxo resumido entre os módulos

O fluxo principal do UrbanPrime ERP pode ser entendido da seguinte forma:

1. O **Comercial** cadastra o cliente, agenda visitas e formaliza o contrato.
2. **Engenharia e Projetos** cria o projeto e controla suas revisões.
3. **Gestão de Obras** abre a obra, planeja o cronograma e o orçamento e registra a execução.
4. **Compras e Estoque** seleciona fornecedores, realiza compras e controla os materiais.
5. **Frota e Equipamentos** registra o uso, abastecimento e manutenção das máquinas.
6. **Recursos Humanos** aloca funcionários, registra jornadas e calcula a folha.
7. O **Financeiro** consolida faturamento, despesas, custos, pagamentos, recebimentos e caixa.
8. O **Dashboard** transforma os registros dos módulos em indicadores e tendências.
9. **Administrativo e Segurança** controla o acesso e registra todas as operações relevantes na auditoria.

## 13. Regra geral de utilização

Para que as análises sejam confiáveis, cada setor deve registrar suas operações no módulo correspondente e manter os vínculos corretos com cliente, contrato, projeto, obra, fornecedor, funcionário ou equipamento. Quanto mais completos forem esses relacionamentos, mais precisos serão os custos por obra, a rentabilidade, o fluxo de caixa e os indicadores apresentados no Dashboard.
