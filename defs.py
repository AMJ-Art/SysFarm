from classeProduto import Remedio, Higiene, Alimenticio
from classeEstoque import Estoque

#Pacote de funções

# Listar os produtos armazenados
def listar(list):
    i = 0
    
    for produto in list.produtos:
        i += 1
        if  (type(produto) == Higiene):
            print(f"Código {i:>2}:  Nome:{produto.nome:<30} Valor:{produto.valor:>6}  Quantidade:{produto.qtd:>3}  {produto.esp()}:NULL")
        elif(type(produto) == Remedio):
            print(f"Código {i:>2}:  Nome:{produto.nome:<30} Valor:{produto.valor:>6}  Quantidade:{produto.qtd:>3}  {produto.esp()}:{produto.tarja}")
        elif(type(produto) == Alimenticio):
            print(f"Código {i:>2}:  Nome:{produto.nome:<30} Valor:{produto.valor:>6}  Quantidade:{produto.qtd:>3}  {produto.esp()}:{produto.validade}")
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
    print          ("O Produto foi criado com sucesso!")
    qtdEstoque     (objeto.qtd, objeto.nome)

    return 0

# Intarface de escolha entre modificar ou colocar produto em promoção
def modificar(list):
    print()
    print("---------------------------------------------------------------------")
    print("------ Modificar um produto(1) ----- adicionar uma promoção(2) ------")
    print()

    tag = input()
    match tag:
        case "1":
            modProduto(list)
        case "2":
            promocao  (list)

# Modifca um Objeto
def modProduto(list):

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

#Cria um objeto do tipo Produto(Sem subClasse)
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

#Usado para verificar se a String não é apenas números
def verificaNum(valor):
    
    if(type(valor) == int | type(valor) == float):
       return True
    return False

#Usado para verificar se não é int ou float
def verificaFloat(input):

    try:
        float(input)
        print(f"Erro: {input} é um nome inadequado")
        print("Por favor, reinicie a operação...")
        return 'erro'

    except ValueError as e:
        return input

# Faz um insert de produtos padrões
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

#Regra de negócio(1): aviso quando há pouca quantidade de determinado produto no estoque
def qtdEstoque(qtd, nome):
    if(qtd < 4):
        print(f"Aviso: pouca quantidade de {nome}, apenas {qtd} no estoque")

#Regra de negócio(2): Muda os preços dos produtos, os colocando em promoção
def promocao(list):

    print()
    desc = float(input("Insira o valor equivalente do desconto: "))

    print()
    print("Digite o(s) produto(s) que serão afetados: ")
    tags  = input()

    listaTags = tags.split()

    for i in listaTags:
        for j in list:
            if(i == j.nome):
                j.valor = calculoPromo(desc, j.valor)

# Calcula o valor da porcentagem
def calculoPromo(perc, valor):
    valor = valor - (valor * (perc * 0.01))
    return valor
