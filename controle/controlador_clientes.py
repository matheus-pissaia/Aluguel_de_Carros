from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente


class ControladorClientes:

    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()

    def pega_cliente_por_cpf(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["telefone"],
                          dados_cliente["idade"])
        self.__clientes.append(cliente)

    def alterar_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.telefone = novos_dados_cliente["telefone"]
            cliente.cpf = novos_dados_cliente["cpf"]
            cliente.idade = novos_dados_cliente["idade"]
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("cliente não existente")

    def lista_clientes(self):
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_cliente(
                {"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf, "idade": cliente.idade})

    def excluir_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente is not None:
            self.__clientes.remove(cliente)
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem(" cliente não existente ")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_clientes,
                        4: self.excluir_cliente,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
