#5-pop2.py
"""
05. Altere o programa anterior permitindo ao usuário informar as populações e
as taxas de crescimento iniciais. Valide a entrada e permita repetir a 
operação.
"""

popA = float(input('Digite a população do país A: '))
popB = float(input('Digite a população do país B: '))
creA = float(input('Digite a taxa de crescimento país A: '))
creB = float(input('Digite a taxa de crescimento país B: '))
anos = 0

while popA < popB:
	popA += float((popA * creA) / 100)
	popB += float((popB * creB) / 100)
	anos += 1
print('serão necessários %d anos para que a população do país A ultrapasse ou'
 'iguale a população do país B' %anos)