'''
   Exemplo 01: Laço de Repetição com FOR
'''

multiplicador = int(input('Digite o multiplicador: '))

print(f'Tabuada de {multiplicador}:')

for multiplicando in range(1, 11):
    print(f'{multiplicador} x {multiplicando} = {multiplicador * multiplicando}')

print('Fim da tabuada.')