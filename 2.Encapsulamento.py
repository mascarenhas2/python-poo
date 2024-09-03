import os

os.system("cls || clear") 

#Criando sua propria excecao (erros)
class SaldoInsuficienteError(Exception):
    pass
class ValorNegativoError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int,) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 199 # "_" protege o atributo.
   
    @property
    def saldo(self):
        return self._saldo  

    def sacar(self, valor) -> float:
        # try - except
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro:{error}"

        self._saldo -= valor
        return self._saldo
   
    def __verificar_sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.") #lancando um erro

    def depositar(self, valor: float):
        try:
            self.__verificar_depositar(valor)
        except ValorNegativoError as error:
            return f"Erro: {error}"

        
        self._saldo += valor
        return self._saldo
    
    def __verificar_depositar(self,valor):
        if valor < 0 or valor <= 0:
            raise ValorNegativoError("Não é possivel depositar esse valor.")

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass
        

#instanciar classe:       
conta_corrente = ContaCorrente(3333,3333)
conta_poupanca = ContaPoupanca(4444,5554)

print(f"Saldo: {conta_corrente.saldo}")

# print(conta_corrente.sacar(200))
print(conta_corrente.depositar(-10))
