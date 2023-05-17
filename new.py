
from PIL import Image, ImageTk
import csv
import customtkinter as ctk

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
        self.root = ctk.CTk()
        self.root.title("Proyecto Programación Orientada a Objetos")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
    
    def show_main_menu(self):
        self.clear_root()
        self.root.configure(bg_color="#f2f2f2")  # Cambia el color de fondo
        

        estacionamiento_label = ctk.CTkLabel(self.root, text="Estacionamiento UP", font=ctk.CTkFont(size=40, weight="bold"))
        estacionamiento_label.pack(pady=40)

        menu_label = ctk.CTkLabel(self.root, text="Menú de opciones", font=ctk.CTkFont(size=30, weight="bold"))
        menu_label.pack(pady=20)

        menu_frame = ctk.CTkFrame(self.root)
        menu_frame.pack()

        button_frame = ctk.CTkFrame(menu_frame)
        button_frame.pack()

        register_student_button = ctk.CTkButton(button_frame, text="Registrar Estudiante", font=ctk.CTkFont(size=25, weight="bold"), command=self.show_student_registration)
        register_student_button.pack(pady=10, padx=20)

        register_teacher_button = ctk.CTkButton(button_frame, text="Registrar Profesor", font=ctk.CTkFont(size=25, weight="bold"), command=self.show_teacher_registration)
        register_teacher_button.pack(pady=10, padx=20)
    

    def show_student_registration(self):
        self.clear_root()

        title_label = ctk.CTkLabel(self.root, text="Registrar Alumnos", font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(pady=20)

        form_frame = ctk.CTkFrame(self.root)
        form_frame.pack()

        name_label = ctk.CTkLabel(form_frame, text="Nombre:", font=ctk.CTkFont(size=15))
        name_label.pack()
        self.name_entry = ctk.CTkEntry(form_frame, placeholder_text="Ej. Pedro")
        self.name_entry.pack(fill="x", padx=10, pady=5)

        id_label = ctk.CTkLabel(form_frame, text="ID:", font=ctk.CTkFont(size=15))
        id_label.pack()
        self.id_entry = ctk.CTkEntry(form_frame, placeholder_text="Ej. 0222222")
        self.id_entry.pack(fill="x", padx=10, pady=5)

        plates_label = ctk.CTkLabel(form_frame, text="Placas:", font=ctk.CTkFont(size=15))
        plates_label.pack()
        self.plates_entry = ctk.CTkEntry(form_frame, placeholder_text="Ej. H12VF")
        self.plates_entry.pack(fill="x", padx=10, pady=5)

        carrera_label = ctk.CTkLabel(form_frame, text="Carrera:", font=ctk.CTkFont(size=15))
        carrera_label.pack()
        self.carrera_entry = ctk.CTkEntry(form_frame, placeholder_text="Ej. Ing. en ...")
        self.carrera_entry.pack(fill="x", padx=10, pady=5)

        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=30)

        register_button = ctk.CTkButton(button_frame, text="Registrar", command=self.register_student, font=ctk.CTkFont(size=15, weight="bold"))
        register_button.pack(side="left", padx=10)

        back_to_menu = ctk.CTkButton(button_frame, text="Volver al menú", command=self.show_main_menu, font=ctk.CTkFont(size=15, weight="bold"))
        back_to_menu.pack(side="left", padx=10)

    def show_teacher_registration(self):
        self.clear_root()
        self.root.configure(bg="white")
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        title_label = Label(self.root, text="Registrar Docentes", font=("Arial", 16), bg="white")
        title_label.pack(pady=20)
        name_label = Label(self.root, text="Nombre:", font=("Arial", 12), bg="white")
        name_label.pack()
        self.name_entry = Entry(self.root, font=("Arial", 12))
        self.name_entry.pack()
        id_label = Label(self.root, text="ID:", font=("Arial", 12), bg="white")
        id_label.pack()
        self.id_entry = Entry(self.root, font=("Arial", 12))
        self.id_entry.pack()
        plates_label = Label(self.root, text="Placas:", font=("Arial", 12), bg="white")
        plates_label.pack()
        self.plates_entry = Entry(self.root, font=("Arial", 12))
        self.plates_entry.pack()
        area_label = Label(self.root, text="Área:", font=("Arial", 12), bg="white")
        area_label.pack()
        self.area_entry = Entry(self.root, font=("Arial", 12))
        self.area_entry.pack()
        register_button = Button(self.root, text="Registrar", command=self.register_teacher, font=("Arial", 12), height=2, width=15)
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

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.show_main_menu()
        self.root.mainloop()

app = ParkingApp()
app.run() 