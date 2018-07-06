#15-fibo.py
"""
15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
f = int(input("digite o numero: "))
a, b = 1, 1
n = 1
# f - 2, se o primeiro é 1 e o segundo é 1 tbm, 
#são menos duas vezes o loop, 
print(1)
print(1)
while n <= f - 2:
	a, b = b, a + b
	n = n + 1
	print(b)
