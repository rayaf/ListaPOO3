nomes = []
enderecos = []

i=0
while i < 5:
    nome = str(input('digite o nome: '))
    nomes.append(nome)
    endereco = str(input('digite o endereco: '))
    enderecos.append(endereco)
    i += 1
print(*nomes, sep = ", ")
print(*enderecos, sep = ", ")
