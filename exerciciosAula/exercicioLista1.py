#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#a- "Telefonou para a vítima?"
#b- "Esteve no local do crime?"
#c- "Mora perto da vítima?"
#d- "Devia para a vítima?"
#e- "Já trabalhou com a vítima?"

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
listaAssasino = []

a = input('Telefonou para a vitima?')
b = input('Esteve no local do crime?')
c = input('Mora perto da vitima?')
d = input('Devia para a vitima?')
e = input('Já trabalhou com a vitima?')


if a == 'sim':
    listaAssasino.append(a)
elif a == 'nao':
    inocente.append(a)
if b == 'sim':
    listaAssasino.append(b)
elif b == 'nao':
    inocente.append(b)
if c == 'sim':
    listaAssasino.append(c)
elif c == 'nao':
    inocente.append(c)
if d == 'sim':
    listaAssasino.append(d)
elif d == 'nao':
    inocente.append(d)
if e == 'sim':
    listaAssasino.append(e)
elif e == 'nao':
    inocente.append(e)
else:
    print('resposta inválida!')

if listaAssasino.count('sim') == 5:
    print('assasino!')



