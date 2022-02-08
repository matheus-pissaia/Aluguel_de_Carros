from limite.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario

class ControladorFuncionarios():

    def __init__(self, controlador_sistema):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_sistema = controlador_sistema

    def pega_funcionario_por_cpf(self, cpf: int):
        for funcionario in self.__funcionarios:
            if(funcionario.cpf == cpf):
                return funcionario
            return None

    def inicia(self):
        self.tela_inicial()

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"])
        self.__funcionarios.append(funcionario)

    def alterar_funcionario(self):
        self.listar_funcionario()
        cpf_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)

        if(funcionario is not None):
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            funcionario.nome = novos_dados_funcionario["nome"]
            funcionario.cpf = novos_dados_funcionario["cpf"]
            funcionario.telefone = novos_dados_funcionario["telefone"]
            self.listar_funcionario()
        else:
            self.__tela_funcionario.mostrar_mensagem("funcionario não existente")


    def excluir_funcionario(self):
        self.listar_funcionario()
        cpf_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)

        if (funcionario is not None):
            self.__funcionarios.remove(funcionario)
            self.listar_funcionario()
        else:
            self.__tela_funcionario.mostrar_mensagem("funcionario não existente")

    def listar_funcionario(self):
        for funcionario in self.__funcionarios:
            self.__tela_funcionario.mostra_funcionario({"nome": funcionario.nome, "cpf": funcionario.cpf, "telefone": funcionario.telefone})


    def encerrar_sistema(self):
        exit(0)

    def tela_inicial(self):
        caso = {0: self.encerrar_sistema, 1: self.incluir_funcionario, 2: self.excluir_funcionario,
                3: self.listar_funcionario, 4: self.alterar_funcionario}

        while True:
            opcao = self.__tela_funcionario.exibe_opcoes()
            opcao_escolhida = caso[opcao]
            opcao_escolhida()
