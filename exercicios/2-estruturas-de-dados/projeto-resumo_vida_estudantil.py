# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
nome = input("Digite seu nome: ")
ano_conheceu_linkedin = input("Digite o ano que conheceu o LinkedIn: ")
ano_atual = input("Digite o ano atual: ")
cursos_realizados = input("Digite os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica: ")

# 2. Armazene esses dados em um dicionário
estudante = {'nome': nome,
             'ano_conheceu_linkedin': ano_conheceu_linkedin,
             'ano_atual': ano_atual,
             'cursos_realizados': list(cursos_realizados.split(','))}

print(estudante)

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = int(estudante['ano_atual']) - int(estudante['ano_conheceu_linkedin'])
total_cursos = len(estudante['cursos_realizados'])
primeiro_curso = estudante['cursos_realizados'][0]
ultimo_curso = estudante['cursos_realizados'][-1]

print(f"{estudante['nome']} conheceu o LinkedIn em {estudante['ano_conheceu_linkedin']} e, desde então, se dedicou por {total_anos} anos a realizar {total_cursos} cursos, sendo o primeiro curso '{primeiro_curso}' e o último curso '{ultimo_curso}'.")