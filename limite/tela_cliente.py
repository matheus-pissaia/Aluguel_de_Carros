from limite.abstract_tela import AbstractTela


class TelaCliente(AbstractTela):
    def __init__(self, controlador):
        self.__controlador = controlador


    def exibe_opcoes(self):
        print("-------- CADASTRO DE CLIENTES --------")
        print("1 -  Incluir novo cliente")
        print("2 -  Excluir  cliente")
        print("3 -  Listar  clientes")
        print("4 -  Buscar  um cliente")
        print("0 -  Voltar")
        opcao = self.verifica_opcao("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_cliente(self):
        print("----- DADOS CLIENTE -----")
        cpf = int(input("Cpf: "))
        nome = int(input("Nome: "))
        telefone = int(input("Telefone: "))
        idade = int(input("Idade: "))

        return {"cpf": cpf, "nome": nome, "telefone": telefone, "idade": idade}

    def mostra_cliente(self, dados_cliente):
        if dados_cliente is not None:
            print("NOME: ", dados_cliente["nome"])
            print("CPF: ", dados_cliente["cpf"])
            print("TELEFONE: ", dados_cliente["telefone"])
            print("IDADE: ", dados_cliente["idade"])

        else:
            print("Cliente não encontrado!")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def seleciona_cliente(self):
        cpf_cliente = int(input("CPF do cliente que deseja selecionar: "))

        return cpf_cliente
