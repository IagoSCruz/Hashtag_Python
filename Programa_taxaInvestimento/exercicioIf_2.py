'''
2. Cálculo de bônus com uma nova regra
 • Agora , crie um novo código que calcule e dê um print no bônus dos funcionários novamente . Porém há uma nova regra nesse 2º caso :
A meta é 1000 vendas
Agora , os funcionários que venderem muito acima da meta ganham mais bônus do que os outros . Então o bônus é definido da seguinte forma :
 • Se vendas funcionário for maior ou igual a 2000 , então o bônus é de 15 % sobre o valor de vendas
 • Se vendas funcionário for menor do que 2000 e maior ou igual a 1000 , então o bônus é de 10 % sobre o valor de vendas
 • Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0 .
Use as mesmas variáveis de vendas funcionários

'''

vendas_funcionario1 = int(input('Informe o valor vendido pelo funcionário 1: '))
vendas_funcionario2 = int(input('Informe o valor vendido pelo funcionário 2: '))
vendas_funcionario3 = int(input('Informe o valor vendido pelo funcionário 3: '))

if vendas_funcionario1 >= 1000:
    if vendas_funcionario1 > 2000:
        bonus = vendas_funcionario1 * 0.15
    else:
        bonus = 0.1
else:
    bonus = 0

print('O funcionário 1 ganhou {} de bônus.'.format(bonus))

if vendas_funcionario2 >= 1000:
    if vendas_funcionario2 > 2000:
        bonus = vendas_funcionario2 * 0.15
    else:
        bonus = 0.1
else:
    bonus = 0

print('O funcionário 2 ganhou {} de bônus.'.format(bonus))

if vendas_funcionario3 >= 1000:
    if vendas_funcionario3 > 2000:
        bonus = vendas_funcionario3 * 0.15
    else:
        bonus = 0.1
else:
    bonus = 0

print('O funcionário 3 ganhou {} de bônus.'.format(bonus))