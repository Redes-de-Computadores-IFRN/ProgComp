#Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a somados seus algarismos.

num = int(input('Digite um número de 4 digitos: '))

if num <= 0:
    print('Digite um número válido')
elif num > 9999:
    print('Apenas números abaixo de 9999')
else :

    mil = num // 1000
    num = num % 1000

    cent = num // 100
    num = num % 100

    dez = num // 10
    num = num % 10

    un = num // 1
    num = num % 1

    alg = mil + cent + dez + un

    print(f'A soma dos algarismos é: {alg}')