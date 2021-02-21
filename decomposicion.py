
class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en movimiento'

    def desacelerar(self, tipo = 'despacio'):
        if tipo == 'rapido':
            self._motor.variar_velocidad(5)
        else:
            self._motor.variar_velocidad(2)


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self. temperatura = 0

    def inyecta_gasolina(self, cantidad):
        print(f'Necesitas inyectar {cantidad} litros')

    def variar_velocidad(self, velocidad):
        print(f'Reduce la velocidad en {velocidad} m/s')


if __name__ == '__main__':
    carro_1 = Automovil('GRC8', 'Audi', 'rojo')
    carro_1.acelerar('rapida')
    carro_1.desacelerar()