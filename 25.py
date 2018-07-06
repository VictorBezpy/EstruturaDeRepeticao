#25.py
"""
25. Faça um programa que peça para n pessoas a sua idade, ao final o programa 
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e 
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a 
média calculada.
"""
q = int(input("Digite a quantidade de pessoas: "))
idade = []
s = 0
x = 0
while x <= q - 1:
	n = float(input("idade: "))
	idade.append(n)
	s += n
	x += 1
m = s / x
print ('média de idade da turma: %.2f' %m)
if m > 0 and m < 25:
	print('a turma é jovem')
elif m > 26 and m < 60:
	print('a turma é adulta')
else:
	print('a turma é idosa')