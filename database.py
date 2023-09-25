import sqlite3

def create_database():
    conn = sqlite3.connect("employee_management.db")
    cursor = conn.cursor()

    # Criar tabela de funcionários
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    hourly_rate REAL NOT NULL)''')

    conn.commit()
    return conn
