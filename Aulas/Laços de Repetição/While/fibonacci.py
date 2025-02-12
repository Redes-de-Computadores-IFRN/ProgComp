# Fazer um programa que solicite um valor inteiro positivo (n) e imprima os n primeiros elementos da sequência de fibonacci

num = int(input('Digite um número inteiro: '))

if num <= 0 :
    sys.exit ('informe n° positivo')

anterior, atual = 0, 1

contador = 1

while contador <= num :
    print(atual, end = ' ')
    anterior, atual = atual, atual + anterior
    contador += 1