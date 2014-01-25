#Tipos de triângulos
ladoa = int(input('Informe o lado A: '))
ladob = int(input('Informe o lado B: '))
ladoc = int(input('Informe o lado C: '))


if ladob - ladoc < ladoa < ladob + ladoc and ladoa - ladoc < ladob < ladoa + ladoc and ladoa - ladob < ladoc < ladoa + ladob:
    print('Essas medidas formam um triângulo')
    if ladoa != ladob and ladoa != ladoc:
        print('As medidas formam um triângulo escaleno')
    elif ladoa == ladob and ladoa != ladoc:
        print('As medidas formam um triângulo isósceles')
    elif ladob == ladoc and ladob != ladoa:
        print('As medidas formam um triângulo isósceles')
    elif ladoa == ladoc and ladoa != ladob:
        print('As medidas formam um triângulo isósceles')
    elif ladoa == ladoc and ladoa == ladob:
        print('As medidas formam um triângulo equilátero')
else:
    print('Essas medidas NÃƒO formam um triângulo')
