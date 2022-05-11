from random import random
import tkinter as tk
from tkinter import *
import tkinter
from typing import final
import random
import csv

#Creating all start stuff
class Estacionamiento():
    def __init__(self):
        self.nombre = " "
        self.id = " "
        self.__placas = ""
        self.hora_llegada = 0
        self.lugar = 0

    def setName(self,name):
        self.nombre = name

    def setID(self, iD):
        self.id = iD

    def setHoradeLlegada(self, hora):
        self.hora_llegada = hora
        
    def setLugar(self, lugar):
        running = True
        while running:
            try:
                self.lugar = lugar
                running = False
            except ValueError:
                print("Introduzca un valor válido")
          
    def setPlacas(self, placas):
        running = True
        while running:
            try:
                self.__placas = placas
                running = False
            except ValueError:
                print("Introduzca placas válidas")

    def printData(self):
        print(vars(self))

    def getPlacas(self):
        return self.__placas

class Estudiante(Estacionamiento):
    def __init__(self):
        self.carrera = " "
        self.ocupacion = "Estudiante"
        self.lista = []
    
    def setCarrera(self, carrera):
        self.carrera = carrera

    def outSData(self):
        with open("studentdata.csv",mode="a") as studentdata:
            studentdata = csv.writer(studentdata, delimiter=",")
            studentdata.writerow([self.nombre,self.id,self.carrera,self.getPlacas(),self.hora_llegada,self.lugar,self.ocupacion])
    def clearSData(self):
        with open("studentdata.csv",mode="w") as studentdata:
            studentdata = csv.writer(studentdata, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
            studentdata.writerow(" ")
class Profesor(Estacionamiento):
    def __init__(self):
        self.area = ""
        self.ocupacion = "Docente"

    def setArea(self, area):
        self.area = area
        
    def outTData(self):
        with open("teacherdata.csv",mode="a") as teacherdata:
            teacherdata = csv.writer(teacherdata, delimiter=",")
            teacherdata.writerow([self.nombre,self.id,self.hora_llegada, self.lugar, self.getPlacas(),self.area,self.ocupacion])
    def clearTData(self):
        with open("teacherdata.csv",mode="w") as teacherdata:
            teacherdata = csv.writer(teacherdata, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
            teacherdata.writerow(" ")


#Init window
win = tk.Tk()

#Some other stuff
global entername, enterid, entercarrera, enterhora, enterlugar, enterplacas, enterarea
entername = StringVar()
enterid = StringVar()
entercarrera = StringVar()
enterhora = StringVar()
enterlugar = StringVar()
enterplacas = StringVar()
enterarea = StringVar()


studentdatabase = "studentdata.csv"

#Creating the main menu

def mainmenu():

    for widget in win.winfo_children():
        widget.destroy()

    win.geometry("500x500")
    win.title("Proyecto Programación Orientada a Objetos")

    registerstudent = tk.Button(text="Registrar Alumno", command=RegistStudents)
    registerstudent.pack()

    registerteacher = tk.Button(text="Registrar Profesor", command=RegistTeachers)   
    registerteacher.pack()
    
    consults = tk.Button(text="Consultar un estudiante", command=ConsultStudent)
    consults.pack()

    consultt = tk.Button(text="Consultar un docente", command=ConsultTeacher)
    consultt.pack()

    win.mainloop()


#Function and menu to students

def RegistStudents():

    listStudents = []
    student = Estudiante()
    student.clearSData()

    def finalRegister():
        name = NOMBRE.get()
        iD = ID.get()
        carrera = CARRERA.get()
        placas = PLACAS.get()
        hora = HORA.get()
        lugar = LUGAR.get()

        for i in range(1):
            student.setName(name)
            student.setID(iD)
            student.setCarrera(carrera)
            student.setPlacas(placas)
            student.setHoradeLlegada(hora)
            student.setLugar(lugar)
            listStudents.append(student)
            student.printData()
            student.outSData()

        entername.set("")
        enterid.set("")
        entercarrera.set("")
        enterplacas.set("")
        enterhora.set("")
        enterlugar.set("")
    

    for widget in win.winfo_children():
        widget.destroy()

    win.title("Registrar Usuarios")
    
    text = tk.Label(text="Registrar Alumnos")
    text.pack()


    #Registro nombre 
    nombrescreen = tk.Label(win,text= "Nombre: ")
    nombrescreen.pack()

    NOMBRE = tk.Entry(bd=4,textvariable=entername)
    NOMBRE.pack()

    #Registro id
    idscreen = tk.Label(win, text= "ID: ")
    idscreen.pack()

    ID = tk.Entry(bd=4,textvariable=enterid)
    ID.pack()

    #Registro carrera

    carrerascreen = tk.Label(win,text="Carrera: ")
    carrerascreen.pack()

    CARRERA = tk.Entry(bd=4,textvariable=entercarrera)
    CARRERA.pack()

    #Registro placas
    
    placasscreen = tk.Label(win, text= "Placas: ")
    placasscreen.pack()

    PLACAS = tk.Entry(bd=4,textvariable=enterplacas)
    PLACAS.pack()
    
    #Registro hora

    horascreen = tk.Label(win, text="Hora:")
    horascreen.pack()

    HORA = tk.Entry(bd=4,textvariable=enterhora)
    HORA.pack()

    #Registro lugar

    lugarscreen = tk.Label(win, text="Lugar: ")
    lugarscreen.pack()

    LUGAR = tk.Entry(bd=4,textvariable=enterlugar)
    LUGAR.pack()

    registname = tk.Button(text="Guardar nombre", command=finalRegister)
    registname.pack()

    back_to_menu = tk.Button(text="Volver al menú", command=mainmenu)
    back_to_menu.pack()

    
    win.mainloop()



#Regist Teachers
def RegistTeachers():
    
    listTeachers = []
    teachers = Profesor()
    teachers.clearTData()
    def finalRegister():
        name = NOMBRE.get()
        iD = ID.get()
        hora = HORA.get()
        lugar = LUGAR.get()
        placas = PLACAS.get()
        area = AREA.get()

        for i in range(1):
            teachers.setName(name)
            teachers.setID(iD)
            teachers.setArea(area)
            teachers.setPlacas(placas)
            teachers.setHoradeLlegada(hora)
            teachers.setLugar(lugar)
            listTeachers.append(teachers)
            teachers.printData()
            teachers.outTData()

        entername.set("")
        enterid.set("")
        enterarea.set("")
        enterplacas.set("")
        enterhora.set("")
        enterlugar.set("")
    

    for widget in win.winfo_children():
        widget.destroy()

    win.title("Registrar Docentes")
    
    text = tk.Label(text="Registrar Docentes")
    text.pack()


    #Registro nombre 
    nombrescreen = tk.Label(win,text= "Nombre: ")
    nombrescreen.pack()

    NOMBRE = tk.Entry(bd=4,textvariable=entername)
    NOMBRE.pack()

    #Registro id
    idscreen = tk.Label(win, text= "ID: ")
    idscreen.pack()

    ID = tk.Entry(bd=4,textvariable=enterid)
    ID.pack()

    #Registro carrera

    carrerascreen = tk.Label(win,text="Área: ")
    carrerascreen.pack()

    AREA = tk.Entry(bd=4,textvariable=enterarea)
    AREA.pack()

    #Registro placas
    
    placasscreen = tk.Label(win, text= "Placas: ")
    placasscreen.pack()

    PLACAS = tk.Entry(bd=4,textvariable=enterplacas)
    PLACAS.pack()
    
    #Registro hora

    horascreen = tk.Label(win, text="Hora:")
    horascreen.pack()

    HORA = tk.Entry(bd=4,textvariable=enterhora)
    HORA.pack()

    #Registro lugar

    lugarscreen = tk.Label(win, text="Lugar: ")
    lugarscreen.pack()

    LUGAR = tk.Entry(bd=4,textvariable=enterlugar)
    LUGAR.pack()

    registname = tk.Button(text="Guardar nombre", command=finalRegister)
    registname.pack()

    back_to_menu = tk.Button(text="Volver al menú", command=mainmenu)
    back_to_menu.pack()

    win.mainloop()


def ConsultStudent():

    with open("studentdata.csv", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    with open("teacherdata.csv", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    for widget in win.winfo_children():
        widget.destroy()
    
    namerequest = tk.Label(text="Introduzca su nombre:")
    entername = tk.Entry(bd=4)
    idrequest = tk.Label(text="Introduzca su ID:")
    enterid = tk.Entry(bd=4)
    namerequest.pack()
    entername.pack()
    idrequest.pack()
    enterid.pack()

    nombre = entername.get()
    iD = enterid.get()

    win.mainloop()

def ConsultTeacher():

    for widget in win.winfo_children():
        widget.destroy()
    
    namerequest = tk.Label(text="Introduzca su nombre:")
    entername = tk.Entry(bd=4)
    idrequest = tk.Label(text="Introduzca su ID:")
    enterid = tk.Entry(bd=4)
    namerequest.pack()
    entername.pack()
    idrequest.pack()
    enterid.pack()

    nombre = entername.get()
    iD = enterid.get()

    win.mainloop()

    
if __name__ == "__main__":
    mainmenu()







