class ContaCorrente:

    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor


conta = ContaCorrente(12, 'joca')
conta.deposito(1000)
print(conta.saldo)
conta.saque(200)
print(conta.saldo)
conta.alterarNome('ze')
print(conta.nomeCorrentista)
