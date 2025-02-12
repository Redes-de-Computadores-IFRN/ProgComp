
'''
O número de dias decorridos entre duas datas é importante em uma infinidade de
situações da vida cotidiana. Faça um programa que recebe inicialmente dois valores (dia inicial e mês
inicial), depois mais dois valores (dia final, mês final), ao final deve indicar quantos dias se passaram entre
as datas (considere que o ano não é bissexto).
Exemplos:
o 02 de 05 até 03 de 05 - 1 dia
o 27 de 04 até 03 de 05 - 6 dias
o 03 de 02 até 03 de 05 - 79 dias
Não esqueça de verificar se a data inicial é menor ou igual à data final.
Dica: conte o número de dias até cada uma das datas e subtraia esses números
'''

dia_i = int(input('Digite o dia inicial: '))
mes_i = int(input('Digite o mês inicial: '))
dia_f = int(input('Digite o dia final: '))
mes_f = int(input('Digite o mês final: '))

if mes_i == mes_f :
    diferenca = dia_f - dia_i
elif mes_f < mes_i :
    diferenca = (((mes_i + mes_f) * 30) - dia_i + dia_f) / 12
else : 
    diferenca = ((mes_f - mes_i) * 30) - dia_i + dia_f
print(diferenca)