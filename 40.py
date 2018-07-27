#40.py
"""
40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados 
sobre acidentes de trânsito. Foram obtidos os seguintes dados:
        Código da cidade;
        Número de veículos de passeio (em 1999);
        Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
        Qual o maior e menor índice de acidentes de transito e a que cidade 
        pertence;
        Qual a média de veículos nas cinco cidades juntas;
        Qual a média de acidentes de trânsito nas cidades com menos de 2.000 
        veículos de passeio. 
"""
codigos = []
nveic = []
naci = []
k = 0
x = 0
menosaci = []

while k <= 4:
	cod= int(input('Digite código da cidade: '))
	codigos.append(cod)
	veic = int(input('Digite número de veículos de passeio: '))
	nveic.append(veic)
	aci = int(input('Digite número de acidentes de trânsito com vítimas: '))
	naci.append(aci)
	k += 1
	if nveic[x] < 2000:
		menosaci.append(aci)
	x += 1

print('A cidade com mais acidentes foi a', codigos[naci.index(max(naci))], 
', com', max(naci), 'acidentes.')
print('A cidade com menos acidentes foi a', codigos[naci.index(min(naci))], 
', com', min(naci), 'acidentes.')
print('A média de veículos nas cinco cidades juntas é', 
round((sum(nveic) / len(nveic)), 2))
print('A média de acidentes de trânsito nas cidades com menos de 2.000', 
'veículos de passeio é', 
round((sum(menosaci) / len(menosaci)), 2))

