import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="host",
        user="root",
        password="1234s",
        database="barbearia"
    )