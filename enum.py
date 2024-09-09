import os
from enum import Enum

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    
class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "RH"
    VENDAS = "Vendas"
    MARKETING = "Marketing"
    

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario : double, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo
    
    def __str__(self) -> str:
        "To string no java"
        return (f"\nId: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSalario: {self.salario}"
                f"\nSetor: {self.setor.value}"
                f"\nSexo: {self.sexo.value}"
                )

os.system("cls || clear")

funcionario1 = Funcionario(23,"Caio Lucas bdm",44,3000.0,)


                       
