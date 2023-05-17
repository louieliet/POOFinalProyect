from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox
from PIL import Image, ImageTk
import csv

class Estacionamiento:
    def __init__(self):
        self.nombre = ""
        self.id = ""
        self.placas = ""
        self.hora_llegada = ""
        self.lugar = ""

    def set_data(self, nombre, id, placas, hora_llegada, lugar):
        self.nombre = nombre
        self.id = id
        self.placas = placas
        self.hora_llegada = hora_llegada
        self.lugar = lugar

    def print_data(self):
        print("Nombre:", self.nombre)
        print("ID:", self.id)
        print("Placas:", self.placas)
        print("Hora de llegada:", self.hora_llegada)
        print("Lugar:", self.lugar)

    def save_data(self, filename):
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file, delimiter="|")
            writer.writerow([self.nombre, self.id, self.placas, self.hora_llegada, self.lugar])

    def clear_data(self, filename):
        with open(filename, mode="w", newline="") as file:
            pass

class Estudiante(Estacionamiento):
    def __init__(self):
        super().__init__()
        self.carrera = ""
        self.ocupacion = "Estudiante"

    def set_carrera(self, carrera):
        self.carrera = carrera

class Profesor(Estacionamiento):
    def __init__(self):
        super().__init__()
        self.area = ""
        self.ocupacion = "Docente"

    def set_area(self, area):
        self.area = area

class ParkingApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Proyecto Programación Orientada a Objetos")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.bg_image = Image.open("bg.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

    def show_main_menu(self):
        self.clear_window()
        self.window.configure(bg="white")
        bg_label = Label(self.window, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        estacionamiento_label = Label(self.window, text="Bienvenido al Estacionamiento", font=("Arial", 16), bg="white")
        estacionamiento_label.pack(pady=20)
        menu_label = Label(self.window, text="Menú de opciones", font=("Arial", 14), bg="white")
        menu_label.pack(pady=20)
        register_student_button = Button(self.window, text="Registrar Alumnos", command=self.show_student_registration, font=("Arial", 12), height=2, width=15)
        register_student_button.pack()
        register_teacher_button = Button(self.window, text="Registrar Docentes", command=self.show_teacher_registration, font=("Arial", 12), height=2, width=15)
        register_teacher_button.pack()

    def show_student_registration(self):
        self.clear_window()
        self.window.configure(bg="white")
        bg_label = Label(self.window, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        title_label = Label(self.window, text="Registrar Alumnos", font=("Arial", 16), bg="white")
        title_label.pack(pady=20)
        name_label = Label(self.window, text="Nombre:", font=("Arial", 12), bg="white")
        name_label.pack()
        self.name_entry = Entry(self.window, font=("Arial", 12))
        self.name_entry.pack()
        id_label = Label(self.window, text="ID:", font=("Arial", 12), bg="white")
        id_label.pack()
        self.id_entry = Entry(self.window, font=("Arial", 12))
        self.id_entry.pack()
        plates_label = Label(self.window, text="Placas:", font=("Arial", 12), bg="white")
        plates_label.pack()
        self.plates_entry = Entry(self.window, font=("Arial", 12))
        self.plates_entry.pack()
        carrera_label = Label(self.window, text="Carrera:", font=("Arial", 12), bg="white")
        carrera_label.pack()
        self.carrera_entry = Entry(self.window, font=("Arial", 12))
        self.carrera_entry.pack()
        register_button = Button(self.window, text="Registrar", command=self.register_student, font=("Arial", 12), height=2, width=15)
        register_button.pack()
        back_to_menu = Button(text="Volver al menú", command=self.show_main_menu, font=("Arial", 12), height=2, width=15)
        back_to_menu.pack()


    def show_teacher_registration(self):
        self.clear_window()
        self.window.configure(bg="white")
        bg_label = Label(self.window, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        title_label = Label(self.window, text="Registrar Docentes", font=("Arial", 16), bg="white")
        title_label.pack(pady=20)
        name_label = Label(self.window, text="Nombre:", font=("Arial", 12), bg="white")
        name_label.pack()
        self.name_entry = Entry(self.window, font=("Arial", 12))
        self.name_entry.pack()
        id_label = Label(self.window, text="ID:", font=("Arial", 12), bg="white")
        id_label.pack()
        self.id_entry = Entry(self.window, font=("Arial", 12))
        self.id_entry.pack()
        plates_label = Label(self.window, text="Placas:", font=("Arial", 12), bg="white")
        plates_label.pack()
        self.plates_entry = Entry(self.window, font=("Arial", 12))
        self.plates_entry.pack()
        area_label = Label(self.window, text="Área:", font=("Arial", 12), bg="white")
        area_label.pack()
        self.area_entry = Entry(self.window, font=("Arial", 12))
        self.area_entry.pack()
        register_button = Button(self.window, text="Registrar", command=self.register_teacher, font=("Arial", 12), height=2, width=15)
        register_button.pack()
        back_to_menu = Button(text="Volver al menú", command=self.show_main_menu, font=("Arial", 12), height=2, width=15)
        back_to_menu.pack()

    def register_student(self):
        nombre = self.name_entry.get()
        id = self.id_entry.get()
        placas = self.plates_entry.get()
        carrera = self.carrera_entry.get()
        if nombre and id and placas and carrera:
            estudiante = Estudiante()
            estudiante.set_data(nombre, id, placas, "N/A", "N/A")
            estudiante.set_carrera(carrera)
            estudiante.save_data("estudiantes.csv")
            messagebox.showinfo("Registro Exitoso", "El alumno ha sido registrado exitosamente.")
            self.show_main_menu()
        else:
            messagebox.showerror("Error de Registro", "Por favor, complete todos los campos.")

    def register_teacher(self):
        nombre = self.name_entry.get()
        id = self.id_entry.get()
        placas = self.plates_entry.get()
        area = self.area_entry.get()

        if nombre and id and placas and area:
            profesor = Profesor()
            profesor.set_data(nombre, id, placas, "N/A", "N/A")
            profesor.set_area(area)
            profesor.save_data("profesores.csv")
            messagebox.showinfo("Registro Exitoso", "El docente ha sido registrado exitosamente.")
            self.show_main_menu()
        else:
            messagebox.showerror("Error de Registro", "Por favor, complete todos los campos.")

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def run(self):
        self.show_main_menu()
        self.window.mainloop()


app = ParkingApp()
app.run()