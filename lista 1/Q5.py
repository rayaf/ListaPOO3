listaA = [15,14,18,16,24,35]
listaB = [9,2,3,4,5,6]

listaB.reverse()

listaC = [x + y for x, y in zip(listaA, listaB)]

print(listaC)
