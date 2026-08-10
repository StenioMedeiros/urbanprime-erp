# Localização brasileira do UrbanPrime ERP

O sistema utiliza português do Brasil na interface e o fuso `America/Recife`, correspondente ao horário de Garanhuns/PE (UTC−3). Para o usuário, esse horário é identificado como **Horário de Brasília**.

## Regras aplicadas

- Datas: `DD/MM/AAAA`.
- Datas com horário: `DD/MM/AAAA HH:MM`.
- Competências: `MM/AAAA` na apresentação e `AAAA-MM` no banco, preservando a ordenação.
- Moeda: real brasileiro, como `R$ 1.234,56`.
- Números: ponto para milhar e vírgula para decimais.
- CPF, CNPJ, CEP e telefone: máscaras brasileiras na entrada e na apresentação.
- Estados: seleção pelas 27 siglas oficiais das unidades federativas.
- Novos endereços: Garanhuns/PE como referência inicial, ainda permitindo alteração.
- Situações e códigos internos: armazenados sem acentos para integração, mas apresentados em português legível.

## Horários técnicos

Cada conexão PostgreSQL configura explicitamente o fuso definido em `APP_TIMEZONE`. Isso evita diferenças quando o sistema for executado em outro computador ou servidor.

Os horários operacionais visíveis, como último acesso e auditoria, seguem o horário local configurado. Datas internas dos tokens JWT continuam em UTC, conforme o padrão técnico de segurança, e não são apresentadas ao usuário.

## Configuração

```env
APP_TIMEZONE=America/Recife
APP_LOCALE=pt_BR
APP_CURRENCY=BRL
DEFAULT_CITY=Garanhuns
DEFAULT_STATE=PE
```

Se a empresa passar a operar em outra localidade, essas variáveis permitem alterar a referência sem modificar as regras de negócio.
