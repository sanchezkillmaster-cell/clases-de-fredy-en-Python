# Código básico para ilustrar la ASOCIACIÓN entre clases

class Curso:

    def __init__(self, titulo):
        self.titulo = titulo

    def mostrar_info(self):
        print(f"Curso: {self.titulo}")


class Estudiante:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []  # Asociación con Curso

    def inscribirse(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"\nCursos inscritos por {self.nombre}:")

        if not self.cursos:
            print("No tiene cursos inscritos.")
        else:
            for curso in self.cursos:
                print(f"- {curso.titulo}")


# Programa principal

# Creación de cursos
curso1 = Curso("programacion orientada por objeto")
curso2 = Curso("Bases de Datos")
curso3 = Curso("machine learnig")

# Creación de estudiante
estudiante = Estudiante("carlos ")

# Inscripción a cursos
estudiante.inscribirse(curso1)
estudiante.inscribirse(curso2)
estudiante.inscribirse(curso3)

# Mostrar cursos inscritos
estudiante.mostrar_cursos()