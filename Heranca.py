from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        # Acréscimo de 10%
        BONIFICACAO = 1.1
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSalário: {self.calcular_salario():.2f}"

class Motoboy(Funcionario):
    def __init__(self, nome: str, cnh: str, idade: int, salario: float) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        # Acréscimo de 10%
        BONIFICACAO = 1.1
        salarioFinal = self.salario * BONIFICACAO
        return salarioFinal

    def __str__(self) -> str:
        return f"\nNome: {self.nome}\nIdade: {self.idade}\nSalário: {self.calcular_salario():.2f}\nCNH: {self.cnh}"

# Instanciando os objetos
gerente1 = Gerente("Claudio", 23, 1000.0)
motoboy1 = Motoboy("Junior", "2343434", 20, 500.0)

# Exibindo as informações
print(gerente1)
print(motoboy1)