#conexao com banco de dados
import sqlite3
from contextlib import contextmanager
import os

# Função de conexão com o banco
@contextmanager
def get_db_connection():
    conn = sqlite3.connect("feature_store.db")
    conn.row_factory = sqlite3.Row  # Formatação dos resultados como dicionário
    try:
        yield conn
    finally:
        conn.close()