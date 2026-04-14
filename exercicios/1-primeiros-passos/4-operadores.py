ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
print(f"Girlaine tinha {ano_formatura - ano_nascimento} anos quando se formou.")

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento > ano_formatura)
print(ano_nascimento <= ano_formatura)
print(ano_nascimento == ano_formatura)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((ano_nascimento < ano_formatura) and (ano_formatura < 2020))
print((ano_nascimento > 2000) or (ano_formatura < 2020))
print(not(ano_nascimento == ano_formatura))