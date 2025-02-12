#Faça um programa que solicite ao usuário um valor decimal positivo (esse valor corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.

saque = float(input('Digite o valor do saque em real: R$ '))

if saque <= 0 :
    print('Digite um saque válido')
else :
    cent = saque // 100
    saque = saque % 100

    cinq = saque // 50
    saque = saque % 50

    vint = saque // 20
    saque = saque % 20

    dez = saque // 10
    saque = saque % 10

    cinc = saque // 5
    saque = saque % 5

    dois = saque // 2
    saque = saque % 2

    um = saque // 1
    saque = saque % 1

    cinq_cent = saque // 0.50
    saque = saque % 0.50

    vint_cinc_cent = saque // 0.25
    saque = saque % 0.25

    dez_cent = saque // 0.10
    saque = saque % 0.10

    cinc_cent = saque // 0.05
    saque = saque % 0.05

    um_cent = saque // 0.01
    saque = saque % 0.01

    print(
        f'\nQUANTIDADES DE CÉDULAS: \n{cent: .0f} de R$ 100,00 \n{cinq: .0f} de R$ 50,00 \n{vint: .0f} de R$ 20,00 \n{dez: .0f} de R$ 10,00 \n{cinc: .0f} de R$ 5,00 \n{dois: .0f} de R$ 2,00 \n \nQUANTIDADES DE MOEDAS: \n{um: .0f} de R$ 1,00 \n{cinq_cent: .0f} de R$ 0,50 \n{vint_cinc_cent: .0f} de R$ 0,25 \n{dez_cent: .0f} de 0,10 \n{cinc_cent: .0f} de 0.05 \n{um: .0f} de R$ 0,01  '
    )