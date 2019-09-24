class Bichinho:

    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setFome(self, fome):
        self.fome = fome

    def getFome(self):
        return self.fome

    def setSaude(self, saude):
        self.saude = saude

    def getSaude(self):
        return self.saude

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def alimenta(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100.0)

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.saude += self.saude * (quantidade / 100.0)

    def getHumor(self):
        return self.getFome() * self.getSaude()

    def str(self):
        print('Nome:', self.getNome())
        print('Idade:', self.getIdade())
        print('Fome:', self.getFome())
        print('Saude:', self.getSaude())
        print('Humor:', self.getHumor())


# TESTE DA CLASSE
bichinho = Bichinho('Tamagoshi', 10, 10, 10)
print('Humor: %d' % bichinho.getHumor())
bichinho.alimenta(30)
print('Humor: %d' % bichinho.getHumor())
bichinho.brincar(20)
print('Humor: %d' % bichinho.getHumor())
bichinho.str()
