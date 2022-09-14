meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 200000

if vendas_funcionario >= meta_funcionario and vendas_loja >= meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('O funcionário teve um bônus de {}.'.format(bonus))
else:
    print('O funcionário não ganhou bônus')

print('A loja vendeu {} de reais no mês. A meta era de {} reais.'.format(vendas_loja, meta_loja))


