class Carro:
    
    def __init__(self, placa: str, modelo: str, cor: str):
        self.__placa = placa
        self.__modelo = modelo

    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, placa: str):
        if isinstance(placa, str):
            self.__placa = placa

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str):
        if isinstance(modelo, str):
            self.__modelo = modelo
