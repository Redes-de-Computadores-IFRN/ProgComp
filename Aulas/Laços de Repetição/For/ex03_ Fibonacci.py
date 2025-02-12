
'''
   Exemplo 03: Faça um programa que solicite ao usuário um valor 
   inteiro positivo (n) e imprima os n primeiros números da sequência 
   de Fibonacci.

   exemplo: para n = 5
            1 1 2 3
'''
import sys

n = int(input('Digite um número inteiro positivo: '))

if n <= 0:
   sys.exit('O número deve ser positivo...')

anterior, atual = 0, 1

for contador in range(1, n + 1):
    print(atual, end=' ')
    anterior, atual = atual, atual + anterior
