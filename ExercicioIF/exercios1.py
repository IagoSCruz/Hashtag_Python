# Criando um mini sistema de controle de estoque

print('Sistema de Controle de Estoque')
print('CATEGORIAS PERMITIDAS: alimentos | bebidas | limpeza')

nome_produto = input('Informe o nome do produto: ') 
categoria = input('informe a categoria do produto: ')
estoque = int(input('Digite a quantidade atual: '))


    
if nome_produto and categoria and estoque:
    if categoria == 'bebidas':
        if estoque < 75:
            print(f'Solicitar {nome_produto} a equipe de compras. Há apenas {estoque} em estoque')
        else:
            print(f'Estoque de {nome_produto} registrado')
    elif categoria == 'alimentos':
        if estoque < 50:
            print(f'Solicitar {nome_produto} a equipe de compras. Há apenas {estoque} em estoque')
        else:
            print(f'Estoque de {nome_produto} registrado')
    elif categoria == 'limpeza':
        if estoque < 30:
            print(f'Solicitar {nome_produto} a equipe de compras. Há apenas {estoque} em estoque')
        else:
            print(f'Estoque de {nome_produto} registrado')  
    
else:
    print('ERRO! Preencha os produtos corretamente')