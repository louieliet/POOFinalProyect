import tkinter


import tkinter

win = tkinter.Tk()
win.geometry("500x500")

def hola(name):
    print("Hola putos" + name)


def savetext():
    texto = textbox.get()
    print(texto)

b1 = tkinter.Button(win, text = "Click", padx = 50, pady = 20, command = savetext)
b1.pack()


textbox = tkinter.Entry(win, font = "Helvetica")
textbox.pack()



text = tkinter.Label(win,text="Hola", bg = "blue")
text.pack(fill = tkinter.Y, expand= True)
win.mainloop()
