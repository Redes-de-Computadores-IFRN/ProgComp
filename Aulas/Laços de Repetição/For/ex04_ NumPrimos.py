
'''
   Exemplo 04: Faça um programa que solicite ao usuário um valor 
   inteiro positivo (n) e imprima os n primeiros números inteiros primos.
'''
import sys

n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
   sys.exit('O número deve ser positivo...')

cont_primos = 0
numero      = 2

while cont_primos < n:
   cont_divisores = 0
   for i in range(1, numero + 1):
      if numero % i == 0: cont_divisores += 1

   if cont_divisores == 2:
      print(numero, end ='; ')
      cont_primos += 1

   numero += 1
