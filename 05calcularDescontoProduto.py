print ('Calcular desconto de produto\n')

precoProduto = float(input('Informe o preço do produto: R$'))
porcentagem = float(input('Informe a porcentagem do desconto: %'))

desconto = porcentagem / 100 * precoProduto
valorFinal = precoProduto - desconto

print('\nO valor do desconto foi de: R$',desconto,'\nO valor a pagar é: R$', valorFinal)
