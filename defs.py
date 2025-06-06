from classeProduto import Remedio, Higiene, Alimenticio
from classeEstoque import Estoque
import warnings

#Pacote de funções

def selectEst(list1, list2):
    print("----------------------------------------------------")
    print("Selecione em qual estoque sera efetuada a operação: ")
    print("---- Armazem Geral(1) --- Estoque de pedidos(2) ----")
    print("")
    list0 = input()

    match list0:
        case '1':
            return list1
        case '2':
            return list2

# Listar os produtos armazenados
def listar(list):
    i = 0
    for produto in list.produtos:
        i += 1
        if  (type(produto) == Higiene):
            print(f"Código {i:>2}:  Nome:{produto.nome:<30} Valor:{produto.valor:>6}  Quantidade:{produto.qtd:>3}  Especialidade:NULL")
        elif(type(produto) == Remedio):
            print(f"Código {i:>2}:  Nome:{produto.nome:<30} Valor:{produto.valor:>6}  Quantidade:{produto.qtd:>3}  Especialidade:{produto.tarja}")
        elif(type(produto) == Alimenticio):
            print(f"Código {i:>2}:  Nome:{produto.nome:<30} Valor:{produto.valor:>6}  Quantidade:{produto.qtd:>3}  Especialidade:{produto.validade}")
        else:
            ValueError("Erro: produto adicionado incorretamente!")

    return 0

# Adiciona um produto a lista
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
            objeto   = Higiene(nome, valor, qtd)

        case 'alimenticio':
            validade = input('Insira a validade do produto: ')
            objeto   = Alimenticio(nome, valor, qtd, validade)
    
    list.addProduto(objeto)
    print("O objeto foi criado e adicionado na lista")
    qtdEstoque(objeto.qtd)

    return 0

# Modifica um objeto na lista
def modificar(list):
    print("---------------------------------------------------------------------")
    print("Escolha se deseja modificar um produto(1) ou adicionr uma promoção(2)")
    tag = input()

    match tag:
        case "1":
            modProduto()
        case "2":
            promocao()

def modProduto():

    obj = input("Escreva o nome do produto que desaja alterar: ")

    for i in list.produtos:
        if(i.nome == obj): 
            print("---")
            print(f"Produto: {i.nome} Valor: {i.valor} Quantidade: {i.qtd}")
            option = input("Selecione qual dado deseja modificar: ")
            print("---")

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
                    qtdEstoque(i.qtd)

        else:
            print("Produto não encontrado")

# Cria um objeto do tipo Produto(Sem subClasse)
def criaObj():
    try:
        nome   = input('Insira um nome: ')
        if((verificaFloat(nome)) == 'erro'):
            raise ValueError()
        
        valor  = (float(input('Insira o valor: ')))
        qtd    = (int(input('Insira a quantidade: ')))

        tipo   = (input('Insira o tipo do produto: '))
        if((verificaFloat(tipo)) == 'erro'):
            raise ValueError()

        return nome,valor,qtd,tipo
        
    except ValueError as e:
        print("Erro: valores de inserção inválidos!")
        return None

# Usado para verificar se a String não é apenas números
def verificaNum(valor):
    if(type(valor) == int | type(valor) == float):
       return True
    return False

# Usado para verificar se não é int ou float
def verificaFloat(input):
    try:
        float(input)
        print(f"Erro: {input} é um nome inadequado")
        print("Por favor, reinicie a operação...")
        return 'erro'
    
    except ValueError as e:
        return input

def insertInicial(list):

    list.addProduto(Remedio('Clonazepam', 20.99, 5, 'preta'))
    list.addProduto(Remedio('Paracetamol', 11.99, 16, 'amarela'))
    list.addProduto(Remedio('Ibuprofeno', 28.99, 8, 'amarela'))

    list.addProduto(Alimenticio('Pringles', 18.99, 5, '12/12/2035'))
    list.addProduto(Alimenticio('Barra de cereal - Nutry', 18.99, 10, '12/12/2028'))
    list.addProduto(Alimenticio('Pastilha - Valda', 19.99, 6, '12/12/2034'))

    list.addProduto(Higiene('Papel higiênico - 20 unidades', 22.99, 8))
    list.addProduto(Higiene('Pasta de dente - Colgate', 5.00, 12))

    return list

#adicionar seguintes regras de negócios: def de promoções & def de dispara aviso quando pouco produto em estoque

#Regra de negócio(1): verificação de quantidade do estoque
def qtdEstoque(qtd):
    if(qtd < 4):
        warnings.warn(f"Aviso: pouca quantidade de {qtd}", UserWarning)

#Regra de negócio(2): Muda os preços dos produtos, os colocando em promoção
def promocao():

    print("Qual produto ou classificação deseja alterar?")
    tag = input()

