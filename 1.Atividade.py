from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__ (self, logradouro: str, numero: str, complemento: str, cep : str, cidade: str):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade


    def exibir_endereco(self) -> str:
        return f"Logradouro: {self.logradouro} \nNumero: {self.numero} \nComplemento: {self.complemento} \nCep: {self.cep} \nCidade: {self.cidade}"
    
class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome})"
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"\nSalario: {self.salario_final()}"
                f"\nEndereco:{self.endereco.exibir_endereco()}")
            
class Engenheiro(Funcionario):
    def __init__(self, nome:str, telefone:str, email:str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return 2000.0
        
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return 5000.0

print("\n=== Dados do engenheiro ===")
engenheiro2 = Engenheiro("Caio","22442","caiovin55@gmail.com","re242",
                         Endereco("Rua caralinhos","2324","fundo","403010564","Salvador"))
print(engenheiro2)

print("\n=== Dados do medico ===")
medico2 = Medico("Caio","23242","caio@gmail.com","rrre234",
                Endereco("rua imbativel","72","Fundo","232333","Guarulhos"))

print(medico2)

    