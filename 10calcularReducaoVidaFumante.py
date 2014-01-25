print ('Cálculo da redução de vida de um fumante \n')

qtdCigarros = int(input('Informe a quantidade de cigarros fumados por dia: '))
qtdAnosFum = int(input('Informe quantos anos você já fuma: '))

diasPerdidos = qtdCigarros * 0.166 + qtdAnosFum * 24 * 30 * 12

print('\nA quantidade de dias perdidos é de:',diasPerdidos)
