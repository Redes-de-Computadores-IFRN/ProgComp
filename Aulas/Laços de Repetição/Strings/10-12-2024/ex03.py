'''
   EXEMPLO 03:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas palavras existem na string digitada
'''

# Solicita ao usuário que informe uma string
frase = input('Informe uma string: ')

# Percorre cada caractere da frase digitada
intPosicao    = 0
intQtPalavras = 0
while intPosicao < len(frase):
   # Verifica se o caractere atual é um espaço em branco
   if frase[intPosicao] == ' ' and frase[intPosicao - 1] != ' ':  
      intQtPalavras += 1
   intPosicao += 1 

# verifica se a última palavra da frase não foi contabilizada
if frase[-1] != ' ': intQtPalavras += 1

# Exibe a quantidade de palavras na frase digitada
print(f'Quantidade de palavras na frase: {intQtPalavras}')