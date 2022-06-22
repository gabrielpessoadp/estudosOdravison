





#['jan','fev','mar','abril','maio','junho','julho','agosto','set','out','nov','dez']
meses = ['jan','fev','mar','abril','maio','junho','julho','agosto','set','out','nov','dez']
mediaTemp = []

for mes in meses:
    mediaTemp.append(float(input(f'Digite a temp media do mes de {mes}: ')))
mediaAnual = sum(mediaTemp) / len(meses)
print('A temperatura media anual é: ',mediaAnual)

for i in range(len(meses)):
    if mediaTemp[i] > mediaAnual:
        print('A temperatura de', mediaTemp[i],'do mês de', meses[i], 'foi maior que a média anual')
