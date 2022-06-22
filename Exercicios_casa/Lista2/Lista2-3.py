numero = int(input('Insira um número: '))
if numero%3==0:
    print('É um número multiplo de 3')
else:
    print('Não é multiplo de 3')
if 102%numero==0:
    print('É divisor de 102')
else:
    print('Não é divisor de 102')
if numero%2==0:
    print('O numero não é impar!')
elif numero%3==0:
    print('O numero é impar!')