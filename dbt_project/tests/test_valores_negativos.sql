-- Test to verify that valor is not negative
SELECT
    id,
    data,
    valor
FROM {{ ref('stg_vendas') }}
WHERE valor < 0