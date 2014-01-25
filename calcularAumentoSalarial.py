print ('Calcular aumento de salário\n')

atualSal = float(input('Informe o salário: R$'))
porcentagem = float(input('Informe a porcentagem de aumento: %'))

resultado = porcentagem / 100 * atualSal
novoSal = atualSal + resultado
print('\nO valor do aumento foi de: R$',resultado,'\nO salário com o aumento é: R$',novoSal)
