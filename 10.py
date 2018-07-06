#10-intervalo.py
"""
10. Faça um programa que receba dois números inteiros e gere os números 
inteiros que estão no intervalo compreendido por eles.
"""
x = int(input('Digite o primeiro número (menor): '))
y = int(input('Digite o segundo número (maior): '))
#para imprimir apenas o intervalo
x += 1

while x < y:
	print(x)
	x += 1