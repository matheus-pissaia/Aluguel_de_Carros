from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: int, matricula: int):
        super().__init__(nome, cpf, telefone)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, int):
            self.__matricula = matricula
