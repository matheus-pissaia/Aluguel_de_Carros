class Funcionario(Pessoa):
    def __init__(self, cpf, nome, idade, matricula: int, cargo: str):
        super().__init__(cpf, nome, idade)
        self.__matricula = matricula
        self.__cargo = cargo

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
