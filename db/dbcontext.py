import sqlite3
import pandas as pd

def get_conexao():
    return sqlite3.connect("db/pacientes.db")

def criar_tabela():
    with get_conexao() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gender TEXT NOT NULL,
                age INTEGER,
                hypertension INTEGER,
                heart_disease INTEGER,
                ever_married TEXT NOT NULL,
                work_type TEXT NOT NULL,
                residence_type TEXT NOT NULL, 
                avg_glucose_level REAL,
                bmi REAL NOT NULL,
                smoking_status TEXT NOT NULL,
                stroke INTEGER
            )
        """)
        conexao.commit()
        conexao.close()
