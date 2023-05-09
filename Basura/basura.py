import unittest

cliente1= {
    "nombre" : "Pepe",
    "apellido":"Honguito",
}

cliente2= {
    "nombre" : "Pepa",
    "apellido": "Fernandez",
}

class Persona:
#    def __init__(self, persona:dict):
 #       self.nombre = persona.get ("nombre") # persona["nombre"]
  #      self.apellido = persona.get ("apellido")

#    def __init__ (self,nombre="",apellido=""):
 #       self.nombre=nombre
  #      self.apellido=apellido

   def __repr__(self): #"buscar para que sirve"
        return f"->Persona:{self.nombre}{self.apellido}"
        
    #def __str__(self): "buscar para que sirve"

if __name__ == "__main__":
    p1 = Persona(cliente1) #p1 y p2 punteros. (referencias en python, variable que borra la dirección de memoria de la RAM)
    p2 = Persona(cliente2) #el objeto es Persona()
    p3=p1
    print (p1)
    print (p2)
    print (p3)
