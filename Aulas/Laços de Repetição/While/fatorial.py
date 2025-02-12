# Faça um programa que solicite um valor inteiro e calcule o seu fatorial

num = int(input('Digite o valor para ser calculado: '))

fatorial = 1
contador = num

i = 1

if num < 0 :
    sys.exit('Informe n° >= 0')
if num == 0 or num == 1 :
    sys.exit (f'{num} = 1')

while contador > 1 :
    fatorial *= contador 
    contador -= 1

print(f'{num} fatorial é: {fatorial}')