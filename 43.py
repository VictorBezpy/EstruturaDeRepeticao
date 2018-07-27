#43.py
"""
3. O cardápio de uma lanchonete é o seguinte:

        Especificação   Código  Preço
        Cachorro Quente 100     R$ 1,20
        Bauru Simples   101     R$ 1,30
        Bauru com ovo   102     R$ 1,50
        Hambúrguer      103     R$ 1,20
        Cheeseburguer   104     R$ 1,30
        Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades 
desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e 
o total geral do pedido. Considere que o cliente deve informar quando o pedido 
deve ser encerrado. 
"""

saida = []
multiplicador = []

while 0 not in saida:
	cod = int(input('Digite o código do produto(0 para sair): '))
	saida.append(cod)
	multi = int(input('Digite a quantidade(0 para sair): '))
	multiplicador.append(multi)
saida.remove(0)
multiplicador.remove(0)
print('\tEspecificação \tCódigo\tQuantidade\tPreço')

total = []
for s in range(0, len(saida)):
	if saida[s] == 100:
		t = 1.20 * multiplicador[s]
		total.append(t)
		print('\tCachorro Quente\t100\t%d\t     R$ %.2f' %(multiplicador[s], t))
	elif saida[s] == 101:
		t = 1.30 * multiplicador[s]
		total.append(t)
		print('\tBauru Simples\t101\t%d\t       R$ %.2f' %(multiplicador[s], t))
	elif saida[s] == 102:
		t = 1.50 * multiplicador[s]
		total.append(t)
		print('\tBauru com ovo\t102\t%d\t       R$ %.2f' %(multiplicador[s], t))
	elif saida[s] == 103:
		t = 1.20 * multiplicador[s]
		total.append(t)
		print('\tHambúrguer\t103\t%d\t          R$ %.2f' %(multiplicador[s], t))
	elif saida[s] == 104:
		t = 1.30 * multiplicador[s]
		total.append(t)
		print('\tCheeseburguer\t104\t%d\t       R$ %.2f' %(multiplicador[s], t))
	elif saida[s] == 105:
		t = 1 * multiplicador[s]
		total.append(t)
		print('\tRefrigerante\t105\t%d\t        R$ %.2f' %(multiplicador[s], t))
print('Total: R$', round(2, sum(total)))


