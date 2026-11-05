import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_URL = (
    f"postgresql+psycopg://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}"
    f"@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
)
engine = create_engine(DB_URL)

import csv

# getcolumns name 
def get_columns(csv_path: str) -> list[str]:
    with open(csv_path, newline="", encoding="utf-8") as f:
        header = next(csv.reader(f))
    return [col.lower() for col in header]

# generate create table sql
def generate_create_table_sql(table_name: str, columns: list[str]) -> str:
    cols_sql = ",\n    ".join(f'"{col}" TEXT' for col in columns)
    return f'CREATE TABLE IF NOT EXISTS {table_name} (\n    {cols_sql}\n);'


def create_and_load(csv_path: str, table_name: str) -> None:
    columns = get_columns(csv_path)
    create_table_sql = generate_create_table_sql(table_name, columns)

    raw_conn = engine.raw_connection()
    try:
        with raw_conn.cursor() as cur:
            cur.execute(f'DROP TABLE IF EXISTS {table_name};')
            cur.execute(create_table_sql)

            copy_sql = f'COPY {table_name} FROM STDIN WITH (FORMAT csv, HEADER true)'
            with open(csv_path, "r", encoding="utf-8") as f, cur.copy(copy_sql) as copy:
                while data := f.read(8192):
                    copy.write(data)
        raw_conn.commit()
        print(f'Loaded {table_name} from {csv_path}')
    finally:
        raw_conn.close()

if __name__ == "__main__":
    create_and_load("data/raw/application_train.csv", "application_train")
    create_and_load('data/raw/bureau.csv', 'bureau')