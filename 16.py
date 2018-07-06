#16-fib500.py
"""
16. A série de Fibonacci é formada pela seqüência 
0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o 
valor seja maior que 500.
"""

a, b = 1, 1
 
print(a)
print(b)
while b < 500:
	a, b = b, a + b
	print(b)