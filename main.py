print('*********************')
print('Metas de Funcionários')
print('*********************')

#variaveis

meta = 50000
venda_func = int(input('Insira o valor de vendas: '))
meta_loja = 90000
vendas_loja = int(input('Insira o valor vendido pela loja: '))



if venda_func >= meta and vendas_loja >= meta_loja:
    bonus = venda_func * 0.1
    print('O vendedor ganhou {} de bônus!'.format(bonus))
else:
    print('O vendedor não alcançou a meta.')
    