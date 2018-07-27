#49.py
"""
49. Faça um programa que mostre os n termos da Série a seguir:

          S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

        Imprima no final a soma da série. 
"""
x = int(input('Digite o limitador: '))
n = 1
m = 1
soma = 0
print('S =', end=' ')
while n <= x:
	print(n, '/' m, '+' , end=' ')
	soma = soma + (n / m)
	n += 1
	m += 2
print('=', soma)