#produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
#vendas = [1000, 1500, 350, 270, 900]

# print(vendas[1])
#vendas [3] = 300
#print ('Vendas do produto {} foram de {} unidades.'.format(produtos[3], vendas[3]))

# listas são mutáveis, isso significa que podemos alterar o valor delas.

"""
COMO DESCOBRIR O ÍNDICE DE UM ITEM DE UMA LISTA?
"""

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 120, 70, 90, 80, 15]

# utilizaremos o método index

i = produtos.index('geladeira')
qnt_estoque = estoque[5]

print(qnt_estoque)
print(i)

print(produtos[i])

