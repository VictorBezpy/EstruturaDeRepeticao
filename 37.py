#37.py
"""
37. Uma academia deseja fazer um senso entre seus clientes para descobrir o 
mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve 
fazer um programa que pergunte a cada um dos clientes da academia seu código, 
sua altura e seu peso. O final da digitação de dados deve ser dada quando o 
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve 
ser informados os códigos e valores do clente mais alto, do mais baixo, do 
mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""
altura = []
peso = []
codigo = []

while 0 not in codigo:
	cod = int(input('Digite seu código (0 para sair): '))
	codigo.append(cod)
	if 0 not in codigo:
		p = float(input('Digite seu peso em kg: '))
		peso.append(p)
		alt = float(input('Digite sua altura em metros: '))
		altura.append(alt)
print('O cliente', codigo[altura.index(max(altura))], 
', é o mais alto com', max(altura), 'metors.')
print('O cliente', codigo[altura.index(min(altura))], 
', é o mais baixo com', min(altura), 'metors.')
print('O cliente', codigo[peso.index(max(peso))], 
', é o mais gordo com', max(peso), 'kg.')
print('O cliente', codigo[peso.index(min(peso))], 
', é o mais magro com', min(peso), 'kg.')
print('A média de peso dos clientes é', 
round((sum(peso) / len(peso)), 2), 'kg.')
print('A média de altura dos clientes é',
round((sum(altura) / len(altura)), 2), 'metros.')