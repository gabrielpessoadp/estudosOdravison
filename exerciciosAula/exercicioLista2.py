#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#  encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
#  Após esta entrada de dados, faça:
#a. Mostre a quantidade de valores que foram lidos;
#b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#d. Calcule e mostre a soma dos valores;
#e. Calcule e mostre a média dos valores;
#f. Calcule e mostre a quantidade de valores acima da média calculada;
#g. Calcule e mostre a quantidade de valores abaixo de sete;
#h. Encerre o programa com uma mensagem;
valores = []
n = 0
valoresAcimaMedia = []
valoresAbaixoSete = []

while n != 1:
    n = float(input('Digite notas:'))
    if n == -1:
        break
    else:
        n = valores.append(n)
print(len(valores))

print(valores)

valores.reverse()

for i in range(len(valores)):
    print(valores[i])

print('soma dos valores é igual a:',sum(valores))

media = sum(valores)/len(valores)

print('a media é igual a:', media)

for num in range(len(valores)):
    if valores[num] > media:
        valoresAcimaMedia.append(num)

for num in range(len(valores)):
    if valores[num] < 7:
        valoresAbaixoSete.append(num)
        
print('quantidade de valores acima da média:', len(valoresAcimaMedia))
print('quantidade de valores abaixo da média:', len(valoresAbaixoSete))
print('PROGRAMA ENCERRADO!')

