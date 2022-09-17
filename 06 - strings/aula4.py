# OPERAÇÕES COM STRINGS
"""
str -> transforma número em string
in -> verifica se um texto está contido dentro de outro
operador + -> concatenar strings
.format e {} -> substitui valores
%s -> substitui textos
%d -> substitui números decimais

"""

faturamento = 1000
custo = 500
lucro = faturamento - custo

#print('O faturamento da loja foi de: ' + str(faturamento)) # o problema desse tipo é ter que tratar todas variáveis, é trabalhoso

#print('O faturamento foi de: {}. O custo foi de {}. O lucro foi de {}.'.format(faturamento, custo, lucro))
# Podemos repetir a variável dentro da string com o format, definindo o índex
print('O faturamento foi de: {0}. O custo foi de {1}. O lucro foi de {2}. Lembrando que o faturamento foi {0}.'.format(faturamento, custo, lucro))