#   SALÁRIOS E COMISSÕES
'''
Faça um programa que solicite o salário base de um funcionário, o valor total das vendas dele e o percentual relativo a comissão e exiba o valor do salário a ser pago (salário base + comissão).
'''

salario = float(input('Insira seu salário base: '))
vendas = float(input('Insira o valor total das vendas: '))
comissao = float(input('Insira a porcentagem da comissão: '))

comissao = vendas * (comissao / 100)

salar_final = salario + comissao

print('__________________________________________')
print(
    f'Salário: R${salario: .2f} \nVendas: R${vendas: .2f} \nComissão: R${comissao: .2f} \nSalário a ser pago: R${salar_final: .2f}'
)
print('__________________________________________')