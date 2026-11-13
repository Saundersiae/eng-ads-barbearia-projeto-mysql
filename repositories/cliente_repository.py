import mysql.connector
from database.conexao import conectar

class ClienteRepository:

    def inserir_clientes(self, cliente):
        #cadastrar clientes
        conexao = None 
        cursor = None
        try:
            conexao = conectar()
            cursor = conexao.cursor()

            sql = "INSERT INTO clientes (nome, telefone, servicos_id) VALUES (%s, %s, %s)"
            valores = (cliente.nome, cliente.telefone, cliente.servicos_id)

            cursor.execute(sql, valores)
            conexao.commit()
            return True

        except mysql.connector.Error as erro:
            if conexao:
                 conexao.rollback()
            raise erro
        

        finally:
           if cursor:
              cursor.close()

           if conexao:
              conexao.close()

    def listar_clientes(self):
        # listar todos os clientes cadastradoss
        conexao = None
        cursor = None
        try:
           conexao = conectar()
           cursor = conexao.cursor()

           sql = "SELECT * FROM clientes"
           cursor.execute(sql)

           clientes = cursor.fetchall()
           return clientes

        except mysql.connector.Error as erro:
            raise erro

        finally:
            if cursor:
                cursor.close()

            if conexao:
                conexao.close()


    def alterar_dados(self, id, nome, telefone, servicos_id):
        # alterar dados dos clientes
        conexao = None
        cursor = None

        try:

        
           conexao = conectar()
           cursor = conexao.cursor()

           sql = "UPDATE clientes SET nome = %s, telefone = %s, servicos_id = %s WHERE id = %s"
           valores = (nome, telefone, servicos_id, id)

           cursor.execute(sql, valores)
           conexao.commit()

           return cursor.rowcount # retorna o número de linhas afetadas

        except mysql.connector.Error as erro:
            if conexao:
                 conexao.rollback()
            raise erro
        finally:
          if cursor:
            cursor.close()

          if conexao:
            conexao.close()

    def excluir_cliente(self, id):
       # excluir cliente
       conexao = None
       cursor = None
       try:
          conexao = conectar()
          cursor = conexao.cursor()

          sql = "DELETE FROM clientes WHERE id = %s"
          valores = (id,)

          cursor.execute(sql, valores)
          conexao.commit()
          return cursor.rowcount


       except mysql.connector.Error as erro:
           if conexao:
                conexao.rollback()
           raise erro

       finally:
        if cursor:
            cursor.close()

        if conexao:
            conexao.close()