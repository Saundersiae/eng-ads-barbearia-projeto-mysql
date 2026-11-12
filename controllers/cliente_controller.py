from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository


class ClienteController:

    def __init__(self):
        self.repository = ClienteRepository()

    # cadastro do cliente
    def cadastrar_novo_cliente(self, nome, telefone, servicos_id):

        if not nome.strip() or not telefone.strip():
            raise ValueError("Preencha todos os campos!")

        if not str(servicos_id).isdigit():
            raise ValueError("Selecione um serviço válido!")

        novo_cliente = Cliente(
            nome=nome,
            telefone=telefone,
            servicos_id=int(servicos_id)
        )

        return self.repository.inserir_clientes(novo_cliente)


    def listar_clientes(self):
        # listar todos clientes
        return self.repository.listar_clientes()


    def alterar_cliente(self, id, nome, telefone, servicos_id):
        # alterar dados dosclientes

        if not str(id).isdigit():
            raise ValueError("Informe um ID válido!")

        if not nome.strip() or not telefone.strip():
            raise ValueError("Preencha todos os campos!")

        if not str(servicos_id).isdigit():
            raise ValueError("Selecione um serviço válido!")

        return self.repository.alterar_dados(
            int(id), nome, telefone, int(servicos_id)
        )

    def excluir_cliente(self, id):
        # excluir clientes
        if not str(id).isdigit():
            raise ValueError("Informe um ID válido!")

        return self.repository.excluir_cliente(int(id))