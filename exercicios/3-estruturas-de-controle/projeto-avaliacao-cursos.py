# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos = ["Python", "Excel", "Power BI", "Data Science", "Machine Learning"]
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_python = "Python"
curso_excel = "Excel"
curso_power_bi = "Power BI"
# 3. Crie um dicionário vazio para armazenar a nota do curso
notas_cursos = {}
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if curso_excel in cursos:
    print(f"{curso_excel} is in the list of courses")
else:
    print(f"{curso_excel} is not in the list of courses")

if curso_power_bi in cursos:
    print(f"{curso_power_bi} is in the list of courses")
else:
    print(f"{curso_power_bi} is not in the list of courses")

if curso_python in cursos:
    print(f"{curso_python} is in the list of courses")
else:
    print(f"{curso_python} is not in the list of courses")

# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
if curso_excel in cursos:
    nota_excel = input(f"Please provide a rating for the {curso_excel} course: ")
    notas_cursos[curso_excel] = nota_excel
if curso_power_bi in cursos:
    nota_power_bi = input(f"Please provide a rating for the {curso_power_bi} course: ")
    notas_cursos[curso_power_bi] = nota_power_bi
if curso_python in cursos:
    nota_python = input(f"Please provide a rating for the {curso_python} course: ")
    notas_cursos[curso_python] = nota_python

print(notas_cursos)