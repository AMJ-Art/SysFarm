#Grupo: Artur Mesquita Jaeger & João Paulo da Silva Franceschi

import classeProduto
import defs

ListaEstoque = []

"""
 "Clonasepa - Preta", "Ibuprofeno - Amarela", "Pringles", "Barra de cereal", "Creme - Nivea", "esmalte laranja", "Papel Higiênico",   "Pasta de Dente"
"""

while(1):

    print("----------------------------- MENU -----------------------------")
    print("Digite para acessar: (1)Listar (2)Adicionar (3)Modificar (0)Sair")
    print("----------------------------------------------------------------")
    tag = input()
    
    match tag:

        case '1' | 'listar':
            defs.listar(ListaEstoque)

        case '2' | 'adicionar':
            defs.adicionar(ListaEstoque)

        case '3' | 'modificar':
            defs.modificar(ListaEstoque)

        case '0':
            print("Saiu")
            break
