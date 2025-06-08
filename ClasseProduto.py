
class Produto:  #Super Classe(1)

    #Constructor(1)
    nome    = "sem nome"
    valor   = 0
    qtd     = 0

    def __init__(self, nome, valor, qtd): #Constructor(2)
        self.nome   =  nome
        self.valor  = valor
        self.qtd    =   qtd

    #Exemplo de substituição("def esp' funciona de modo diferente de acordo com cada subclasse)
    def esp(self):
        return "NULL"
        
#Sub classe Remedio (2)
class Remedio(Produto):

    TarjasValidas = {"indefinida", "amarela", "vermelha", "preta"}

    def __init__(self, nome, valor, qtd, tarja = "Indefinida"):
        super().__init__(nome, valor, qtd) # 'super' é utilizado para chamar o método pai

        if tarja not in self.TarjasValidas:
            raise ValueError(f"Tarja invalida. Use uma destas: {self.TarjasValidas}")
        
        self.tarja = tarja

    def esp(self):
        return "Tarja"

#Sub classe Higiene(3)
class Higiene(Produto):

    def __init__(self, nome, valor, qtd):
        super().__init__(nome, valor, qtd)

    def esp(self):
        return "NULL"

#Sub classe Alimenticio(4)
class Alimenticio(Produto):

    def __init__(self, nome, valor, qtd, validade = "Deve-se atualizar"):
        super().__init__(nome, valor, qtd)
        self.validade = validade

    def esp(self):
        return "Validade"