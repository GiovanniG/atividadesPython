#Cálculo do maior e menor entre 3 números

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 > n2 and n3:
    print ('é o maior número')
if n2 > n1 and n3:
    print ('é o maior número')
if n3 > n1 and n2:
    print ('é o maior número')
