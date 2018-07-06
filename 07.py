#7-mn.py
"""
07. Faça um programa que leia 5 números e informe o maior número.
"""

n1=float(input("primeiro número: "))
n2=float(input("segundo número: "))
n3=float(input("terceiro número: "))
n4=float(input("quarto número: "))
n5=float(input("quinto número: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
	print("o maior número é o primeiro", n1)

elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
	print("o maior número é o segundo", n2)

elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
	print("o maior número é o terceiro", n3)	

elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
	print("o maior número é o quarto", n4)	

else:
	print("o maior número é o quinto", n5)