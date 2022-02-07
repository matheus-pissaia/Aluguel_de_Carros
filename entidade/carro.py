class Carro:
    
    def __init__(self, placa: str, modelo: str):
        self.__placa = placa
        self.__modelo = modelo

    @property
    def placa_carro(self):
        return self.__placa
    @placa_carro.setter
    def placa_carro(self, placa):
        self.__placa = placa

    @property
    def modelo_carro(self):
        return self.__modelo
    @modelo_carro.setter
    def modelo_carro(self, modelo):
        self.__modelo = modelo
