import sqlite3
from sqlite3 import sql


class Banco():
    database = 'produtos.db'
    conn = None
    cursor = None
    connected = False

    # conecta com o banco de dados
    def connect(self):
        Banco.conn = sql.connect(Banco.database)
        Banco.cursor = Banco.conn.cursor()
        Banco.connected = True

    # desconecta o banco de dados
    def disconnect(self):
        Banco.conn.close()
        Banco.connected = False

    # executar comando no banco de dados
    def execute(self, sql, params = None):
        if Banco.connected:
            if params == None:
                Banco.cursor.execute(sql)
            else:
                Banco.cursor.execute(sql, params)
            return True
        else:
            return False
        
    # valores recebidos
    def fetchall(self):
        return Banco.cursor.fetchall()
    
    # commit
    def persist(self):
        if Banco.connected:
            Banco.cursor.commit()
            return True
        else:
            return False

    # Criar db
def InitDB():
    trans = Banco()
    trans.connect() 
    trans.execute('CREATE TABLE IF NOT EXISTS produto(
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
    trans.persist()
    trans.disconnect()

InitDB()

# Visualizar dados
def view():
    trans = Banco()
    trans.connect()

    trans.execute('SELECT * FROM produto')

    rows = trans.fetchall()
    trans.disconnect()
    return rows

