from limite.tela_sistema import TelaSistema
from controle.controlador_carros import ControladorCarros
from controle.controlador_clientes import ControladorClientes
from controle.controlador_funcionarios import ControladorFuncionarios
from controle.controlador_aluguel import ControladorAlugueis


class ControladorSistema:

    def __init__(self):
        self.__controlador_carros = ControladorCarros(self)
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_funcionarios = ControladorFuncionarios(self)
        self.__controlador_alugueis = ControladorAlugueis(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_clientes(self) -> ControladorClientes:
        return self.__controlador_clientes

    @property
    def controlador_carros(self) -> ControladorCarros:
        return self.__controlador_carros

    @property
    def controlador_funcionarios(self) -> ControladorFuncionarios:
        return self.__controlador_funcionarios

    def finaliza_sistema(self):
        exit(0)

    # Falta
    def abre_tela(self):
        lista_opcoes = {
            1: self.__controlador_carros,
            2: self.__controlador_clientes,
            3: self.__controlador_funcionarios,
            4: self.__controlador_alugueis.abre_tela,
            0: self.finaliza_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            executa_opcao_escolhida = lista_opcoes[opcao_escolhida]
            executa_opcao_escolhida()
