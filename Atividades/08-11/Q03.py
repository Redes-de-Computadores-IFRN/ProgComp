'''
 Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo. Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada (hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto (em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km)
 Após receber os dados, o programa informa dados típicos de um computador de bordo:
 a) o tempo de viagem (em segundos)
 b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h)
 c) o custo da viagem com combustível (em R$)
 d) o desempenho do carro (em Km/l, l/h e R$/Km).
'''

#input's

h_incial = int(input('Informe a hora inicial da partida: '))
min_inicial = int(input('informe os minutos iniciais da partida: '))

h_final = int(input('Informe a hora final da partida: '))
min_final = int(input('informe os minutos finais da partida: '))

descanso = int(input('Informe o tempo de descanso em segundos: '))

l_gasto = float(input('Informe quantos litros foram gastos: '))

l_preco = float(input('Informe o preço do litro: R$ '))

distancia = float(input('Informe a distância percorrida em Km: '))



#convertendo tudo pra segundos


seg_inicial = ((h_incial * 60) + min_inicial) * 60
seg_final = ((h_final * 60) + min_final) * 60

# Dados do computador de bordo 

if seg_inicial >= seg_final :
   a = (seg_final - seg_inicial) + descanso
else :
   a = (seg_final + seg_inicial) - (24 * 60 * 60) + descanso

b_global = distancia / ((a / 60) / 60)
b_movimento = distancia / ((a - descanso) / 60 ) / 60
c = l_preco * l_gasto
d_kml = distancia / l_gasto
d_lh = l_gasto / (((seg_final - seg_inicial) / 60 ) / 60)
d_rkm = l_preco / distancia 

print(
   f'\nOs dados da viagem são: \ntempo da viagem: {a}s \nVelocidade média geral: {b_global} Km/h \nVelocidade média em movimento: {b_movimento} Km/h \nO custo da viagem com combustível: R$ 
      {c: .2f} \nDesempenho do carro: {d_kml: .2f} Km/l, {d_lh: .2f} L/h e {d_rkm: .2f} R$/Km \n'
)