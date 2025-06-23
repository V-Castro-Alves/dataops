SELECT *
FROM {{ ref('stg_vendas') }}
WHERE valor IS NULL
