# Comentario de linha
# aula 03 exemplo 01
# Cacio

x = int(input("Digite o primeiro valor: "))
sinal = input("Digite um sinal? ")
y = int(input("Digite o segundo valor: "))
p = 0
while sinal != 'false' :
    if sinal == '+':
        p = x + y;
        sinal = 'false'
        print('A soma dos dois numeros É:',p)
    elif (sinal == '-'):
        p = x - y;
        print('A soma dos dois numeros É:',p)
        sinal = 'false'
    elif(sinal == '/'):
        p = x / y;
        print('A soma dos dois numeros É:',p)
        sinal = 'false'
    elif (sinal == '*'):
        p = x * y;
        print('A soma dos dois numeros É:',p)
        sinal = 'false'
    else:
        print('gite um operador valido')
        sinal = 'false'
        
        sinal = input("Digite um sinal? ")
                
