#2-valns.py

"""
02. Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a 
pedir as informações.
"""

while True:
	nome = str(input("Digite o nome do usuário: "))
	senha = str(input("Digite a senha do usuário: "))
	if nome != senha:
		break
	else:
		print ("nome ou senha inválidos!")
print ("Válido!")