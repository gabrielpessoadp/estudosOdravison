
atleta = []
atletasLista = []
paradaCond = 'a'
distancias = []
distLista = []
while paradaCond != '':
    paradaCond = input('Para encerrar aperte Enter, para continuar digite algo:')
    if paradaCond == '':
        print('PROGRAMA ENCERRADO')
        break
    atleta.append(input('Digite o nome do atleta:'))
    for i in range(5):
        distancias.append(input('Digite os saltos:'))
    atleta.append(distancias)
    print(atleta)
distLista.append(distancias)
atletasLista.append(atleta)
print(atletasLista)
print(atleta)
        