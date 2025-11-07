from datos.gestor_csv import GestorCSV

class Notas:
    def __init__(self):
        self.lista_estudiantes_materias = []  # Se recibe desde Materia

    def recibir_estudiantes(self, lista_estudiantes_materias):
        self.lista_estudiantes_materias = lista_estudiantes_materias

    def agregar_notas_estudiantes(self):
        if not self.lista_estudiantes_materias:
            print("\nNo hay estudiantes inscritos en materias.\n")
            return

        print("\nEstudiantes inscritos en materias disponibles:\n")
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

        # Pedimos cuántas notas se quieren ingresar
        while True:
            try:
                n = int(input("\n¿Cuántas notas desea agregar? "))
                if n <= 0:
                    print("Debe ingresar al menos una nota.")
                else:
                    break
            except ValueError:
                print("Ingrese un número entero válido.")

        datos_csv = []
        for i in range(n):
            while True:
                try:
                    valor = float(input(f"Ingrese la nota #{i+1} (0.0 - 5.0): "))
                    if 0.0 <= valor <= 5.0:
                        datos_csv.append([registro_encontrado[0], registro_encontrado[1], registro_encontrado[2], valor])
                        break
                    print("La nota debe estar entre 0.0 y 5.0.")
                except ValueError:
                    print("Ingrese un número decimal válido.")

        # Guardamos en CSV correctamente
        encabezados = ["ID Estudiante", "Nombre Estudiante", "Materia", "Nota"]
        GestorCSV.añadir_datos_csv(
            nombre_archivo="notas.csv",
            encabezados=encabezados,
            datos=datos_csv
        )

        print(f"\nSe agregaron {len(datos_csv)} notas para {registro_encontrado[1]} en {registro_encontrado[2]}.\n")

        return datos_csv