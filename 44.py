#44.py
"""
44. Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

        1 , 2, 3, 4  - Votos para os respectivos candidatos 
        (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
        5 - Voto Nulo
        6 - Voto em Branco

        Faça um programa que calcule e mostre:
        O total de votos para cada candidato;
        O total de votos nulos;
        O total de votos em branco;
        A percentagem de votos nulos sobre o total de votos;
        A percentagem de votos em branco sobre o total de votos. Para 
        finalizar o conjunto de votos tem-se o valor zero. 
"""
votos = []

while 0 not in votos:
	print('1-José/ 2-João/3-Junior/4-Jairo/5-Voto Nulo/6-Voto em Branco')
	print('Para sair digite 0')
	v = int(input('Voto: '))
	votos.append(v)
print('Total de votos para José: ', votos.count(1))
print('Total de votos para João: ', votos.count(2))
print('Total de votos para Junior: ', votos.count(3))
print('Total de votos para Jairo: ', votos.count(4))
print('Total de votos Nulos: ', votos.count(5))
print('Total de votos em Branco: ', votos.count(6))

pn = votos.count(5) * 100 / len(votos)
print('Percentagem de votos Nulos: %.2f' %pn, '%')

pb = votos.count(6) * 100 / len(votos)
print('Percentagem de votos em Branco: %.2f' %pb, '%')