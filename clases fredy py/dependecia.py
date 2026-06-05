# Código básico para ilustrar la DEPENDENCIA entre clases
class BaseDatos:

    def conectar(self):
        return "Conexión establecida con la base de datos"

    def obtener_datos(self):
        return ["Juan", "María", "Carlos"]


class Reporte:

    def generar_reporte(self, base_datos):
        print("Generando reporte...")

        print(base_datos.conectar())

        datos = base_datos.obtener_datos()

        print("\nContenido del reporte:")
        for persona in datos:
            print(f"- {persona}")


# Programa principal
bd = BaseDatos()

reporte = Reporte()

# Dependencia: Reporte usa temporalmente BaseDatos
reporte.generar_reporte(bd)

