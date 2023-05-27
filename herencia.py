#HERENCIA: subclase hereda los atributos y metodos de una superclase (clase padre)
#no ahorra el error de los dos puntos (pass)
class Persona:
    def _init_(self, Nombre, Edad, DNI):
        self.nombre = Nombre
        self.edad = Edad
        self.dni = DNI
    def presentacion(self):
        print(f"Mucho gusto soy {self.nombre} tengo {self.edad} años")
persona1 = Persona("Angel", 27, "12345678")
persona1.presentacion()

class Docente(Persona):
    def _init_(self, Nombre, Edad, DNI, Especialidad, Submodulos, Universidad):
        super()._init_(Nombre, Edad, DNI)
        self.especialidad = Especialidad
        self.submodulos = Submodulos
        self.universidad = Universidad
docente1 = Docente("Andrea", 29, "87654321", "Matematica", "Algebra", "Cesde")
docente1.presentacion()
print(docente1.especialidad)

class Estudiante(Persona):
    def _init_(self, Nombre, Edad, DNI, Cursos, Aula, Semestre, Nota):
        super()._init_(Nombre, Edad, DNI)
        self.cursos = Cursos
        self.aula = Aula
        self.semestre = Semestre
        self.nota = Nota
    def Aprobacion(self):
        if self.nota >= 3.0:
            print("Aprobo")
        else:
            print("Reprobo")
Estudiante1 = Estudiante("Henry", 34, "12346897", "Python", 405, 3, 2.9)
Estudiante1.presentacion()
Estudiante1.Aprobacion()

