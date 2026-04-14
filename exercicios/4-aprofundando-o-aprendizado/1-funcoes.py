# Crie uma função para selecionar o curso desejado em uma trilha profissional
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
# Execute as funções

def selecionar_curso():
    curso = input("Digite o numero do curso desejado (1-Python, 2-Java): ")
    return curso

def percorrer_niveis(nivel):
    curso_escolhido = selecionar_curso()
    curso_dic = {"1": "Python", "2": "Java"}
    print(f"Você escolheu o curso de {curso_dic[curso_escolhido]}")
    for i in range(1, nivel+1):
        print(f"Você está no nível {i} do curso de {curso_dic[curso_escolhido]}.")
    else:
        print(f"Parabéns! Você concluiu o curso de {curso_dic[curso_escolhido]}.")

percorrer_niveis(10)