from database.conexao import conectar

class ServicosRepository:
    def listar_todos(self):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, nome, preco FROM servicos"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados