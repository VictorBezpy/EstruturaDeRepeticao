#28.py
"""
28. Faça um programa que calcule o valor total investido por um colecionador 
em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá 
informar a quantidade de CDs e o valor para em cada um.
"""
qcd = int(input("quantidade de CD's: "))
cds = []
i = 1
while i <= qcd:
	n = float(input('preço do CD: '))
	cds.append(n)
	i += 1

soma = 0
i = 0
while i <= qcd - 1:#vagões [0 1 2 3 4] por isso - 1
	soma += cds[i]
	i += 1

print('média de preço por CD: %.2f' %(soma/qcd))