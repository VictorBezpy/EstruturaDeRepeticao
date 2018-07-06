#8-5notas.py
"""
08. Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

nota = [5, 7, 6, 8, 5]
s = 0
x = 0
while x < 5:
#soma = soma + nota [x] soma as 5 notas
	s += nota[x]
#x = x + 1 conta a quantidade de notas
	x += 1
print ('média : %.2f' %(s/x))