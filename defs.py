
import classeProduto
from classeProduto import Remedio, Higiene, Alimenticio, Cosmetico

#Pacote de funções

#FAZER A POHA DOS ENCAPSULAMENTOS

#Listar os produtos armazenados
def listar(list):
    for produto in list:
        print(f"Produto:  N:", produto.nome, " V:", produto.valor, " Q:", produto.qtd, " T:", produto.tarja)
        return 0

#Adiciona um produto a lista
def adicionar(list):

    print("Criando um objeto na lista...")
    dados = criaObj()
    if(dados is not None):
        nome, valor, qtd, tipo = dados
    else:
        print("Por favor, reinicie a operação...")
        return 1

    match tipo.lower():
        case 'remedio':
            tarja    = (input('Insira o tarja: ')).lower()
            objeto   = Remedio(nome, valor, qtd, tarja)

        case 'higiene':
            tipoH    = input('Insira tipo de especialização do produto: ')
            objeto   = Higiene(nome, valor, qtd, tipoH)

        case 'alimenticio':
            validade = input('Insira a validade do produto: ')
            objeto   = Alimenticio(nome, valor, qtd, validade)

        case 'cosmetico':
            objeto   = Cosmetico(nome, valor, qtd)

    list.append(objeto)
    print("O objeto foi criado e adicionado na lista")
    return 0

#Modifica um objeto na lista (OBS: não pode alterar o tipo)
def modificar(list):
    print("----------------------------------------------")
    obj = input("Escreva o nome do produto que desaja alterar: ")

    for i in list:
        if(i.nome == obj): 
            print(f"Produto: {i.nome} Valor: {i.valor} Quantidade: {i.qtd}")
            option = input("Selecione qual dado deseja modificar: ")

            match option.lower():

                case 'nome':
                    dado = input("Coloque o novo nome: ")
                    i.nome = dado
                    print("Edição realizada com sucesso!")

                case 'valor':
                    dado = input("Coloque o novo valor: ")
                    i.valor = dado
                    print("Edição realizada com sucesso!")

                case 'quantidade':
                    dado = input("Coloque a nova quantidade: ")
                    i.qtd = dado
                    print("Edição realizada com sucesso!")
    
        else:
            print("Produto não encontrado")

#Cria um objeto do tipo Produto(Sem subClasse)
def criaObj():

    try:
        nome   = input('Insira um nome: ')
        if((verificaString(nome)) == 'erro'):
            raise ValueError()
        
        valor  = (float(input('Insira o valor: ')))
        qtd    = (int(input('Insira a quantidade: ')))

        tipo   = (input('Insira o tipo do produto: '))
        if((verificaString(tipo)) == 'erro'):
            raise ValueError()

        return nome,valor,qtd,tipo
        
    except ValueError as e:
        print("Erro: valores de inserção inválidos!")
        return None

#Usado para verificar se a String não é apenas números
def verificaNum(valor):
    if(type(valor) == int | type(valor) == float):
       return True
    return False

#Usado para verificar se não é int ou float
def verificaString(input):

    try:
        float(input)
        print(f"Erro: {input} é um nome inadequado")
        print("Por favor, reinicie a operação...")
        return 'erro'
    
    except ValueError as e:
        return input
    
#incompleto
def verificaTipo(input):

    tipos = ['remedio', 'higiene', 'alimenticio', 'cosmetico']

    try:
        print(f"Erro: {input} é um tipo inadequado")
        print("Por favor, reinicie a operação...")
        return 'erro'
    
    except ValueError as e:
        return input
