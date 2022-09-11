# Exercícios

> Curso Hashtag

```
Sistema de cadastro de metas
```

## Blocos e Identação

### Estrutura
Sempre que usamos o if ou qualquer outra estrutura no Python, devemos usar a identação para dizer ao programa onde a estrutura começa e onde ela termina.

Isso vai ajudar muito quando tivermos mais de 1 condição ao mesmo tempo e quando tivermos várias ações para fazer dentro de um if.

### Várias ações em 1 if:

```
if condicao:
    alguma coisa
    outra coisa
    outra coisa a mais
    outra coisa mais ainda
else:
    uma coisa
    uma coisa a mais
    coisa final

## Exemplo

Regra de fundo de investimentos é:

- O fundo se compromete a entregar no mínimo 5% de retorno ao ano
- caso o fundo não consiga entregar os 5% de retorno, ele não pode cobrar taxa dos seus investidores
- caso o fundo consiga entregar mais de 5% de retorno, ele irá cobrar 2% de taxa dos seus investidores
- Caso o fundo consiga mais de 20% de retorno, ele irá cobrar 4% de taxa dos seus investidores

## Acréscimo do elif:

> E se temos mais do que um caso de sim e não?

```
if condicao:
    o que fazer se a condição 1 for verdadeira
elif condicao_2:
    o que fazer se a condição 1 for falsa e a condição 2 for verdadeira
else:
    o que fazer se a condição 1 e a condição 2 forem falsas

