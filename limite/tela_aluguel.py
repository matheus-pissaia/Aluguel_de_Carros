from limite.abstract_tela import AbstractTela


class TelaAluguel(AbstractTela):

    def mostra_opcoes(self):
        print("----- ALUGUÉIS -----")
        print("Escolha sua opção:")
        print("1 - Incluir Aluguel")
        print("2 - Excluir Aluguel")
        print("3 - Listar Aluguéis")
        print("4 - Listar Carros Disponíveis")
        print("5 - Listar Carros Alugados")
        print("0 - Retornar")

        opcao = self.verifica_opcao("Digite a opção: ", [1, 2, 3, 4, 5, 6, 0])

        return opcao

    def mostra_alugueis(self, dados_aluguel):
        if dados_aluguel is not None:
            print("CÓDIGO ALUGUEL: ", dados_aluguel["código"])
            print("CLIENTE QUE ALUGOU: ", dados_aluguel["cliente"])
            print("FUNCIONÁRIO RESPONSÁVEL: ", dados_aluguel["funcionario"])
            print("CARRO ALUGADO: ", dados_aluguel["modelo"])
            print("DATA DO ALUGUEL: ", dados_aluguel["data_aluguel"])
            print("\n")
        else:
            print("Não há nenhum aluguel registrado.")

    def mostra_carros_disponiveis(self, dados_carros_disponiveis):
        if dados_carros_disponiveis is not None:
            print("----- CARROS DISPONIVEIS -----")
            print("PLACA: ", dados_carros_disponiveis["placa"])
            print("MODELO: ", dados_carros_disponiveis["modelo"])
            print("\n")

        else:
            print("----- CARROS DISPONIVEIS -----")
            print("Não há carros disponíveis.")
            print("\n")

    def mostra_carros_alugados(self, dados_carros_alugados):
        if dados_carros_alugados is not None:
            print("PLACA: ", dados_carros_alugados["placa"])
            print("MODELO: ", dados_carros_alugados["modelo"])

        else:
            print("Não há carros alugados ainda.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def pega_dados_aluguel(self):
        print("----- DADOS ALUGUEL -----")
        placa = int(input("Placa do Carro: "))
        cpf_cliente = int(input("CPF do Cliente: "))
        cpf_funcionario = int(input("CPF do Funcionário: "))

        return {"placa": placa, "cpf_cliente": cpf_cliente, "cpf_funcionario": cpf_funcionario}

    def seleciona_aluguel(self):
        codigo = int(input("Código do aluguel que deseja selecionar: "))

        return codigo
