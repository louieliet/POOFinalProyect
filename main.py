from binascii import b2a_base64
import tkinter
import sys
from traceback import TracebackException


class ExcepcionHora(Exception):
    def __init__(self, hora):
        self.hora = hora


class Estacionamiento():
    def __init__(self, nombre, _id, ocupacion):
        self.nombre = nombre
        self.id = _id
        self.ocupacion = ocupacion
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
        running = True
        while running:
            try:
                self.__placas = str(input("Placas del coche: "))
                running = False
            except ValueError:
                print("Introduzca placas válidas")
    
class Estudiante(Estacionamiento):
    def __init__(self, nombre, id, ocupacion, carrera, semestre):
        super().__init__(nombre, id, ocupacion)
        self.carrera = carrera
        self.semestre = semestre
    
class Profesor(Estacionamiento):
    def __init__(self, nombre, id, ocupacion):
        super().__init__(nombre, id, ocupacion)

p1 = Estudiante("Emi", 241718 ,"Estudiante","Animación","2do")

win = tkinter.Tk()
win.geometry("500x500")


win.mainloop()