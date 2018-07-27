#35.py
"""
35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera
uma lista dos números primos existentes entre 1 e um número inteiro informado
pelo usuário.
"""

primos = []
p = int(input('Quais os números primos de 1 até: ' ))

for c in range(1, p + 1):
	k = 0
	for d in range(1, c + 1):
		if c % d == 0:
			k += 1
	if k <= 2 and c != 1:
		primos.append(c)

print(primos)