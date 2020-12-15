import sqlite3

database = 'produtos.db'

conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS produto(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_produto VARCHAR(50) NOT NULL,
    marca VARCHAR(20),
    unidade VARCHAR(10),
    localizao_estoque VARCHAR(30),
    estoque_minimo INTEGER,
    estoque_maximo INTEGER,
    peso_kg REAL,
    valor_venda REAL,
    valor_custO REAL,
    tamanho_produto INTEGER,
    origem VARCHAR(40),
    classificao VARCHAR(40),
    situacao VARCHAR(10),
    tipo VARCHAR(10),
    fornecedor VARCHAR(30),
    estoque_inicial INTEGER,
)')