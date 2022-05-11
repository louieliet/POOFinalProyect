from random import random
import tkinter as tk
from tkinter import *
import tkinter
from turtle import back, bgcolor
from typing import final
import random
import csv
from PIL import Image
from PIL import ImageTk


#Creating the abstract class: Parking lot
class Estacionamiento():
    def __init__(self):
        self.nombre = " "
        self.id = " "
        self.__placas = ""
        self.hora_llegada = 0
        self.lugar = 0

    #method to enter the name
    def setName(self,name):
        self.nombre = name

    #method to enter the ID
    def setID(self, iD):
        self.id = iD

    #method to enter the arrival time
    def setHoradeLlegada(self, hora):
        self.hora_llegada = hora
        
    #method to enter the parking lot's place
    def setLugar(self, lugar):
        running = True
        while running:
            try:
                self.lugar = lugar
                running = False
            except ValueError:
                print("Introduzca un valor válido")
          
    #method to enter the license plate
    def setPlacas(self, placas):
        running = True
        while running:
            try:
                self.__placas = placas
                running = False
            except ValueError:
                print("Introduzca placas válidas")

    #method to print all the user's information
    def printData(self):
        print(vars(self))

    #method to get the license plate
    def getPlacas(self):
        return self.__placas


#Creating the concrete class: Student
class Estudiante(Estacionamiento):
    def __init__(self):
        self.carrera = " "
        self.ocupacion = "Estudiante"
    
    #method to enter the student's career
    def setCarrera(self, carrera):
        self.carrera = carrera

    #method to print the students' text file
    def outSData(self):
        with open("studentdata.csv",mode="a") as studentdata:
            studentdata = csv.writer(studentdata, delimiter="|")
            studentdata.writerow(["Nombre | ID | Carrera | Placas | Hora de llegada | Lugar"])
            studentdata.writerow([self.nombre,self.id,self.carrera,self.getPlacas(),self.hora_llegada,self.lugar])
    
    #method to clear the students' text file
    def clearSData(self):
        with open("studentdata.csv",mode="w") as studentdata:
            studentdata = csv.writer(studentdata, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
            studentdata.writerow(" ")


#Creating the concrete class: Teacher
class Profesor(Estacionamiento):
    def __init__(self):
        self.area = ""
        self.ocupacion = "Docente"

    #method to set the teachers' work area
    def setArea(self, area):
        self.area = area

    #method to print the teachers' text file
    def outTData(self):
        with open("teacherdata.csv",mode="a") as teacherdata:
            teacherdata = csv.writer(teacherdata, delimiter="|")
            teacherdata.writerow(["Nombre | ID | Area | Placas | Hora de llegada | Lugar "])
            teacherdata.writerow([self.nombre,self.id,self.area,self.getPlacas(),self.hora_llegada,self.lugar])
    
    #method to clear the teachers' text file
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

    
    image = Image.open("bg.jpg")
    image = ImageTk.PhotoImage(image)

    bg = tk.Label(win,image=image)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    
    win.geometry("500x500")
    win.title("Proyecto Programación Orientada a Objetos")
    
    
    estacionamiento = tk.Label(text="Bienvenido al Estacionamiento")
    welcome = tk.Label(text="Menú de opciones")
    estacionamiento.pack()
    welcome.pack()

    registerstudent = tk.Button(text="Registrar Alumnos", command=RegistStudents, height="5", width="15")
    registerstudent.pack()

    registerteacher = tk.Button(text="Registrar Docentes", command=RegistTeachers, height="5", width="15")   
    registerteacher.pack()
    
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

    image = Image.open("bg2.jpg")
    image = ImageTk.PhotoImage(image)

    bg = tk.Label(win,image=image)
    bg.place(x=0, y=0, relwidth=1, relheight=1)

    win.title("Registrar Alumnos")
    win.resizable = False
    
    text = tk.Label(text="Registrar Alumnos")
    text.pack()


    #register the name 
    nombrescreen = tk.Label(win,text= "Nombre: ")
    nombrescreen.pack()

    NOMBRE = tk.Entry(bd=4,textvariable=entername)
    NOMBRE.pack()

    #register the id
    idscreen = tk.Label(win, text= "ID: ")
    idscreen.pack()

    ID = tk.Entry(bd=4,textvariable=enterid)
    ID.pack()

    #register the career
    carrerascreen = tk.Label(win,text="Carrera: ")
    carrerascreen.pack()

    CARRERA = tk.Entry(bd=4,textvariable=entercarrera)
    CARRERA.pack()

    #register the licence plate
    placasscreen = tk.Label(win, text= "Placas: ")
    placasscreen.pack()

    PLACAS = tk.Entry(bd=4,textvariable=enterplacas)
    PLACAS.pack()
    
    #register the arrival time
    horascreen = tk.Label(win, text="Hora:")
    horascreen.pack()

    HORA = tk.Entry(bd=4,textvariable=enterhora)
    HORA.pack()

    #register the parking lot's place
    lugarscreen = tk.Label(win, text="Lugar: ")
    lugarscreen.pack()

    LUGAR = tk.Entry(bd=4,textvariable=enterlugar)
    LUGAR.pack()

    #save name button
    registname = tk.Button(text="Guardar nombre", command=finalRegister)
    registname.pack()

    #back to menu button
    back_to_menu = tk.Button(text="Volver al menú", command=mainmenu)
    back_to_menu.pack()

    
    win.mainloop()



#Regist Teachers
def RegistTeachers():
    win.resizable = False   
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

    image = Image.open("bg3.jpg")
    image = ImageTk.PhotoImage(image)

    bg = tk.Label(win,image=image)
    bg.place(x=0, y=0, relwidth=1, relheight=1)
    

    win.title("Registrar Docentes")
    
    text = tk.Label(text="Registrar Docentes")
    text.pack()


    #register the name
    nombrescreen = tk.Label(win,text= "Nombre: ")
    nombrescreen.pack()

    NOMBRE = tk.Entry(bd=4,textvariable=entername)
    NOMBRE.pack()

    #register the id
    idscreen = tk.Label(win, text= "ID: ")
    idscreen.pack()

    ID = tk.Entry(bd=4,textvariable=enterid)
    ID.pack()

    #register the career
    carrerascreen = tk.Label(win,text="Área: ")
    carrerascreen.pack()

    AREA = tk.Entry(bd=4,textvariable=enterarea)
    AREA.pack()

    #register the license plate
    placasscreen = tk.Label(win, text= "Placas: ")
    placasscreen.pack()

    PLACAS = tk.Entry(bd=4,textvariable=enterplacas)
    PLACAS.pack()
    
    #register the arrival time
    horascreen = tk.Label(win, text="Hora:")
    horascreen.pack()

    HORA = tk.Entry(bd=4,textvariable=enterhora)
    HORA.pack()

    #register the parking lot's place
    lugarscreen = tk.Label(win, text="Lugar: ")
    lugarscreen.pack()

    LUGAR = tk.Entry(bd=4,textvariable=enterlugar)
    LUGAR.pack()

    #save name button
    registname = tk.Button(text="Guardar nombre", command=finalRegister)
    registname.pack()

    #Back to menu button
    back_to_menu = tk.Button(text="Volver al menú", command=mainmenu)
    back_to_menu.pack()

    win.mainloop()
    
if __name__ == "__main__":
    mainmenu()







