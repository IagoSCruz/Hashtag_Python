# Métodos de String

nome = "Iago Silva da Cruz"

print(nome.capitalize())

print(nome.count('a')) # o que passamos dentro dos parênteses é conhecido como 'argumento'

email = 'iago@gmail.com'
print(email.endswith('gmail.com'))

print(email.find('@'))


texto = """ Olá, bom dia
Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
Faturamento = R$2.500,00
"""

print(texto.splitlines())