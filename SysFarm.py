#Grupo: Artur Mesquita Jaeger & João Paulo da Silva Franceschi

import defs
from classeEstoque import Estoque

Est1 = Estoque("Armazem geral")
Est2 = Estoque("Estoque de pedidos")

defs.insertInicial(Est1)

while(1):

    print("--------------------------- MENU DE SELEÇÃO ----------------------------")
    print("---------- Selecione em qual estoque será efetuada a operação ----------")
    print("------------- Armazem Geral(1) ----- Estoque de pedidos(2) -------------")
    print("------------------------------ Sair(0) ---------------------------------")
    print()

    list0 = input()
    match   list0:

        case '1':
            list0 = Est1
        case '2':
            list0 = Est2
        case '0':
            print("Saiu do programa")
            break

    while(1):
    
        print("------------------------------------------------------------------------")
        print("-------------------------------- MENU ----------------------------------")
        print("-- Digite para acessar: (1)Listar (2)Adicionar (3)Modificar (0)Voltar --")
        print("------------------------------------------------------------------------")
        print()

        tag = input()
        match tag:

            case '1' | 'listar':
                defs.listar(list0)
            case '2' | 'adicionar':
                defs.adicionar(list0)
            case '3' | 'modificar':
                defs.modificar(list0)
            case '0':
                break