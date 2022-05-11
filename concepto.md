Inicio del programa:
    - Dos botones:
        1. Ingresar un nuevo usuario
        2. Consultar un usuario registrado
    
    En consultar, ingresar ID, y desplegar información
    En ingresar, meter todos los datos 

        self.nombre = " "
        self.id = " "
        self.__placas = ""
        self.hora_llegada = 0
        self.lugar = 0



    
    listStudents = []
    student = Estudiante()

    for i in range(1):
        student.setName()
        student.setID()
        student.setCarrera()
        student.setPlacas()
        student.setHoradeLlegada()
        student.setLugar()
        listStudents.append(student)

    for i in range (len(listStudents)):
        listStudents[i].printData()



Profe:
    nombre
    id
    hora
    lugar
    placas
    area
    ocupacion