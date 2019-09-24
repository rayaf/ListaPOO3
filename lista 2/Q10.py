class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)
    def alterarValor(self, valorLitro):
        self.setValorLitro(valorLitro)

    def alterarCombustivel(self, tipoCombustivel):
        self.setTipoCombustivel(tipoCombustivel)

    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.setQuantidadeCombustivel(quantidadeCombustivel)


bomba1 = BombaCombustivel('Gasolina Aditivada', 3.03, 10000)
bomba1.abastecerPorLitro(100)
print(bomba1.quantidadeCombustivel)
bomba1.abastecerPorValor(100)
print(bomba1.quantidadeCombustivel)
bomba1.alterarValor(3.89)
print(bomba1.valorLitro)
bomba1.alterarCombustivel('Gasolina Comum')
print(bomba1.tipoCombustivel)
bomba1.alterarQuantidadeCombustivel(5000)
print(bomba1.quantidadeCombustivel)

