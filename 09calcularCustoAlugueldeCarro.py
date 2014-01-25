print ('Cálculo de custo carro de aluguel \n')

qtdKm = int(input('Informe a quantidade de km percorridos carro alugado: Km'))
qtdDias = int(input('Informe a quantidade de dias com carro alugado:'))

resultado = qtdDias * 60 + qtdKm * 0.15

print('\nO valor a pagar é: R$',resultado)

