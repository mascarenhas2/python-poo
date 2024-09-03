from abc import ABC, abstractmethod
import os

#criando erros
class SalarioNegativoError(Exception):
    pass

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
    def exibir_endereco(self) -> str:
        return f"Logradouro: {self.logradouro} \nNumero: {self.numero} \nCidade: {self.cidade}"
    
class Funcionario(ABC):
    def __init__(self, nome: str, email : str, salario : float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:  
        return (f"\nNome: {self.nome}"
                f"\nEmail: {self.email}"
                f"\nSalario: {self.salario}"
                f"\nEndereco: {self.endereco.exibir_endereco()}")
                
class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco) 

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nEmail: {self.email} \nSalario: {self.salario} Endereco: {self.endereco.exibir_endereco()}"     

class Motoboy(Funcionario):
    def __init__(self, nome: str,cnh: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

    def __str__(self) -> str:
        return f"\nNome: {self.nome} \nemail: {self.email} \nSalario: {self.salario} \nEndereco: {self.endereco.exibir_endereco}"

#instanciando os objetos
gerente1 = Gerente("william", "willa@gmail.com",4000,
                   Endereco("Rua sugas",23,"Salvador"))
print(gerente1)

motoboy1 = Motoboy("Lucas","A","Vander@gmail.com",-1000,
                   Endereco("Rua ponciano",23,"Salvador"))
print(motoboy1)