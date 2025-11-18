from modelos.persona import Persona
from datos.gestor_csv import GestorCSV

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.registro = []

    def agregar_docente(self):
        print('--------------------------------------')
        while True:
            try:
                n = int(input("¿Cuántos registros deseas ingresar? "))
                if n <= 0:
                    print(" Debes ingresar al menos un registro.")
                else:
                    break
            except ValueError:
                print(" Por favor ingrese un número válido.")
        for i in range(n):
            print(f"\nRegistro {i+1}:")
            datos = self.solicitar_datos_persona()
            self.registro.append(datos)
        print("\n DOCENTES REGISTRADOS:")
        for d in self.registro:
            print(f"ID: {d[0]} | Nombre: {d[1]} | Edad: {d[2]} | Email: {d[4]}")
        encabezados = ["Id", "Nombre", "Edad", "Direccion", "Email", "Fecha_nacimiento"]
        GestorCSV.añadir_datos_csv("docentes.csv", encabezados, self.registro)

    def obtener_docentes(self):
        return self.registro

    def buscar_docente(self, id_buscar):
        for estudiante in self.registro:
            if estudiante[0] == id_buscar:
                return estudiante
        return None