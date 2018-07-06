#11-intsoma.py
"""
11. Altere o programa anterior para mostrar no final a soma dos números.
"""
x = int(input('Digite o primeiro número (menor): '))
y = int(input('Digite o segundo número (maior): '))
#para imprimir apenas o intervalo
x += 1
soma = 0
while x < y:
	print(x)
	soma += x
	x += 1
print('Soma: %d' %soma)