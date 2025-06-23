FROM python:3.12.3

WORKDIR /app

COPY ingestao/ingestao.py .
COPY data/vendas.csv /data/vendas.csv
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "ingestao.py"]
