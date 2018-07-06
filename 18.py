#18-Mms.py
"""
18. Faça um programa que, dado um conjunto de N números, determine o menor 
valor, o maior valor e a soma dos valores.
"""
qnt = int(input("Digite a quantidade de números do conjunto: "))
valor = int(input("Digite um número: "))
maior = valor
menor = valor
soma = valor
k = 0
while k < qnt - 1:
    valor = int(input("Digite outro número: "))
    soma = valor + soma
    k += 1
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor        
print("o menor valor é: ",menor)
print("o maior valor é: ",maior)
print("soma =",soma)