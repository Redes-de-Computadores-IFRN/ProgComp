'''
 Fazer um programa que fique solicitando ao usuário para digitar um número inteiro e informe se o número é par ou ímpar. 
   
   O programa só deve encerrar quando o usuário digitar o número 0.
'''

num = int(input('Digite um número inteiro: '))

if num == 0 :
    sys.exit('Digite um valor maior que zero')

while num != 0 :
    if num % 2 == 0 :
        print(f'O número {num} é par.')
    else :
        print(f'O número {num} é impar.')
    num = int(input('Digite um número inteiro: '))


'''
while True:
    n = inte(input('Informe um valor: '))
    if n == 0 : break
    if n % 2 == 0 :
        print(f'{n} é um n° par!')
    else:
        print(f'{n} é um n° ímpar!')
print('Fim')

'''