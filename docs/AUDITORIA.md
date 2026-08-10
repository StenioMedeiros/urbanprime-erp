# Auditoria e histórico de atividades

O UrbanPrime ERP registra uma nova linha em `logs_auditoria` para cada atividade relevante. O campo `usuarios.ultimo_login` continua existindo apenas como resumo do acesso mais recente e não representa o histórico.

## Eventos registrados

- login realizado;
- tentativa de login sem sucesso;
- saída do sistema;
- criação de registros;
- edição de registros, com dados anteriores e novos;
- exclusão pela API, preservando os dados anteriores;
- criação de usuários e perfis;
- alteração da situação de usuários;
- vínculo de permissões aos perfis.

As operações genéricas do Streamlit e da API passam pelo mesmo repositório, portanto clientes, contratos, projetos, obras, financeiro, compras, estoque, frota e recursos humanos seguem a mesma regra.

## Segurança

Senhas, hashes, tokens, chaves secretas e chaves de criptografia nunca são copiados para `dados_anteriores` ou `dados_novos`.

## Consulta

A tela **Administrativo e Segurança → Auditoria** oferece:

- listagem geral das atividades mais recentes;
- histórico específico de acessos;
- pesquisa por usuário, módulo, ação ou descrição;
- consulta dos dados anteriores e novos de cada alteração.

Os registros são ordenados do mais recente para o mais antigo e usam o horário brasileiro configurado no sistema.
