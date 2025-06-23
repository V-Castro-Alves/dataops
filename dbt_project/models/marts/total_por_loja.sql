SELECT
    loja,
    SUM(valor) AS total_vendido
FROM {{ ref('stg_vendas') }}
GROUP BY loja
