#26.py
"""
26. Numa eleição existem três candidatos. Faça um programa que peça o número 
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número
de votos de cada candidato.
"""
q = int(input("Digite a quantidade de eleitores: "))
votos = []
s = 0
x = 0

while x <= q - 1:
	votos.append(input("\nVote a/b/c: "))
	x += 1

x = 0
k1 = 0
k2 = 0
k3 = 0
while x <= q - 1:
	if votos[x] in 'a':
		k1 += 1
	elif votos[x] in 'b':
		k2 += 1
	elif votos[x] in 'c':
		k3 += 1
	x += 1

print('\nCandidato a %d votos' %k1)
print('\nCandidato b %d votos' %k2)
print('\nCandidato c %d votos' %k3) 