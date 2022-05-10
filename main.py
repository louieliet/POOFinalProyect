from  tkinter import *
from tkinter import ttk
import sys


class ExcepcionHora(Exception):
    def __init__(self, hora):
        self.hora = hora


class Estacionamiento():
    def __init__(self, nombre, _id, profesion):
        self.nombre = nombre
        self.id = _id
        self.profesion = profesion
        self.__placas = ""
        self.hora_llegada = 0
        self.lugar = 0
    
    def setHoradeLlegada(self):
        running = True

        while running:
            try:
                self.hora_llegada = int(input("Introduzca la hora de llegada: "))
                running = False
            except ValueError:
                print("Introduzca una hora válida")
        
    def setLugar(self):
        running = True
        while running:
            try:
                self.lugar = int(input("Introduzca el lugar (#) de estacionamiento: "))
                running = False
            except ValueError:
                print("Introduzca un valor válido")
          
    def setPlacas(self):
        try:
            self.__placas = str(input("Placas del coche: "))
        except ValueError:
            print("Introduzca placas válidas")
        
class Estudiante(Estacionamiento):
    def __init__(self, nombre, id, profesion, carrera, semestre):
        super().__init__(nombre, id, profesion)
        self.carrera = carrera
        self.semestre = semestre
    
class Profesor(Estacionamiento):
    def __init__(self, nombre, id, profesion):
        super().__init__(nombre, id, profesion)

p1 = Estudiante("Emi", 241718 ,"Estudiante","Animación","2do")

p1.setHoradeLlegada()
p1.setLugar()

print(p1.hora_llegada)
print(p1.lugar)
print(p1.id)


