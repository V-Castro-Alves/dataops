SELECT
    id,
    data,
    produto,
    loja,
    valor
FROM {{ ref('stg_vendas_filtrado') }}   