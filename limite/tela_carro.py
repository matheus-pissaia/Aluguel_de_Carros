from limite.abstract_tela import AbstractTela


class TelaCarro(AbstractTela):
    def tela_opcoes(self):
        print("-------- Carros ----------")
        print("Escolha a opcao")
        print("1 - Incluir Carro")
        print("2 - Alterar Carro")
        print("3 - Listar Carro")
        print("4 - Excluir Carro")
        print("0 - Retornar")

        opcao = int(input("Escolha uma opcao: "))
        return opcao

    def pega_dados_carro(self):
        print("-------- DADOS CARRO ----------")
        modelo = input("Modelo: ")
        placa = input("Placa: ")

        return {"modelo": modelo, "placa": placa}

    def mostra_carro(self, dados_carro):
        print("MODELO DO CARRO: ", dados_carro["modelo"])
        print("PLACA DO CARRO: ", dados_carro["placa"])
        print("\n")

    def seleciona_carro(self):
        placa = input(" Placa do carro que deseja selecionar: ")
        return placa

    def mostra_mensagem(self, msg):
        print(msg)
