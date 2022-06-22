valor = int(input('Qual o valor da compra? '))
formaPag = (input('Qual a forma de pagamento? '))
if valor >= 100 and formaPag == 'Dinheiro':
    valor = valor - (10/100)*valor
    print('O valor promocional foi de:',valor,'reais, e a forma de pagamento foi:',formaPag)
elif formaPag == 'Dinheiro':
    print('O valor foi de:',valor,'reais, e a forma de pagamento foi:',formaPag)
elif formaPag == 'Cheque':
    print('O valor foi de:',valor,'reais, e a forma de pagamento foi:',formaPag)
elif formaPag == 'Cartão':
    modoCard = input('Débito ou crédito?')
    if modoCard == ('Débito'):
        print('O valor foi de:',valor,'reais, e a forma de pagamento foi:',formaPag, modoCard)
    elif modoCard == ('crédito'):
        parcelas = int(input('Quantas parcelas vão ser? \n'))
        valorParcelado = (valor / parcelas)
        print('O valor foi de:',valor,'reais, dividido em', parcelas,'parcelas de', valorParcelado,'reais')
    else:
        print('Forma invalida')
else:
    print('Forma de pagamento ou valor inválido!')