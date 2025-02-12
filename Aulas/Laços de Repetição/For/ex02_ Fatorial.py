'''
   Exemplo 02: Fazer um programa que solicite ao usuário um valor inteiro e 
   calcule o fatorial desse número. O fatorial de um número é calculado pela
   multiplicação desse número por todos os seus antecessores até o número 1.

   Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''
import sys

n = int(input('Digite um número inteiro: '))

if n < 0:
   sys.exit('O número deve ser positivo...')

if n == 0 or n == 1:
   sys.exit(f'{n}! = 1')

fatorial = 1

for contador in range(n, 1, -1):
   fatorial *= contador

print(f'{n}! = {fatorial}')