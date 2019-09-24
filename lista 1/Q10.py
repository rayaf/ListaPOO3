print('reponda 1 para sim e 0 para não')
count = 0
resp = int(input('Telefonou para a vítima?: '))
if resp == 1:
  count += 1

resp = int(input('Esteve no local do crime?: '))
if resp == 1:
  count += 1

resp = int(input('Mora perto da vítima?: '))
if resp == 1:
  count += 1

resp = int(input('Devia para a vítima?: '))
if resp == 1:
  count += 1

resp = int(input('Já trabalhou com a vítima?: '))
if resp == 1:
  count += 1

if count == 2:
  print('Suspeita(0)')
if count == 3 or count == 4:
  print('Cúmplice')
if count == 5:
  print('Assassino')
else:
  print('Inocente')
