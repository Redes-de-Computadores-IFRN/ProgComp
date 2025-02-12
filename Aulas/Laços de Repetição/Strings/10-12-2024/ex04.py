'''
   EXEMPLO 04:
   Fazer um programa em que o usuário informe uma palavra e em seguida
   o programa exiba a palavra invertida e diga se ela é um palíndromo ou não.
'''

palavra = input('Digite a palavra: ')

palav_invert = ' '

for i in range(len(palavra) -1, -1, -1):
    palav_invert += palavra[i]
if palavra.lower() == palav_invert.lower():
    print('É palindromo')