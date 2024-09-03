from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro : str, numero: int, cidade : str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                f"\nCidade: {self.cidade}"        
                 )
    
class Funcionario(ABC):
    def __init__(self, nome: str, email : str, salario : float, endereco: Endereco) -> None:
        return (f"\nNome: {self.nome}"
                f"\nEmail: {self.email}"
                f"\nSalario: {self.salario}"
                f"\nEndereco: {self.endereco}"
                )
    
    @abstractmethod
    def salario                                             