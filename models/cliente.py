class Cliente:
    def __init__(self, nome, telefone, servicos_id, id=None):
        self.id = id
        self.servicos_id = servicos_id
        self.nome = nome
        self.telefone = telefone 

