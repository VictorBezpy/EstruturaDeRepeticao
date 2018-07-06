#1-nota0a10.py

"""
01. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem 
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
"""

while True:
	nota = float(input("Digite uma nota entre 0 e 10: "))
	if nota <= 10 and nota >= 0:
		break
	else:
		print ("nota inválida!")

print ("nota válida!")
