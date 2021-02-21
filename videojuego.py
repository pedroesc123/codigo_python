import random

def run():
    numero_random = random.randint(1, 100)
    contador = 5
    
    while contador > 0:
        numero_escogido = int(input("Introduce un número del 1 al 100: "))
        if numero_escogido < numero_random:
            print ("El número escogido es menor al número aleatorio.")
            contador -= 1
            continue
        elif numero_escogido > numero_random:
            print ("El número escogido es mayor al número aleatorio.")
            contador -= 1
            continue 
        else:
            print ("Adivinaste el número. Felicidades!")
            break
    
    if contador == 0:
        print("Has perdido.")


if __name__ == "__main__":
    run()