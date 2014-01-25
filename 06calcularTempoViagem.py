print ('Calcular tempo de viagem\n')

distancia = int(input('Informe a distância a ser percorrida: KM'))
velMedia = int(input('Informe a velocidade média a ser percorrida: KM/h'))

tempoHora = distancia / velMedia
tempoMin = tempoHora*60

print('\nO tempo de viagem serão de: Horas',tempoHora)
print('\nO tempo de viagem serão de: Minutos',tempoMin)
