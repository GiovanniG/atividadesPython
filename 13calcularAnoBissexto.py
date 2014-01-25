# Cáculo de ano bissexto

ano = int(input('Informe o ano para saber se é bissexto: '))  
anOne = str(ano)          
valAno = ano % 400          
valAnoFull = str(valAno)     
if ano % 4 == 0:                       
    if '00' in anOne [2:]:                 
        if '0' in valAnoFull [2:]:            
           print ('O ano não é bissexto!')  
        else:  
           print ('O ano é bissexto!')  
    else:  
        print ('O ano é bissexto!')  
else:  
    print ('O ano não é bissexto!')
