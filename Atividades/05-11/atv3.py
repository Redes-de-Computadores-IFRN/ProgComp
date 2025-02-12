#   DESCONTO
'''
Faça um programa que solicite o preço de um produto e um valor percentual de desconto e que calcule e exiba o preço do produto com desconto.
'''

preco = float(input('Insira o preço do produto: '))
percent = float(input('Insira a porcentagem do desconto: '))

descont = preco * (percent / 100)

descont = preco - descont

print('__________________________________________')
print(
    f'Preço: R$ {preco: .2f} \nDesconto: {percent: .2f}% \nPreço com desconto: R$ {descont: .2f}'
)
print('__________________________________________')