-- Test to verify that all required fields have values
SELECT
    id
FROM {{ ref('stg_vendas') }}
WHERE 
    data IS NULL OR
    produto IS NULL OR
    loja IS NULL OR
    valor IS NULL