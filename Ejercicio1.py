# EJERCICIO 1: HERENCIA Y ENCAPSULAMIENTO
#1. Clase base: Animal
#       Atributos encapsulados: _nombre, _edad
#       Métodos:
#              __init__(nombre, edad)
#              get_nombre(), get_edad()
#              hacer_sonido() (método abstracto, debe ser implementado por las clases hijas)
#2. Clase hija: Perro (hereda de Animal)
#       Atributo encapsulado: _raza
#       Métodos:
#              __init__(nombre, edad, raza)
#              hacer_sonido() → Devuelve "Guau guau"
#3. Clase hija: Gato (hereda de Animal)
#       Atributo encapsulado: _color
#       Métodos:
#              __init__(nombre, edad, color)
#              hacer_sonido() → Devuelve "Miau"

from abc import ABC, abstractmethod
import os
os.system("cls")

class Animal(ABC):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad
    
    @abstractmethod
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza
        
    def hacer_sonido(self):
        return "Guau guau"
    
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color
        
    def hacer_sonido(self):
        return "Miau"
    
# Crear instancias de Perro y Gato
perro1 = Perro("Rex", 5, "Labrador")
gato1 = Gato
("Mimi", 3, "Blanco")
# Mostrar información y sonidos
print(f"{perro1.get_nombre()} es un perro de raza {perro1._raza} y tiene {perro1.get_edad()} años. Sonido: {perro1.hacer_sonido()}")
print(f"{gato1.get_nombre()} es un gato de color {gato1._color} y tiene {gato1.get_edad()} años. Sonido: {gato1.hacer_sonido()}")
