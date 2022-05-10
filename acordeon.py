import tkinter


def hola(name):
    print("Hola, " + name)


def savetext():
    texto = cajitadetexto.get()
    print(texto)


pantalla = tkinter.Tk()
pantalla.geometry("500x500")


cajitadetexto = tkinter.Entry(pantalla, font="Helvetica 20")
cajitadetexto.pack()

texto = tkinter.Label(pantalla,text="Hola", bg = "red")
texto.pack(side = tkinter.TOP)
texto.pack(fill = tkinter.Y, expand= True)


boton1 = tkinter.Button(pantalla, text = "Play", command = savetext)
boton1.pack()


pantalla.mainloop()
