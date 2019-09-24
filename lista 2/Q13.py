class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

funcionario = Funcionario('Zé', 1000)
print('Nome: %s' % funcionario.getNome())
print('Salario: %.2f' % funcionario.getSalario())
