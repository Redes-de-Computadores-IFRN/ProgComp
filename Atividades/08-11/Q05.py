'''
Em um estacionamento, as tarifas são as seguintes (cumulativas):
• Até duas horas: R$ 8,00/hora ou fração;
• Entre três e quatro horas: R$ 5,00/hora ou fração;
• Horas seguintes: R$ 3,00/hora ou fração.
• Depois de 12h, o custo passa a ser fixo: R$ 30,00
Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba
o valor a ser pago pelo responsável.
Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da sexta hora): total de R$ 32,00
'''

min = float(input('Insira a quantidade de minutos estacionado: '))

if min <= 120 :
    duas_horas = min / 60
    duas_horas = 8.00 * duas_horas
    print(f'A tarifa é: R${duas_horas: .2f}')
elif min > 180 and min < 240 :
    uma_hora = 



