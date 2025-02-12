import datetime as dt

'''
Com base na nova legislação da Previdência Brasileira, regulamentada pela Lei Complementar nº 1354/2020 e pela Emenda à Constituição nº 49/2020,desenvolva um programa em Python que solicite as seguintes informações de uma pessoa:

• Sexo da pessoa (masculino/feminino).
• Data de nascimento da pessoa (no formato DD/MM/AAAA).
• Data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA).

O programa deve então calcular e exibir a data em que a pessoa poderá se aposentar, considerando as seguintes regras:

• Aposentadoria por Idade:
o Homens podem se aposentar aos 65 anos de idade.
o Mulheres podem se aposentar aos 62 anos de idade.
o É necessário ter pelo menos 15 anos de contribuição.

• Aposentadoria por Tempo de Contribuição:
o Homens podem se aposentar após 35 anos de contribuição.
o Mulheres podem se aposentar após 30 anos de contribuição.

Implemente o programa em Python para calcular a data de aposentadoria e exibi-la como resultado.
'''

#input's
sex =  bool(input('Informe seu sexo (masculino ou feminino): '))
dia_nasc = int(input('Informe o Dia do seu nascimento: '))
mes_nasc = int(input('Informe o Mês do seu nascimento: '))
ano_nasc = int(input('Informe o Ano do seu nascimento: '))
dia_contrib = int(input('Informe o Dia do inicio da contribuição: '))
mes_contrib = int(input('Informe o Mês do inicio da contribuição: '))
ano_contrib = int(input('Informe o Ano do inicio da contribuição: '))

masculino = True
feminino = True

#datas
data_recent = dt.date.today()
data_nasc = dt.date(ano_nasc,mes_nasc,dia_nasc)
data_contrib = dt.date(ano_contrib,mes_contrib,dia_contrib)

#aposentadoria por idade
ano_id = data_nasc.year
ano_hj = data_recent.year

aposent_id = ano_hj - ano_id

data_aposent_id = data_recent + (data_recent - data_nasc)
dt_apos_d = data_aposent_id.day
dt_apos_m = data_aposent_id.month
dt_apos_a = data_aposent_id.year

if sex := masculino and aposent_id >= 65 :
    print('\nPode aposentar')
else :
    print(f'\nIdade mínima para Homens aposentar é 65 anos \nVocê poderá se aposentar na data: {dt_apos_d}/{dt_apos_m}/{dt_apos_a}')
if sex := feminino and aposent_id >= 62 :
    print('\nPode aposentar')
else :
    print(f'\nIdade mínima para Mulheres aposentar é 62 anos \nVocê poderá se aposentar na data: {dt_apos_d}/{dt_apos_m}/{dt_apos_a}')

#Aposentadoria por Tempo de Contribuição

ano_cont = data_contrib.year
ano_hoje = data_recent.year

aposent_contrib = ano_hoje - ano_cont

data_aposent_cont = data_recent + (data_recent - data_contrib)
dt_apos_cont_d = data_aposent_cont.day
dt_apos_cont_m = data_aposent_cont.month
dt_apos_cont_a = data_aposent_cont.year

if sex := masculino and aposent_contrib >= 35 :
    print('\nPode aposentar')
else :
    print('\nContribuição mínima para Homens aposentar é 35 anos')
if sex := feminino and aposent_contrib >= 30 :
    print('\nPode aposentar')
else :
    print('\nContribuição mínima para Mulheres aposentar é 30 anos')


'''
TENTEI USAR O ELIF MAS POR ALGUM MOTIVO TAVA INDICANDO ERRO NO ':'
'''
