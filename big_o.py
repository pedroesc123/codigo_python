import time
import math

def constante(n):
    return 1

def logaritmico(n):
    return math.log10(n)

def lineal(n):
    return n

def lin_log(n):
    return n * math.log10(n)

def cuadratica(n):
    return n ** 2

def exponencial(n):
    return 2 ** n

if __name__ == '__main__':
    n =[1, 10, 100, 1000, 10000]

    # for i in n:
        # comienzo = time.time()
        # print(constante(i))
        # final = time.time()
        # print(f'El tiempo usado es: {final - comienzo}')

        # comienzo = time.time()
        # print(logaritmico(i))
        # final = time.time()
        # print(f'El tiempo usado es: {final - comienzo}')

    comienzo = time.time()
    print(exponencial(10000))
    final = time.time()
    print(final - comienzo)

    print ('Ahora pasaremos al siguiente valor de n. \n')

