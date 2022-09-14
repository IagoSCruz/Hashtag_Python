faturamento = input('Qual foi o faturamento da loja nesse mês: ')
custo = input('QUal foi o custo da loja nesse mês: ')

if faturamento == '' or custo == '':
    print('Preencha os dados corretamente')
else:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de {} reais.'.format(lucro))