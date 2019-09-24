class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def setAltura(self, altura):
        self.altura = altura

    def getAltura(self):
        return self.altura

    def calculaArea(self):
        return self.base * self.altura

    def calculaPerimetro(self):
        return 2 * self.base + 2 * self.altura

base = int(input('Informe o valor da base: '))
altura = int(input('Informe o valor da altura: '))
retangulo = Retangulo(base, altura)
print('A area do retangulo eh: %d' % retangulo.calculaArea())
print('O perimetro do retangulo eh: %d' % retangulo.calculaPerimetro())
