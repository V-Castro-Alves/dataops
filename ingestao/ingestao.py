import os
import pandas as pd
import psycopg2
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CSVHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if os.path.basename(event.src_path) == "vendas.csv":
            print("vendas.csv changed, updating database...")
            ingest_csv_to_db()

def ingest_csv_to_db():
    try:
        df = pd.read_csv('/data/vendas.csv')
        conn = psycopg2.connect(
            host="postgres",
            database="dataops",
            user="postgres",
            password="postgres"
        )
        cur = conn.cursor()
        
        # Use DROP CASCADE to handle dependent objects like views
        cur.execute("DROP TABLE IF EXISTS vendas CASCADE")
        
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
        print("Database updated.")
    except Exception as e:
        print(f"Error updating database: {e}")

if __name__ == "__main__":
    ingest_csv_to_db()  # Initial load
    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, path="/data", recursive=False)
    observer.start()
    print("Watching /data/vendas.csv for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()