
palavra = "";
contador = -1;

while True:

     n = input("didgite um numero: ")

     if n == 'fim':
         break
     else:
         n = int(n)
         if int(n) > 0:   
             
             if n > contador:
                contador = n

print("O maior número digitado é ", contador)

                

         
