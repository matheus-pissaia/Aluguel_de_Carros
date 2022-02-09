from limite.tela_carro import TelaCarro
from entidade.carro import Carro


class ControladorCarros:

  def __init__(self, controlador_sistema):
    self.__carros = []
    self.__controlador_sistema = controlador_sistema
    self.__tela_carro = TelaCarro()

  def pega_carro_por_placa(self, placa: str):
    for carro in self.__carros:
      if(carro.placa == placa):
        return carro
    return None

  def incluir_carro(self):
    dados_carro = self.__tela_carro.pega_dados_carro()
    carro = Carro(dados_carro["placa"], dados_carro["modelo"])
    self.__carros.append(carro)

  def alterar_carro(self):
    self.lista_carro()
    placa_carro = self.__tela_carro.seleciona_carro()
    carro = self.pega_carro_por_placa(placa_carro)

    if(carro is not None):
      novos_dados_carro = self.__tela_carro.pega_dados_carro()
      carro.modelo = novos_dados_carro["modelo"]
      carro.placa = novos_dados_carro["placa"]
      self.lista_carro()
    else:
      self.__tela_carro.mostra_mensagem("carro não existente")

  def lista_carro(self):
    for carro in self.__carros:
      self.__tela_carro.mostra_carro({"modelo": carro.modelo, "placa": carro.placa})

  def excluir_carro(self):
    self.lista_carro()
    placa_carro = self.__tela_carro.seleciona_carro()
    carro = self.pega_carro_por_placa(placa_carro)

    if(carro is not None):
      self.__carros.remove(carro)
      self.lista_carro()
    else:
      self.__tela_carro.mostra_mensagem(" carro não existente ")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_carro, 2: self.alterar_carro, 3: self.lista_carro, 4: self.excluir_carro, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_carro.tela_opcoes()]()
