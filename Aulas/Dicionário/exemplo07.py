'''
   EXEMPLO 07:

   Usando o dicionário dictAlunos faça um programa que solicite ao usuário a matrícula de um aluno:
   
    - Caso a matrícula não exista no dicionário, o programa deverá solicitar as duas notas da disciplina e adicione os valores digitados no dicionário;

    - Caso a matrícula já exista no dicionário, o programa deverá exibir a mensagem "Matrícula já  existe!" 
    mostrar as notas cadastradas e solicitar as novas notas.  

   O programa deve continuar solicitando a matrícula e as notas até que o usuário digite a matrícula 0.

   Ao final, o programa deve exibir o dicionário dictAlunos.
'''

dictAlunos = dict()
'''
dictAlunos = [
    ['2505', '15', '4'],
    ['2025', '10', '8'],
    ['2015', '20', '7']
]
'''

while True:
    matricula = input('Digite a matrícula: ')
    if matricula == '0': break
    for notas in dictAlunos:
        if matricula == notas[0]:
            print('Matrícula já existe!')
            print(f'Nota 1: {notas[1]}, Nota 2: {notas[2]}')
            break
    else:
        nota1 = input('Digite sua primeira nota: ')
        nota2 = input('Digite sua segunda nota: ')
        dictAlunos[matricula] = {'Nota 1': nota1, 'Nota 2': nota2}

print(dictAlunos)