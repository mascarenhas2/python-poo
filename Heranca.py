from abc import ABC, abstractmethod
import os

os.system("cls || clear") #limpa terminal.

class Funcionario(ABC):
    def __init__ (self, nome:str, idade:int, salario: float) -> None:
        self.nome = nome 
        self.idade = idade
        self.salario = salario 

    @abstractmethod    
    def calcular_salario(self) -> float:
        pass    

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
            # Acrescimo de 20%
            BONIFICACAO = 1.1
            salarioFinal = self.salario * BONIFICACAO
            return salarioFinal
    def __str__(self) -> str:
         return f"nome: {self.nome} idade: {self.idade} salario:{self.salario}
        
class Motoboy(Funcionario):
    def __init__(self, nome: str, cnh: str ,idade: int, salario: float) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    def calcular_salario(self) -> float:
        # Acrescimo de 20%
        BONIFICACAO = 1.1
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal
    def __str__(self) -> str:
         return f"nome: {self.nome} idade: {self.idade} Salario: {self.calcular_salario()}"
        

gerente1 =  Gerente("Claudio",23,1000.0)
motoboy1 =  Motoboy("junior","2343434",20,500.0)

print(gerente1)
print(motoboy1)
