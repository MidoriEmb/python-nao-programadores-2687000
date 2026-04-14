# Declare 4 variáveis do tipo numérica
a =1
b=2
c=3
d=4

# Crie uma estrutura condicional para comparar dois números
if (a > b):
    print("True")
else:
    print("False")
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if(d>4):
    print(f"True {d} is greater than 4")

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
else:
    print(f"False {d} is not greater than 4")

# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if(a>b) or (c>d):
    print("True")
elif(a>b) and (c>d):
    print("True")
else:    
    print("False")

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if(b>a):
    print("True1")
if(c>a):
    print("True2")
else:    print("False")