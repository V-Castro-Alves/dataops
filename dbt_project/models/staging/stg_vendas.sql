SELECT
    id,
    data,
    produto,
    loja,
    valor
FROM {{ source('public', 'vendas') }}
