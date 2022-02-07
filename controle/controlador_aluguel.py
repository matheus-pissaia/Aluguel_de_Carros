import datetime

from entidade.aluguel import Aluguel
from limite.tela_aluguel import TelaAluguel

from random import randint


class ControladorAlugueis:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alugueis = []
        self.__carros_alugados = []
        self.__carros_disponiveis = []
        self.__tela_aluguel = TelaAluguel()

    def lista_alugueis(self):
        for a in self.__alugueis:
            self.__tela_aluguel.mostra_alugueis({
                "codigo": a.codigo,
                "cliente": a.cliente.nome,
                "funcionario": a.funcionario.nome,
                "carro": a.carro.modelo,
                "data_aluguel": a.data_aluguel
            })

    def busca_aluguel_por_codigo(self, codigo: int):
        for aluguel in self.__alugueis:
            if aluguel.codigo == codigo:
                return aluguel

            return None

    def mostra_carros_alugados(self):
        for carro in self.__carros_alugados:
            self.__tela_aluguel.mostra_carros_alugados({
                "placa": carro.placa,
                "modelo": carro.modelo
            })

    # Implementar método
    def mostra_carros_disponiveis(self):
        pass

    # Falta fazer as verificações e tratamento de exceções
    def incluir_aluguel(self):
        dados_aluguel = self.__tela_aluguel.pega_dados_aluguel()

        carro = self.__controlador_sistema.\
            controlador_carros.pega_carro_por_placa(dados_aluguel["carro"])

        cliente = self.__controlador_sistema.\
            controlador_clientes.pega_cliente_por_cpf(dados_aluguel["cpf_cliente"])

        funcionario = self.__controlador_sistema.\
            controlador_funcionarios.pega_funcionario_por_cpf(dados_aluguel["cpf_funcionario"])

        try:
            aluguel = Aluguel(cliente, funcionario, carro, randint(0, 1000), datetime.date.today())

            self.__alugueis.append(aluguel)
            self.__carros_alugados.append(carro)

        except Exception as e:
            self.__tela_aluguel.mostra_mensagem(e)

    def excluir_aluguel(self):
        self.lista_alugueis()

        codigo_aluguel = self.__tela_aluguel.seleciona_aluguel()
        aluguel = self.busca_aluguel_por_codigo(codigo_aluguel)

        if aluguel is not None:
            self.__alugueis.remove(aluguel)
            self.lista_alugueis()

        else:
            self.__tela_aluguel.mostra_mensagem("Erro: Aluguel não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_aluguel,
            2: self.excluir_aluguel,
            3: self.lista_alugueis,
            4: self.mostra_carros_disponiveis,
            5: self.mostra_carros_alugados,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_aluguel.mostra_opcoes()]()
