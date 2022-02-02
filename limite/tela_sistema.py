from abstract_tela import AbstractTela


class TelaSistema(AbstractTela):

    def tela_opcoes(self):
        print("----- Sistema Aluguel -----")
        print("Escolha sua opção:")
        print("1 - Carros")
        print("2 - Clientes")
        print("3 - Funcionários")
        print("4 - Aluguéis")
        print("0 - Finalizar Sistema")

        opcao = self.verifica_opcao("Digite a opção: ", [1, 2, 3, 4, 0])

        return opcao
