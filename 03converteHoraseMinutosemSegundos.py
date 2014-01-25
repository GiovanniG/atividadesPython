print ('Conversor de horas e minutos para segundos\n')

valDia = int(input('Informe dia(s): '))
valHora = int(input('Informe uma hora: '))
valMin = int(input('Informe os minutos: '))
valSeg = int(input('Informe os segundos: '))

resultado = valDia*24*3600 + valHora*3600 + valMin*60 + valSeg

print ('\nO valores informados em segundos são:',resultado)
