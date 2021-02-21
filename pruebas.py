def enum_exhaustiva():
    objetivo = int(input("Escoge un entero: "))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1


    if respuesta**2 == objetivo:
        print (f"La raíz cuadrada es {respuesta}")

    if respuesta**2 > objetivo:
        print (f"{objetivo} no tiene raíz cuadrada exacta")


def aprox_soluc():
    objetivo = int(input("Escoge un número: "))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No se encontro la raíz cuadrada de {objetivo}")
    else:
        print(f"La raíz cuadrada de {objetivo} es {respuesta}")

   
def binaria():
    """Hola"""
    objetivo = int(input("Escoge un entero: "))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f"bajo={bajo}, alto={alto}, respuesta={respuesta}")
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print (f"La raíz cuadrada de {objetivo} es la {respuesta}")
        
# opcion = int(input("ESCOGE TU OPCIÓN: "))

# if opcion == 1:
#     enum_exhaustiva()

# elif opcion == 2:
#     aprox_soluc()

# elif opcion == 3:
#     binaria()

# else:
#     print("Opción incorrecta")

