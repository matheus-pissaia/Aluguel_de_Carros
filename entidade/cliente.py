from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: int):
        super().__init__(cpf, nome):
        self.__telefone = telefone


    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
