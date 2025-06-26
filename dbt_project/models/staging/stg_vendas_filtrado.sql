SELECT
    id,
    data,
    produto,
    loja,
    valor
FROM {{ source('public', 'vendas') }}
WHERE valor >= 0
  AND id IS NOT NULL
  AND data IS NOT NULL
  AND produto IS NOT NULL
  AND loja IS NOT NULL
  AND valor IS NOT NULL