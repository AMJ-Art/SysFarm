#Pacote de funções

import classeProduto
from classeProduto import Produto, Remedio, Higiene, Alimenticio, Beleza

def listar(lista):
    for produto in lista:
        print(f"Produto:  N:", produto.nome, " V:", produto.valor, " Q:", produto.qtd, " T:", produto.tarja)

def adicionar(lista):
    print("Criando um objeto...")

    nome   = input('Insira um nome: ')
    valor  = input('Insira o valor: ')
    qtd    = input('Insira a quantidade: ')
    tipo   = input('Insira o tipo do produto: ')

    match tipo:
        case 'Remedio' | 'remedio':
            tarja  = input('Insira o tarja: ')
            objeto = Remedio(nome, valor, qtd, tarja)
            
        case 'Higiene' | 'higiene':
            tipoH = input('Insira tipo de especialização do produto')
            objeto = Higiene(nome, valor, qtd, tipoH)

        case 'Alimenticio' | 'alimenticio':
            validade = input('Insira a validade do produto')
            objeto = Alimenticio(nome, valor, qtd, validade)

        case 'Beleza' | 'beleza':
            tipoB = input('Insira o tipo de produto')
            objeto = Beleza(nome, valor, qtd, tipoB)

    lista.append(objeto)
    print("O objeto foi criado e adicionado na lista")

    return 0

def verificaNum(valor):
    if(type(valor) == int | type(valor) == float):
        return True
    return False

def modificar(lista):
    pass