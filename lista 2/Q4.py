from pprint import pprint


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        if (peso > self.peso):
            self.peso = 0
        else:
            self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def envelhecer(self, anos):
        anosAntes = self.idade
        self.idade += anos
        if (anosAntes < 25):
            if (self.idade < 25):
                self.crescer(anos * 0.5)
            else:
                self.crescer((25 - anosAntes) * 0.5)


pessoa = Pessoa('Zé', 19, 75.0, 180)
pprint(vars(pessoa))
pessoa.engordar(1)
pprint(vars(pessoa))
pessoa.emagrecer(2)
pprint(vars(pessoa))
pessoa.crescer(3)
pprint(vars(pessoa))
pessoa.envelhecer(7)
pprint(vars(pessoa))
