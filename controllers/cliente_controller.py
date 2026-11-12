from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository

class ClienteController:
    def __init__(self):
        #vai criar uma conexao entre controller e repository
        self.repository = ClienteRepository()

    def cadastrar_novo_cliente(self, nome, telefone):
         if not nome.strip() or not telefone.strip():
            raise ValueError("Por gentileza, preencha todos os campos da tela!")

         novo_cliente = Cliente(nome=nome, telefone=telefone)
         self.repository.inserir(novo_cliente)


