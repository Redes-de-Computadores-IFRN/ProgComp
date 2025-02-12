'''
   EXEMPLO 06:

   Usando o dicionário dictAlunos faça um programa que solicite ao usuário a matrícula de um aluno e as duas notas da disciplina e adicione os valores digitados no dicionário.

   O programa deve continuar solicitando a matrícula e as notas até que o usuário digite a matrícula 0.

   Ao final, o programa deve exibir o dicionário dictAlunos.
'''

dictAlunos = dict()

while True:
    matricula = input('Digite a matrícula: ')
    if matricula == '0':
        break
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    dictAlunos[matricula] = {'Nota 1': nota1, 'Nota 2': nota2}

print(dictAlunos)