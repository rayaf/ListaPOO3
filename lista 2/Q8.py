class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def comer(self, comida):
        self.estomago.append(comida)

    def verEstomago(self):
        print('Estomago:', self.estomago)

    def digerir(self):
        if (len(self.estomago) > 0):
            self.estomago.pop(0)

# Teste
macaco1 = Macaco('chico')
macaco2 = Macaco('twelves')

macaco1.comer('Maca')
macaco1.verEstomago()
macaco1.comer('Banana')
macaco1.verEstomago()
macaco1.comer('Abacaxi')
macaco1.verEstomago()
macaco1.digerir()
macaco1.verEstomago()
macaco2.comer('Maca')
macaco2.comer('Banaca')
macaco2.comer(macaco1)
macaco2.verEstomago()
