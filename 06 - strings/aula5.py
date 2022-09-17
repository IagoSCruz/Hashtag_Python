# Métodos de String
"""
nome = "Iago Silva da Cruz"

print(nome.capitalize())

print(nome.count('a')) # o que passamos dentro dos parênteses é conhecido como 'argumento'

email = 'iago@gmail.com'
print(email.endswith('gmail.com'))

print(email.find('@'))


#texto = """#Olá, bom dia
#Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
#Faturamento = R$2.500,00
"""

print(texto.splitlines())

"""

# Exercícios: CADASTRO DE CPF

#cpf = input('Insira o seu CPF: ')

#tratar o cpf
#tirar espaços no inicio e final. Tirar pontos. Tirar traços
"""
cpf = cpf.strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
   
else:
    print('Digite o seu cpf corretamente')
"""    



# EXERCÍCIO DE CADASTRO DE EMAILS

nome = input('Qual o seu primeiro nome? ')

email = input('Informe o seu melhor e-mail: ')


if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro foi concluído!')
    else:
        print('E-mail inválido')
else:
    print('Digite os dados para continuar')