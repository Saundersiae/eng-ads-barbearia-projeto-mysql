from database.conexao import conectar
from models.cliente import Cliente

class ClienteRepository:
    def inserir(self, cliente):
        conexao = conectar()
        cursor = conexao.cursor()

# %S obrigatorio
        sql = "INSERT INTO clientes (nome, telefone) VALUES (%s, %s)"
        valores = (cliente.nome, cliente.telefone)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()