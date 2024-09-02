import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logradouro:str, numero:int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    # def exibir_endereco(self) -> str:
    
    def __str__(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNumero: {self.numero}"
        

class Aluno:
    def __init__(self,nome: str, idade: int, endereco : Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self) -> str:
         return f"\nNome: {self.nome} \nIdade: {self.idade}, \n Endereco: {self.endereco}"
     #def exibir_dados(self) -> str:
      #  return f"\nNome: {self.nome} \nIdade: {self.idade}, \n Endereco: {self.endereco}"

aluno1 = Aluno("Mascarenhas", 20,Endereco("Rua do dende","67") )
aluno2 = Aluno("Karol","24",Endereco("Rua sibirinha","3444"))

print(aluno1) 
print(aluno2)   
