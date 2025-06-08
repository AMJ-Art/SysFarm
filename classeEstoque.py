#É uma classes de agregação

from classeProduto import Produto, Remedio, Higiene, Alimenticio

#Classe Estoque (5), pode armazenar objetos de outras classes
class Estoque:
    def __init__(self, nome):

        self.nome = nome
        self.produtos = []

    def addProduto(self, Produto):
        self.produtos.append(Produto)

    def __iter__(self):
        return iter(self.produtos)