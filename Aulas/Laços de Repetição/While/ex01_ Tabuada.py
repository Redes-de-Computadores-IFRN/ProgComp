# Usando while

mult = int(input('Valor: '))

# Multiplicando
i = 1

print(f'Tabuada do {mult}')

while i <= 10 :
    print(f'{i} x {mult} = {i * mult}')
    i += 1

print('Fim da tabuada')