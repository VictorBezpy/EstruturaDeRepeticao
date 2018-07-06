#19-0e1000.py
"""
19. Altere o programa anterior para que ele aceite apenas números entre 0 e 
1000.
"""
qnt = int(input("Digite a quantidade de números: "))
valor = int(input("Digite um número: "))
while valor < 0 or valor > 1000:
    valor = int(input("Valor não aceito, digite um número: "))
else:    
    maior = valor
    menor = valor
    soma = valor
    k = 0
    while k < qnt - 1:
        valor = int(input("Digite outro número: "))
        while valor < 0 or valor > 1000:
            valor = int(input("Valor não aceito, digite outro  número: "))
        else:
            soma = valor + soma
            k = k + 1
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor        
print("o menor valor é: ", menor)
print("o maior valor é: ", maior)
print("soma =", soma)