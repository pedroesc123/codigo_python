import time
import sys

sys.setrecursionlimit(2500)
print (sys.getrecursionlimit())

#Iterativo
def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

#Recursivo
def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n-1)


if __name__ == '__main__':
    n = 2200

    comienzo = time.time() #Significa que se esta ejecutando el modulo time
    # y adentro hay una función que se llama time
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)