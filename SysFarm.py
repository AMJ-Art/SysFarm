#Grupo: Artur Mesquita Jaeger & João Paulo da Silva Franceschi

import defs
from classeEstoque import Estoque

Est1 = Estoque("Armazem geral")
Est2 = Estoque("Estoque de pedidos")

while(1):

    print()
    print("----------------------------------------------------------------------")
    print("-------------------------------- MENU --------------------------------")
    print("-- Digite para acessar: (1)Listar (2)Adicionar (3)Modificar (0)Sair --")
    print("----------------------------------------------------------------------")
    print()

    tag = input()
    
    match tag:

        case '1' | 'listar':
            defs.listar((defs.selectEst(Est1, Est2)))

        case '2' | 'adicionar':
            defs.adicionar(defs.selectEst(Est1, Est2))

        case '3' | 'modificar':
            defs.modificar(defs.selectEst(Est1, Est2))

        case '0':
            print("Você saiu do programa.")
            break
