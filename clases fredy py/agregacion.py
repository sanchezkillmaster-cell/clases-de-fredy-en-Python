#Código para ilustrar la relación de AGREGACION entre clases
class Profesor:

    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        print(f"Profesor {self.nombre} creado.")

    def mostrar_info(self):
        print(f"Profesor: {self.nombre} - Especialidad: {self.especialidad}")

class Departamento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores = []
        print(f"Departamento {self.nombre} creado.")

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def listar_profesores(self):
        print(f"\nDepartamento: {self.nombre}")

        if len(self.profesores) == 0:
            print("No hay profesores asignados.")
        else:
            for profesor in self.profesores:
                print(f"- {profesor.nombre}")

    def __del__(self):
        print(f"Departamento {self.nombre} eliminado.")


# Programa principal

# Los profesores existen independientemente
prof1 = Profesor("Laura Torres", "Matemáticas")
prof2 = Profesor("Carlos Ramírez", "Programación")
prof3 = Profesor("Ana Gómez", "Bases de Datos")

# Se crea el departamento
departamento = Departamento("Ingeniería de Sistemas")

# Se agregan profesores al departamento
departamento.agregar_profesor(prof1)
departamento.agregar_profesor(prof2)
departamento.agregar_profesor(prof3)

# Mostrar profesores del departamento
departamento.listar_profesores()

print("\n--- El departamento desaparece ---")

del departamento

print("\nLos profesores siguen existiendo:")

prof1.mostrar_info()
prof2.mostrar_info()
prof3.mostrar_info()

print("\nFin del programa.")
