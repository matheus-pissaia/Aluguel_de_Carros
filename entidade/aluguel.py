from entidade.cliente import Cliente
from entidade.carro import Carro
from entidade.funcionario import Funcionario
from datetime import date


class Aluguel:

    def __init__(self, cliente: Cliente, funcionario: Funcionario, carro: Carro, codigo: int, data_aluguel: date):
        if cliente.idade <= 18:
            raise Exception("O Cliente precisa ter mais de 18 anos para alugar um carro")
        else:
            if isinstance(cliente, Cliente):
                self.__cliente = cliente
            else:
                raise Exception("Erro ao incluir o aluguel: Cliente inválido")

        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario
        else:
            raise Exception("Erro ao incluir o aluguel: Funcionário inválido")

        if isinstance(carro, Carro):
            self.__carro = carro
        else:
            raise Exception("Erro ao incluir o aluguel: Carro inválido")

        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(data_aluguel, date):
            self.__data_aluguel = data_aluguel

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def carro(self) -> Carro:
        return self.__carro

    @property
    def funcionario(self) -> Funcionario:
        return self.__funcionario

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def data_aluguel(self) -> date:
        return self.__data_aluguel

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @carro.setter
    def carro(self, carro: Carro):
        if isinstance(carro, Carro):
            self.__carro = carro

    @funcionario.setter
    def funcionario(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @data_aluguel.setter
    def data_aluguel(self, data_aluguel: date):
        if isinstance(data_aluguel, date):
            self.__data_aluguel = data_aluguel
