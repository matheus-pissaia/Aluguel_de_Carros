class TelaCliente:
    def __init__(self, controlador):
        self.__controlador = controlador

    def le_inteiro(self, mensagem: str = "", inteiros_validos: [] = None ):
        while True:
            valor_lido = input(mensagem)

            try:
                inteiro = int(valor_lido)

                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro

            except ValueError:
                print("Valor incorreto, digite um inteiro valido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)

    def exibe_opcoes(self):
        print("-------- CADASTRO DE CLIENTES --------")
        print("1 -  Incluir novo cliente")
        print("2 -  Excluir  cliente")
        print("3 -  Listar  clientes")
        print("4 -  Buscar  um cliente")
        print("0 -  Voltar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao
