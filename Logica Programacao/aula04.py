
maior    = 0;
contador = 0;
while contador  < 5:

    n = int(input(str(contador+1))+" Numero: "))
    if(n > 0):
        contador = contador + 1
        if(n > maior):
            maior = n
    else:
        print("erro")
        

     
 
print("maior:", maior)
    
#n1 = int(input("Numero: "))
#n2 = int(input("Numero: "))
#n3 = int(input("Numero: "))
#n4 = int(input("Numero: "))
#n5 = int(input("Numero: "))

#if(n1 > 0 and n2 > 0 and n3 > 0 n4 >0 and n5>0):
 #   print("nem desse 5 foram escritos")
