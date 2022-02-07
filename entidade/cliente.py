from Modelo.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, cpf, nome, idade, email: str, telefone: int):
        super().__init__(cpf, nome, idade)
        self.__email = email
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
