'''
meta = 0.05
taxa = 0
rendimento = float(input('Insira o rendimento do fundo: '))

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print('A taxa foi de {}'.format(taxa))
    else:    
        taxa = 0.02
        print('A taxa foi de {}'.format(taxa))
else:
    taxa = 0
    print('A taxa foi de {}'.format(taxa))
''' 
# Muita repetição de código
# Deixar o código mais limpo:


# ACRESCIMO DO ELIF

meta = 50000
vendas_funcionario1 = int(input('Informe o total de vendas: '))

if vendas_funcionario1 >= meta:
    bonus = (0.03 * vendas_funcionario1) / 100
    print('O funcionário obteve {} de bônus.'.format(bonus))

elif vendas_funcionario1 > meta * 2:
    bonus = (0.07 * vendas_funcionario1)
    print('O funcionário ultrapassou a meta, obtendo {} de bônus.'.format(bonus))

else:
    bonus = 0
    print('O funcionário não obteve bonificação.')
    

