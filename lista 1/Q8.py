def valo_de_s(valor):
    soma = 0
    for i in range (1, valor+1):
        soma += 1/i

    print("O Somatorio de S é: ", soma)


valor = int(input('Informe um valor para S: '))
valo_de_s(valor)
