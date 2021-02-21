
# class Rectangulo:

#     def __init__(self, base, altura):
#         self.base = base
#         self. altura = altura

#     def area(self):
#         return self.base * self. altura

# class Cuadrado(Rectangulo):

#     def __init__(self, lado):
#         super().__init__(lado, lado)


# if __name__ == '__main__':
#     rectangulo = Rectangulo(base=3, altura=4)
#     print(rectangulo.area())

#     cuadrado = Cuadrado(lado = 5)
#     print(cuadrado.area())

class Electrodomesticos:

    def __init__(self, nombre, uso):
        self.nombre = nombre
        self.uso = uso

    def imprimir_nombre(self):
        print(f'El electrodomestico escogido es: {self.nombre}')

class Refrigeradora(Electrodomesticos):

    def __init__(self, nombre, uso, marca):
        super().__init__(nombre, uso)
        self.marca = marca
        

if __name__ == '__main__':
    electrodomestico = Electrodomesticos('cocina', 'cocinar')
    electrodomestico.imprimir_nombre()

    refrigeradora = Refrigeradora('Refrigeradora', 'Congelar', 'Samsung')
    refrigeradora.imprimir_nombre()