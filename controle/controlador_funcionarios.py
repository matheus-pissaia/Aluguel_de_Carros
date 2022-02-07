class ControladorFuncionarios:
    def __init__(self):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__funcionario = []

    def inicia(self):
        self.tela_inicial()

    def incluir_funcionario(self):
        continuar = "s"
        while continuar == "S"  or continuar == "s":
            while True:
                try:
                    a = int(input("CPF: "))
                    break
                except ValueError:
                    print("Seu CPF deve conter apenas numeros!")
                print("Digite novamente:")
            b = str(input("Nome: "))
            while True:
                try:
                    c = int(input("Idade: "))
                    break
                except ValueError:
                    print("Somente numeros")
                print("Tente novamente")
            while True:
                try:
                    d = int(input("Matricula: "))
                    break
                except ValueError:
                    print("Somente numeros, repita!")
                print("Matricula: ")
            e = str(input("Cargo: "))
            funcionario = Funcionario(a, b, c, d, e)

            if funcionario not in self.__funcionario and isinstance(funcionario, Funcionario):
                self.__funcionario.append(funcionario)

            continuar = str(input("S/s pra continuar. 0 voltar"))

    def excluir_funcionario(self, funcionario: Funcionario):
        for func in self.__funcionario:
            print(self.__funcionario)
        if isinstance(funcionario, Funcionario) and (funcionario in self.__funcionario):
            self.__funcionario.remove(funcionario)

    def listar_funcionario(self):
        print("Funcionarios cadastrados: ")
        for funcionarios in self.__funcionario:
            return funcionarios
        return None

    def buscar_funcionario(self):
        print("Buscar um funcionario ")

        matricula = int(input("Matricula do funcionario: "))
        for funcionario in self.__funcionario:
            if Funcionario.matricula == matricula:
                return funcionario
            return "Funcionario não encontrado"

    def encerrar_sistema(self):
        exit(0)

    def tela_inicial(self):
        caso = {0: self.encerrar_sistema, 1: self.incluir_funcionario, 2: self.excluir_funcionario,
                3: self.listar_funcionario, 4: self.buscar_funcionario}

        while True:
            opcao = self.__tela_funcionario.exibe_opcoes()
            opcao_escolhida = caso[opcao]
            opcao_escolhida()
