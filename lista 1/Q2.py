digito = input('Entra com a letra: ').capitalize()

if not digito.isdigit():
    if digito in ['A', 'E', 'I', 'O', 'U'] :
        print('Vogal')
    else:
        print('Consoante')
else:
    print('não é valido')
