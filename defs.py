#Pacote de funções

import classeProduto
from classeProduto import Produto, Remedio, Higiene, Alimenticio, Beleza

def listar(lista):
    for produto in lista:
        print(f"Produto:  N:", produto.nome, " V:", produto.valor, " Q:", produto.qtd, " T:", produto.tarja)

def adicionar(lista):
    print("Criando um objeto...")

    nome  = input('Insira um nome: ')
    valor = input('Insira o valor: ')
    qtd   = input('Insira a quantidade: ')
    tarja  = input('Insira o tarja: ')
    objeto = Remedio(nome, valor, qtd, tarja)

    lista.append(objeto)
    print("O objeto foi criado e adicionado na lista")

    return 0

def alterar():
    pass