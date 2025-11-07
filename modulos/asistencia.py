from datos.gestor_csv import GestorCSV

class Asistencia:
    def __init__(self):
        self.lista_estudiantes_materias = []  # Se rellena desde Materia

    def recibir_estudiantes(self, lista_estudiantes_materias):
        self.lista_estudiantes_materias = lista_estudiantes_materias

    def registrar_inasistencias(self):
        if not self.lista_estudiantes_materias:
            print("\nNo hay estudiantes inscritos en materias.\n")
            return

        print("\nEstudiantes inscritos y sus materias:\n")
        for registro in self.lista_estudiantes_materias:
            print(f"ID: {registro[0]} - Nombre: {registro[1]} - Materia: {registro[2]}")

        id_est = input("\nDigite el ID del estudiante: ").strip()
        materia_nombre = input("Digite el nombre de la materia: ").strip()

        registro_encontrado = None
        for registro in self.lista_estudiantes_materias:
            if registro[0] == id_est and registro[2].lower() == materia_nombre.lower():
                registro_encontrado = registro
                break

        if not registro_encontrado:
            print("\nNo se encontró el estudiante en esa materia.")
            return

        while True:
            try:
                cantidad = int(input("\n¿Cuántas inasistencias desea registrar? "))
                if cantidad <= 0:
                    print("Debe ingresar al menos una fecha.")
                else:
                    break
            except ValueError:
                print("Ingrese un número entero válido.\n")

        datos_csv = []
        for i in range(cantidad):
            while True:
                fecha = input(f"Ingrese la fecha #{i+1} (dd/mm/aaaa): ").strip()

                partes = fecha.split("/")
                if len(partes) == 3 and all(p.isdigit() for p in partes):
                    dia, mes, anio = map(int, partes)
                    if 1 <= dia <= 31 and 1 <= mes <= 12 and anio >= 2000:
                        datos_csv.append([
                            registro_encontrado[0],
                            registro_encontrado[1],
                            registro_encontrado[2],
                            fecha
                        ])
                        break

                print("Formato inválido. Intente de nuevo (dd/mm/aaaa).")

        encabezados = ["ID Estudiante", "Nombre Estudiante", "Materia", "Fecha Inasistencia"]

        GestorCSV.añadir_datos_csv(
            nombre_archivo="asistencias.csv",
            encabezados=encabezados,
            datos=datos_csv
        )

        print(f"\nSe registraron {len(datos_csv)} fechas de inasistencia para {registro_encontrado[1]} en {registro_encontrado[2]}.\n")

        return datos_csv