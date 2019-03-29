
primeiradigitacao = True
while True:

     n = input("didgite um numero: ")

     if n.lower() == 'fim':
         break
     else:
        try:
             n= int(n)
             if primeiradigitacao:
                 meior = n
                 menor = n
                 primeiradigitacao =  False
             else:
                 if n > meior:
                     meior = n
                 if n < menor:
                     menor = n
        except:
                print('aaaa')
                  
if primeiradigitacao:
    print('Nem um valor digitado')
else:
    
    print("O maior número digitado é ", meior,"o menor numero digitado", menor)
                

         
