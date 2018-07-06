#13-potencia.py
"""
13. Faça um programa que peça dois números, base e expoente, calcule e mostre 
o primeiro número elevado ao segundo número. Não utilize a função de potência 
da linguagem.
"""
x = int(input('Digite a base: '))
y = int(input('Digite o expoente: '))
k = 1
n =1

while n <= y:
  k = x * k
  n += 1
  
print('resultado =',k)