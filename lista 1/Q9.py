def converte_segundos(segundos):
    horas = int(segundos/3600)
    minutos = int((segundos - (horas * 3600))/60)
    novos_segundos = int(segundos%60)
    return str(horas)+'h:'+str(minutos)+'m:'+str(novos_segundos)+'s'
    

segundos = int(input('Digite o tempo em segundos: '))
print(converte_segundos(segundos))


