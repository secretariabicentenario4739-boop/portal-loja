import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE usuarios (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
email TEXT,
senha TEXT,
grau TEXT
)
""")

cursor.execute("""
CREATE TABLE atas (
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT,
data TEXT,
arquivo TEXT
)
""")

cursor.execute("""
INSERT INTO usuarios (nome,email,senha,grau)
VALUES ('Administrador','admin@loja.com','123','mestre')
""")

conn.commit()
conn.close()

print("Banco criado")