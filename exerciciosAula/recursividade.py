#Escreva uma função que retorne o maior valor de uma lista de inteiros com n elementos;
lista = [2,4,5,8,10]
def recursividade(numeros):
    for i in lista:
        if numeros == max(lista):
            return max(lista)



    # for i in range(len(lista)):
     #   return max(lista)
    #print(max(lista))