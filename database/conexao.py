import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="host",
        user="root",
        password="senha",
        database="barbearia"
    )