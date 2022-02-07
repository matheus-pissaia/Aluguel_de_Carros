from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: int, idade: int, email: str):
        super().__init__(nome, cpf, telefone)
        if isinstance(idade, int):
            self.__idade = idade
        if isinstance(email, str):
            self.__email = email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email):
        if isinstance(email, str):
            self.__email = email

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            if idade > 0:
                self.__idade = idade
            else:
                raise Exception("Entre com um valor positivo!")
