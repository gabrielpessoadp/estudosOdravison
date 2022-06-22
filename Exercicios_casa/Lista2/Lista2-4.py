valor = int(input('Qual o valor da compra? '))
formaPag = (input('Qual a forma de pagamento? '))
if valor >= 100 and formaPag == 'Dinheiro':
    valor = valor - (10/100)*valor
    print('O valor promocional foi de:',valor,'reais, e a forma de pagamento foi:',formaPag)
elif formaPag == 'Dinheiro':
    print('O valor foi de:',valor,'reais, e a forma de pagamento foi:',formaPag)
elif formaPag == 'Cheque':
    print('O valor foi de:',valor,'reais, e a forma de pagamento foi:',formaPag)
else:
    print('Forma de pagamento ou valor inválido!')