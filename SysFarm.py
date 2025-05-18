#Grupo: Artur Mesquita Jaeger & João Paulo da Silva Franceschi

from datetime import date

#adicionar data nos produtos alimenticios

class Produto:

    nome    = "sem nome"
    valor   = 0
    qtd     = 0

    def __init__(self, nome, valor, qtd):
        self.nome   =  nome
        self.valor  = valor
        self.qtd    =   qtd

class Remedios(Produto):

    TarjasValidas = {"Indefinida", "Amarela", "Vermelha", "Preta"}

    def __init__(self, nome, valor, qtd, tarja = "Indefinida"):
        super().__init__(nome, valor, qtd) # 'super' é utilizado para chamar o método pai

        if tarja not in self.TarjasValidas:
            raise ValueError(f"Tarja invalida. Use uma destas: {self.TarjasValidas}")
        
        self.tarja = tarja

class Higiene(Produto):

    tipoProd = {"pessoal", "intima", "bucal"}

    def __init__(self, nome, valor, qtd, tipo):
        super().__init__(nome, valor, qtd)

        if tipo not in self.tipoProd:
            raise ValueError(f"Tipo invalido. Use uma destes: {self.tipoProd}")

        self.tipo = tipo

class Alimenticios(Produto):

    def __init__(self, nome, valor, qtd, validade = "Deve-se atualizar"):
        super().__init__(nome, valor, qtd)
        self.validade = validade

class Maquiagem(Produto):

    def __init__(self, nome, valor, qtd):
        super().__init__(nome, valor, qtd)


RemedioTeste = Remedios("Paracetamol", 20.00, 40, "Amarela")

print(RemedioTeste.nome,' ', RemedioTeste.valor, ' ', RemedioTeste.qtd, ' ', RemedioTeste.tarja)

#Comentario