#41.py
"""
41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com 
os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e 
valor da parcela.
        Os juros e a quantidade de parcelas seguem a tabela abaixo:

        Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
        1       0
        3       10
        6       15
        9       20
        12      25

        Exemplo de saída do programa:

        Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da 
        Parcela
        R$ 1.000,00     0               1                       R$  1.000,00
        R$ 1.100,00     100             3                       R$    366,00
        R$ 1.150,00     150             6                       R$    191,67
"""
valor = float(input('Valor da dívida: R$ '))
parcela = int(input('Em quantas parcelas vai pagar (1/3/6/9/12): '))

print('\tValor da dívida\tValor dos juros\tParcelas\tValor da parcela.')

if parcela == 1:
	juros = 0
	valordivida = valor + juros
	valorparcela = valordivida / parcela
	print('\tR$ %.2f\tR$ %.2f\t%d\tR$ %.2f' 
%(valordivida, juros, parcela, valorparcela))
elif parcela == 3:
	juros = valor * 10 / 100
	valordivida = valor + juros
	valorparcela = valordivida / parcela
	print('\tR$ %.2f\tR$ %.2f\t%d\tR$ %.2f' 
%(valordivida, juros, parcela, valorparcela))
elif parcela == 6:
	juros = valor * 15 / 100
	valordivida = valor + juros
	valorparcela = valordivida / parcela
	print('\tR$ %.2f\tR$ %.2f\t%d\tR$ %.2f' 
%(valordivida, juros, parcela, valorparcela))
elif parcela == 9:
	juros = valor * 20 / 100
	valordivida = valor + juros
	valorparcela = valordivida / parcela
	print('\tR$ %.2f\tR$ %.2f\t%d\tR$ %.2f' 
%(valordivida, juros, parcela, valorparcela))
elif parcela == 12:
	juros = valor * 25 / 100
	valordivida = valor + juros
	valorparcela = valordivida / parcela
	print('\tR$ %.2f\tR$ %.2f\t%d\tR$ %.2f' 
%(valordivida, juros, parcela, valorparcela))
else:
	print('Valor da parcela incorreto somete (1/3/6/9/12).')
