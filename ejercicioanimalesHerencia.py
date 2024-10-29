class Animal:
    def hacer_sonido(self):
        return "Sonido genérico de animal"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pío!"

# Crear instancias de Perro, Gato y Pájaro
perro = Perro()
gato = Gato()
pajaro = Pajaro()

# Mostrar los sonidos de cada animal
print(f"Sonido del perro: {perro.hacer_sonido()}")
print(f"Sonido del gato: {gato.hacer_sonido()}")
print(f"Sonido del pájaro: {pajaro.hacer_sonido()}")
