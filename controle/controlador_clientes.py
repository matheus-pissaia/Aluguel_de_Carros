class ControlaCliente:
    def __init__(self):
        self.__tela_cliente = TelaCliente(self)
        self.__cliente = []

    def inicia(self):
        self.tela_inicial()

    def incluir_cliente(self):
        continuar = "s"
        while continuar == "S" or continuar == "s":
            while True:
                try:
                    a = int(input("CPF: "))
                    break
                except ValueError:
                    print("CPF deve conter apenas numeros!")
                print("Digite novamente:")
            b = str(input("Nome: "))
            while True:
                try:
                    c = int(input("Idade: "))
                    break
                except ValueError:
                    print("Somente numeros")
                print("Tente novamente")
            d = str(input("Email: "))
            while True:
                try:
                    e = str(input("Telefone: "))
                    break
                except ValueError:
                    print("Telefone deveria conter apenas numeros ")
                print("Digite novamente: ")
            cliente = Cliente(a, b, c, d, e)

            if cliente not in self.__cliente and isinstance(cliente, Cliente):
                self.__cliente.append(cliente)

            continuar = str(input("S/s pra continuar. 0 voltar"))

    def excluir_cliente(self, cliente: Cliente):
        for cliente in self.__cliente:
            print(cliente)
        if isinstance(cliente, Cliente) and (cliente in self.__cliente):
            self.__cliente.remove(cliente)

    def listar_clientes(self):
        print("Clientes cadastrados no sistema: ")
        for cliente in self.__cliente:
            print(cliente)

    def buscar_cliente(self):
        print("Buscar um cliente ")
        cpf = int(input("Digite o CPF: "))
        for cliente in self.__cliente:
            if Cliente.cpf == cpf:
                return cliente
            return  "Cliente não encontrado"

    def encerrar_sistema(self):
        exit(0)

    def tela_inicial(self):
        caso = {0: self.encerrar_sistema, 1: self.incluir_cliente, 2: self.excluir_cliente,
                3: self.listar_clientes, 4: self.buscar_cliente, 5: self.encerrar_sistema}

        while True:
            opcao = self.__tela_cliente.exibe_opcoes()
            opcao_escolhida = caso[opcao]
            opcao_escolhida()
