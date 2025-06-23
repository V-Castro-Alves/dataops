import pandas as pd
import psycopg2

df = pd.read_csv('/data/vendas.csv')

conn = psycopg2.connect(
    host="postgres",
    database="dataops",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS vendas")
cur.execute("""
    CREATE TABLE vendas (
        id INT,
        data DATE,
        produto TEXT,
        loja TEXT,
        valor FLOAT
    )
""")

for _, row in df.iterrows():
    cur.execute("INSERT INTO vendas VALUES (%s, %s, %s, %s, %s)", tuple(row))

conn.commit()
cur.close()
conn.close()
