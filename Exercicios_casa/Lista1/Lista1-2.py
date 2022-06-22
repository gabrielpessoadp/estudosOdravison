pesoPrato = float(input('Digite o peso do seu prato em gramas: '))
if pesoPrato < 230:
     valorPrato = 0
     print('Seu prato está vázio!')
else:
    pesoPrato = (pesoPrato - 230)
    valorPrato = pesoPrato * 0.01
print('Seu prato totalizou um valor de: %.2f '% valorPrato, 'reais.')
