import tkinter

from tkinter import *

global entername



def hola(name):
    print("Hola, " + name)


def savetext():
    texto = cajitadetexto.get()
    print(texto)

def reset():
    entername.set(" ")

pantalla = tkinter.Tk()
pantalla.geometry("500x500")

entername = StringVar(pantalla)

cajitadetexto = tkinter.Entry(pantalla, font="Helvetica 20")
cajitadetexto.pack()

texto = tkinter.Label(pantalla,text="Hola", bg = "red")
texto.pack(side = tkinter.TOP)  
texto.pack(fill = tkinter.Y, expand= True)


boton1 = tkinter.Button(pantalla, text = "Play", command = savetext)
boton1.pack()

button2 = tkinter.Button(pantalla, text="Reset", command=reset)
button2.pack()


b1 = tkinter.Button(pantalla, text= "Click")
b2 = tkinter.Button(pantalla, text= "Click2")
b3 = tkinter.Button(pantalla, text= "Click3")

b1.grid(row = 0, column = 0)
b2.grid(row = 1, column = 0)
b3.grid(row = 2, column = 0)



pantalla.mainloop()
