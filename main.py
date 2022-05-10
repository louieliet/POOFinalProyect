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


#Init window
win = tk.Tk()

#Some other stuff
global entername
entername = StringVar()

#Creating the main menu

def mainmenu():

    for widget in win.winfo_children():
        widget.destroy()

    win.geometry("500x500")
    win.title("Proyecto Programación Orientada a Objetos")

    register = tk.Button(text="Registrar Usuarios", command=RegisterUsers)
    register.pack()
    
    consult = tk.Button(text="Consultar un usuario", command=ConsultUsers)
    consult.pack()

    win.mainloop()


def RegisterUsers():
    
    def setName():
        name = nombre.get()
        print(name)
        entername.set("")
    

    for widget in win.winfo_children():
        widget.destroy()

    win.title("Registrar Usuarios")
    
    text = tk.Label(text="Registrar Usuarios")
    text.pack()

    nombre = tk.Entry(bd=4,textvariable=entername)
    nombre.pack()

    registname = tk.Button(text="Guardar nombre", command=setName)
    registname.pack()
  

    win.mainloop()





def ConsultUsers():
    pass






if __name__ == "__main__":
    mainmenu()



"""""""""""""""
#Creating the register menu
Nombre = tk.Label(text="Introduzca su nombre: ")
Nombre.pack(pady=2,padx=2)
Nombreinput = tk.Entry(bd=4, textvariable=entername)
Nombreinput.pack(pady=5,padx=5)

#clear Function

def setName():
    name = Nombreinput.get()
    print(name)

SaveName = tk.Button(text="Guardar usuario",command=setName)
SaveName.pack()

Clear = tk.Button(text="Nuevo usuario",command=clear)
Clear.pack()


#Id
ID = tk.Label(text="Introduzca su id: ")
ID.pack(pady=2,padx=2)
IDinput = tk.Entry(bd=4, textvariable=entername)
IDinput.pack(pady=5,padx=5)


def setID():
    ID = IDinput.get()
    print(ID)

SaveID = tk.Button(text="Guardar ID",command=setName)
SaveID.pack()

Clear = tk.Button(text="Borrar",command=clear)
Clear.pack()

"""""""""


