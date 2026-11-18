import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="seu host",
        user="root",
        password="sua senha",
        database="barbearia"
    )