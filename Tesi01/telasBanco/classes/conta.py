class Conta:
    def __init__(self, numero, cliente, saldo):
        self.__numero = numero
        self.__titular = cliente
        self.__saldo = saldo

class ContaPoupanca(Conta):
    def poupanca(self):
        pass

class ContaCorrente(Conta):
    def corrente(self):
        desconto = 0.0025
          
