'''
   Fazer um programa que fique lendo números inteiros solicitados ao usuário.

   Quando o usuário digitar 0, o programa deve finalizar e imprimir a soma de 
   todos os números digitados bem como a média aritmética.

   O valor 0 não deve entrar na média.
'''

soma = 0
contador = 0

while True:
    num = int(input("Digite um número: "))
    if num == 0 : break
    soma += num
    contador += 1

media = soma / contador

print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')

'''
intSoma = 0
intQte = 0

while True:
    n = int(input('Digite n: '))
    if n == 0 : break
    intSoma += n 
    intQte += 1
print(f'Soma: {intSoma}')
print(f'Média: {intSoma/intQte}')
'''