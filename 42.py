#42.py
"""
2. Faça um programa que leia uma quantidade indeterminada de números positivos 
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] 
e [76-100]. A entrada de dados deverá terminar quando for lido um número 
negativo.
"""
numeros1 = []#[0-25]
numeros2 = []#[26-50]
numeros3 = []#[51-75]
numeros4 = []#[76-100]
n = 0

while n >= 0:
	print('Para sair digite um número negativo.')
	n = int(input('Digite um número de 0 a 100: '))
	if n >= 0 and n <= 25:
		numeros1.append(n)
	elif n >= 26 and n <= 50:
		numeros2.append(n)
	elif n >= 51 and n <= 75:
		numeros3.append(n)
	elif n >= 76 and n <= 100:
		numeros4.append(n)
print('Entre 0 e 25 temos %d números' %(len(numeros1)))
print('Entre 26 e 50 temos %d números' %(len(numeros2)))
print('Entre 51 e 75 temos %d números' %(len(numeros3)))
print('Entre 76 e 100 temos %d números' %(len(numeros4)))
