numeros = []
numerosPares = []
pares = 0
numerosImpares = []

i=0
while i < 15:
    numeros.append(int(input('Entre com um numero: ')))
    if numeros[i]%2 == 0:
        numerosPares.append(numeros[i])
        pares += 1
    else:
         numerosImpares.append(numeros[i])
    i += 1

print('sao {} numeros pares sendo eles {}'.format(pares, numerosPares))
print(sum(numerosImpares))
        
