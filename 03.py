#3-infos.py

"""
03. Faça um programa que leia e valide as seguintes informações:
        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd'; 
"""

sexol = ['m', 'f']
ecl = ['s', 'c', 'v', 'd']
while True:
	nome = str(input("Digite um nome com mais de 3 caracteres: "))
	idade = int(input("Digite a idade: "))
	salario = int(input("Digite o salario: "))
	sexo = str(input("Digite o sexo ('f' ou 'm'): "))
	ec = str(input("Digite o estado civil ('s', 'c', 'v', 'd'): "))
	if (len(nome) > 3) and (idade > 0) and (idade < 150) and (salario > 0) and (sexo in sexol) and (ec in ecl):
		break
	else:
		print ("\ninformações inválidas!\n")
print ("\ninformações válidas!\n")