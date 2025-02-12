#   IMC
'''
Faça um programa que solicite ao usuário sua altura e seu peso e que calcule e exiba seu indice de massa corporal (IMC)
'''

a = float(input('Insira sua altura em metro: '))
p = float(input('Insira seu peso: '))

imc = p / (a ** 2)

print('__________________________________________')
print(
    f'Altura: {a: .2f}m \nPeso: {p: .2f}kg \nIMC: {imc: .2f}kg/m²'
)
print('__________________________________________')