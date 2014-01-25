#Cálculo do maior e menor entre 3 números
n1 = int(input('Informe o 1° numero: '))
n2 = int(input('Informe o 2° numero: '))
n3 = int(input('Informe o 3° numero: '))
if n1 > n2 and n3:
    print (n1,'é o maior numero')
elif n2 > n1 and n3:
    print (n2,'é o maior numero')
elif n3 > n1 and n2:
    print (n3,'é o maior numero')

#Se alguns numeros forem iguais    
elif n1 == n2 and n1 and n2 > n3:
    print (n1,'é o maior numero')
elif n1 == n3 and n1 and n3 > n2:
    print (n3,'é o maior numero')
elif n2 == n3 and n2 and n3 > n1:
    print (n2,'é o maior numero')

#todos os numeros iguais    
elif n1 == n2 and n3:
    print ('todos o numeros são iguais')

#Se alguns numeros forem iguais
if n1 < n2 and n3 and n1:
    print (n1,'é o menor numero')
elif n2 < n1 and n3:
    print (n2,'é o menor numero')
elif n3 < n1 and n2:
    print (n3,'é o menor numero')
elif n1 == n2 and n1 and n2 < n3:
    print (n1,'é o menor numero')
elif n1 == n3 and n1 and n3 < n2:
    print (n3,'é o menor numero')
elif n2 == n3 and n2 and n3 < n1:
    print (n2,'é o menor numero')
