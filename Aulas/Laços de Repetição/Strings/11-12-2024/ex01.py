'''
   EXEMPLO 01:
   Fazer um programa em que o usuário informe uma frase e depois exiba qual
   a palavra mais longa da frase. 
'''

frase = input('Digite a frase: ')

QtdLetras = 0

while QtdLetras < len(frase):
    if frase[QtdLetras] == ' ' and frase[QtdLetras - 1] != ' ':
        QtdLetras += 1

print(QtdLetras)
