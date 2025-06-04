#É uma classes de agregação

from classeProduto import Produto, Remedio, Higiene, Alimenticio

class Estoque:
    def __init__(self, nome):
        
        self.nome = nome
        self.produtos = []

    def addProduto(self, Produto):
        self.produtos.append(Produto)
