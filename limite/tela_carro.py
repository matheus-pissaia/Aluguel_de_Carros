from abstract_tela import AbstractTela

class TelaCarro(AbstractTela):
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
        print("-------- RESERVAR CARRO --------")
        print("1 - Pegar Chave")
        print("2 - Devolver Chave")
        print("3 - Descricao de Emprestimo")
        print("4 - Devolucao de Chave")
        print("5 - Relatorio de Emprestimo")
        print("0 - Voltar")
        opcao = self.le_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
        return opcao
