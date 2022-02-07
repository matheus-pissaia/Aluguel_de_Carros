from abc import ABC


class AbstractTela(ABC):

    def verifica_opcao(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            opcao_str = input(mensagem)

            try:
                opcao_int = int(opcao_str)

                if inteiros_validos and opcao_int not in inteiros_validos:
                    raise ValueError

                return opcao_int
            

            except ValueError:
                print("Valor incorreto: Digite um número inteiro positivo válido")
                if inteiros_validos:
                    print("Opções válidas: ", inteiros_validos)
