#46.py
"""
46. Em uma competição de salto em distância cada atleta tem direito a cinco 
saltos. No final da série de saltos de cada atleta, o melhor e o pior 
resultados são eliminados. O seu resultado fica sendo a média dos três valores 
restantes. Você deve fazer um programa que receba o nome e as cinco distâncias 
alcançadas pelo atleta em seus saltos e depois informe a média dos saltos 
conforme a descrição acima informada (retirar o melhor e o pior salto e depois 
calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos 
são informados na ordem da execução, portanto não são ordenados. O programa 
deve ser encerrado quando não for informado o nome do atleta. A saída do 
programa deve ser conforme o exemplo abaixo:

    Atleta: Rodrigo Curvêllo

    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m

    Resultado final:
    Rodrigo Curvêllo: 5.9 m
"""
saltos = []
i = 1

nome = str(input('Atleta: '))

while i <= 5:
	s = float(input('Salto %d: ' %i))
	saltos.append(s)
	i += 1

print('Melhor salto: %.1f' %max(saltos), 'm')
saltos.remove(max(saltos))
print('Pior salto: %.1f' %min(saltos), 'm')
saltos.remove(min(saltos))
media = sum(saltos) / 3
print('Média dos demais saltos: %.1f' %media, 'm')
print('Resultado final:')
print(nome, media)