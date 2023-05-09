#todo esto (las clases), son para guardar los datos en la base de datos.
# pass (=clase vacia)
#1 deficinicion N instancias
#con "def" en una clase ingreso metodos __init__ -> crea objetos en la clase (self(referencia a sí mismo, para ponerse cosas a sí mismo), param_nombre)
# param_nombre, sería la "variable" que le agregamos
#linea 8, self.nombre (a mímismo.nombre = a mi variable que le agregue)
#__init__ es el constructor la variable que ponemos al lado de self en este caso self.nombre, lo que pongamos en el = se le va a agregar el parámetro
#instancia que pongamos, no va a una variable, va a todas las variables asociadas al objeto, o sea "nombre"
#class Persona va a ser "HERENCIA"
#LO ÚNICO QUE VA CON MAYÚSCULAS SON LAS CLASES todo lo demás en minúscula.


class Persona:
    def __init__(self,param_nombre,param_apellido,param_email,num_celular):
        self.nombre= param_nombre
        self.apellido=param_apellido
        self.email = param_email
        self.num =num_celular

    def cambiar_nombre (self, nuevo_nombre):
        self.cambiar_nombre = nuevo_nombre
    def asistencia_clase(self):
        self.asistencia+=1


class Profesor(Persona):
    def __init__(self,param_nombre,param_apellido,param_email,num_celular, legajo_empleado):
            self.legajo_empleado = legajo_empleado
            super()(param_nombre,param_apellido,param_email,num_celular) #ejecutar "padre" que no se sobreescriba el último sobre el primero

    def __init__(self,param_nombre,param_email):
        self.asistencia = 0 #arranca siempre en 0 y no hace falta ponerlo en el self () esto es para asignar algo y que quede fijo

    def cambiar_nombre (self, nuevo_nombre):
        self.nombre = nuevo_nombre

profesor_pepe = Profesor("Pepe","pepe@um.edu.ar",62485)

print ("LA ID DEL PROFESOR ES...",id(profesor_pepe))

print ("EL NOMBRE DEL PROFESOR ES...",profesor_pepe.nombre)

print ("EL EMAIL DEL PROFESOR ES...",profesor_pepe.email)

print ("EL PROFESOR FUE A CLASES...",profesor_pepe.legajo_empleado)

print ("EL PROFESOR FUE A CLASES...",profesor_pepe.asistencia)

class Alumno(Persona):
    def __init__ (self,param_nombre,param_apellido,param_email,num_celular,cant_materia,numero_alumno)
        self.cant = cant_mat
        self.num_alum = numero_alumno
        self.materias_cursando =[]
        super()(param_nombre,param_apellido,param_email,num_celular)#arranca siempre en 0 y no hace falta ponerlo en el self () esto es para asignar algo y que quede fijo
    def __init__(self,param_nombre,param_email):
        self.asistencia =  0
    


alumno_luciana = Alumno("Luciana","Sosa","lg.sosa@alumno.um.edu.ar", 10, 2612740142 )

print ("LA ID DEL ALUMNO ES...", (id(alumno_luciana)))

print ("EL NOMBRE DEL ALUMNO ES...", alumno_luciana.nombre)

print ("EL APELLIDO DEL ALUMNO ES...", alumno_luciana.apellido)

print ("EL EMAIL DEL ALUMNO ES...",alumno_luciana.email)

print ("LAS CANTIDAD DE MATERIAS EN LA QUE ESTA INSCRIPTO EL ALUMNO...", alumno_luciana.cant_materia)

print ("EL NÚMERO DEL ALUMNO ES...",alumno_luciana.num)

print ("EL ALUMNO FUE A CLASES...",alumno_luciana.asistencia)

class Materia:
    def __init__(self,cant_alumnos):
        self.cant = cant_alumnos

materia_química = Materia (85)

print ("LA CANTIDAD DE ALUMNOS EN QUÍMICA ES...", materia_química.cant)