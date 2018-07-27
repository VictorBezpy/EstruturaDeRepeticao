#30.py
"""
30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende 
implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99.
Você foi contratado para desenvolver o programa que monta a tabela de preços 
de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

        Preço do pão: R$ 0.18
        Panificadora Pão de Ontem - Tabela de preços
        1 - R$ 0.18
        2 - R$ 0.36
        ...
        50 - R$ 9.00
"""
price = float(input('Preço do pão: '))
qp = int(input('Quantidade de paes: '))
i = 1
print("Panificadora Pao de Ontem - Tabela de precos")
while i <= qp:
	if qp <= 50:
		print(i, "- R$ ", i * price)
		i += 1
	else:
		print("quantidade maxima de paes 50.")
		break