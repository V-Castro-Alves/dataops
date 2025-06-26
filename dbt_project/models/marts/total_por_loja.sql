SELECT
    loja,
    SUM(valor) AS total_vendido
FROM {{ ref('stg_vendas_filtrado') }}
GROUP BY loja
