import random


def ordenamiento_de_burbuja(lista):
    n = len(lista)
    paso = 0

    for i in range(n):
        for j in range(0, n - i -1):
            if lista[j] > lista[j+1]:
                valor = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = valor
            
            paso +=1

    return (lista, paso)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño será la lista: '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    (lista_ordenada, paso) = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
    print (paso)