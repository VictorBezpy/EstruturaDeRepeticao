#33.py
"""
33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um 
programa que leia as um conjunto indeterminado de temperaturas, e informe ao
final a menor e a maior temperaturas informadas, bem como a média das 
temperaturas.
"""
temps = []
i = 1
soma = 0

while 0 not in temps:
	print('0 para finalizar')
	t = float(input('Temperatura %d: ' %i))
	temps.append(t)
	i += 1
	soma += t
temps.remove(0)
print('Maior temperatura: %2.f' %max(temps))
print('Menor temperatura: %2.f' %min(temps))
print('Média das temperaturas: %2.f' %(soma / (i - 2)))
#Já começa com 1, mas a lista com 0 e depois conta a casa do obj 0, então -2.