# Cálculo de Bônus

#Variaveis
meta = 1000
bonus = 0.10
vendas_funcionario1 = int(input('Informe o valor vendido pelo funcionário 1: '))
vendas_funcionario2 = int(input('Informe o valor vendido pelo funcionário 2: '))
vendas_funcionario3 = int(input('Informe o valor vendido pelo funcionário 3: '))

#condições
if vendas_funcionario1 >= meta:
    bonus = vendas_funcionario1 * 0.1
    print('O funcionário 1 ganhou {} de bônus'.format(bonus))
else:
    print('O funcionário não ganhou bônus')

if vendas_funcionario2 >= meta:
    bonus = vendas_funcionario2 * 0.1
    print('O funcionário 2 ganhou {} de bônus.'.format(bonus))
else:
    print('O funcionário não obteve bônus')

if vendas_funcionario3 >= meta:
    bonus = vendas_funcionario3 * 0.1
    print('O funcionário 3 ganhou {} de bônus.'.format(bonus))
else:
    print('O funcionário não obteve bônus')