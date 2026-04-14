# Crie uma lista apenas com elementos numéricos
numericos = [1,2,3,4,5]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = [28, 'Julia', [1,2,3], False, 3.14, 9+9, 'Felipe']

# Imprima na tela apenas os 5 primeiros elementos da lista
print(mista[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(mista[0:-1:2])
# Remova da lista o último item
mista.pop()
# Insira na lista um novo item
mista.append('item novo')
print(mista)
# Remova da lista um item específico
mista.remove(3.14)
print(mista)