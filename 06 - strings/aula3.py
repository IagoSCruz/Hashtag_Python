# Trabalhar com índice negativo e pedaço de string

# Para pegar um texto de trás para frente: texto[-índice]


email = 'iago@gmail.com'
nome = 'Iago Cruz'

codigo = 'EB001234'

# print(texto[-3])

# Para pegar o pedaço de um texto use : (dois pontos). Texto[:índice] ou texto [índice:] ou ainda [índice:índice]

#print(len(texto))
#print(texto[5:10])

# Exercicio para fixação

print('Tamanho do e-mail ' + str(len(email))+ ' caracteres')
print('Primeiro caractere ' + email[0])
print('Último caractere ' + email[-1])
print('Servidor do e-mail: ' + email[5:10])