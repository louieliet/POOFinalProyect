import tkinter as tk
from tkinter import *

#Creating all start stuff
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


#Estudiante object
p1 = Estudiante("Emi", 241718 ,"Estudiante","Animación","2do")


#Tkinter stuffs to start
win = tk.Tk()
win.geometry("500x500")
win.title("Proyecto Programación Orientada a Objetos")


#Some other stuff
global entername
entername = StringVar()


#Creating the main menu
Nombre = tk.Label(text="Introduzca su nombre: ")
Nombre.pack(pady=2,padx=2)
Nombreinput = tk.Entry(bd=4, textvariable=entername)
Nombreinput.pack(pady=5,padx=5)

#clear Function
def clear():
    entername.set("")

def setName():
    name = Nombreinput.get()
    print(name)

Clear = tk.Button(text="Nuevo usuario",command=clear)
Clear.pack()

SaveName = tk.Button(text="Guardar usuario",command=setName)
SaveName.pack()

win.mainloop()

