#Grupo: Artur Mesquita Jaeger & João Paulo da Silva Franceschi

import ClasseProduto

def main():

    ListaEstoque = []

    """
    "Merthiolate - esprei", "Clonasepa - Preta", "Ibuprofeno - Amarela", "Pringles", "Barra de cereal", "Creme - Nivea", "esmalte laranja", "Papel Higiênico", "Pasta de Dente"
    """

    print("------------------------ Menu ------------------------")
    print("Digite para acessar: (1)Listar (2)Adicionar (3)Alterar")
    print("------------------------------------------------------")

    while(1):

        valor = input()

        def switch(valor):
            match valor:

                case 1:
                    listar()

                case 2:
                    adicionar()

                case 3:
                    alterar()
                    

def listar():
    pass

def adicionar():
    pass

def alterar():
    pass
