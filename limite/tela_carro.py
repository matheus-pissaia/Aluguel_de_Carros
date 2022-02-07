from abstract_tela import AbstractTela


class TelaCarro(AbstractTela):
    def __init__(self, controlador):
        self.__controlador = controlador

    def exibe_opcoes(self):
        print("-------- RESERVAR CARRO --------")
        print("1 - Pegar Chave")
        print("2 - Devolver Chave")
        print("3 - Descricao de Emprestimo")
        print("4 - Devolucao de Chave")
        print("5 - Relatorio de Emprestimo")
        print("0 - Voltar")
        opcao = self.verifica_opcao("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])

        return opcao
