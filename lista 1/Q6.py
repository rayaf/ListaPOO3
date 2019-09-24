def converte_horas(horas,minutos):
    if horas == 24:
        horaConvertida = 0
        horas = 0
    elif horas <=12:
        horaConvertida = horas
    else:
        horaConvertida = horas-12
        
    amOuPm = "AM" if horas <12 else "PM"
    return str(horaConvertida)+":"+str(minutos)+amOuPm
	    
while True :
	horas = int(input("Digite a hora a ser convertida: "))
	minutos = int(input("Digite o minuto: "))
	print(converte_horas(horas,minutos))
