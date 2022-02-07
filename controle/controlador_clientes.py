from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente


class ControladorClientes:
    def __init__(self):
        self.__tela_cliente = TelaCliente(self)
        self.__clientes = []

    def inicia(self):
        self.tela_inicial()

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()

        try:
            cliente = Cliente(
                dados_cliente["nome"],
                dados_cliente["cpf"],
                dados_cliente["telefone"],
                dados_cliente["idade"]
            )

            self.__clientes.append(cliente)

        except Exception as e:
            self.__tela_cliente.mostra_mensagem(e)

    def excluir_cliente(self, cliente: Cliente):
        for cliente in self.__cliente:
            print(cliente)
        if isinstance(cliente, Cliente) and (cliente in self.__cliente):
            self.__cliente.remove(cliente)

    def listar_clientes(self):
        print("Clientes cadastrados no sistema: ")
        for cliente in self.__cliente:
            print(cliente)

    def buscar_cliente_por_cpf(self, cpf_cliente: int):
        cpf_cliente = self.__tela_cliente.seleciona_cliente()

        for cliente in self.__cliente:
            if cliente.cpf == cpf_cliente:
                self.__tela_cliente.mostra_cliente({
                    "nome": cliente.nome,
                    "cpf": cliente.cpf,
                    "telefone": cliente.telefone,
                    "idade": cliente.idade
                })
            return None

    def encerrar_sistema(self):
        exit(0)

    def tela_inicial(self):
        caso = {0: self.encerrar_sistema, 1: self.incluir_cliente, 2: self.excluir_cliente,
                3: self.listar_clientes, 4: self.buscar_cliente_por_cpf, 5: self.encerrar_sistema}

        while True:
            opcao = self.__tela_cliente.exibe_opcoes()
            opcao_escolhida = caso[opcao]
            opcao_escolhida()
