def imprime_valores(valor):
    for i in range(1, valor + 1):
        print(('%s '%i)*i)

valor = int(input('Informe um numero: '))

imprime_valores(valor)
