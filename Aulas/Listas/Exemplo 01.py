'''
   EXEMPLO:
   Fazer um programa que nomes de pessoas ao usuário. O programa deverá parar de
   solicitar quando o usuário digitar FIM.
   
   Em seguida o programa deverá solicitar um nome de uma pessoa qualquer e 
   informar se esse nome consta nos nomes digitados anterioremente ou não.
'''

nomes = [ ]

while True:
    n = input('Digite os nomes: ').upper()

    if n == 'FIM': break

    nomes.append(n)

solicite = input('Digite um nome para consulta: ').upper()

if solicite in nomes:
    print('Consta na lista')
else:
    print('Não consta.')