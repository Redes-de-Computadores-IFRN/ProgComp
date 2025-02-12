'''
   EXEMPLO 03:
   A partir do código do Exemplo 01, faça a seguinte alteração:

   a) Caso a lista possua nomes exiba cada nome em uma linha.
      A exibição deve ser em ordem alfabética.
'''




#  Exemplo do professor
'''
lstNomes = list()

while True:
   strNome = input('Digite um nome ou FIM para encerrar: ').upper()
   if strNome == 'FIM': break
   lstNomes.append(strNome)

lstNomes.sort()

# Usando FOR
for nome in lstNomes:
   print(nome)
'''

'''
lstNomes = list()

while True:
   strNome = input('Digite um nome ou FIM para encerrar: ').upper()
   if strNome == 'FIM': break
   lstNomes.append(strNome)

lstNomes.sort()

# Usando WHILE
indice = 0
while indice < len(lstNomes):
   print(lstNomes[indice])
   indice += 1
'''