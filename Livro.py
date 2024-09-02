import os

os.system("cls || clear")


class Livro:
    def __init__(self,titulo:str, autor:str,numeroPag:int, preco:float):
        self.titulo = titulo
        self.autor = autor 
        self.numeroPag = numeroPag
        self.preco = preco 
    

    #criando funcao para exibir
    def exibir_resultados(self) -> str:
        return f"Titulo do livro: {self.titulo} \nAutor do livro: {self.autor} \nNumero de paginas: {self.numeroPag} \nPreco: {self.preco}"
    
informacoes1 = Livro("Primo rico", "Luquinhas boladao", "230","120.80")
informacoes2 = Livro("Diario de um banana","Cedric","233","232.00")

print(f"=== Exibindo Resultados ===")

print(informacoes1.exibir_resultados())
print(informacoes2.exibir_resultados())