from datos.gestor_csv import GestorCSV

class Materia:
    def __init__(self):
        self.lista_docentes = []        # Lista recibida desde la clase Docente
        self.lista_estudiantes = []     # Lista recibida desde la clase Estudiante
        self.materias_asignadas = []    # Guarda relaciones docente-materia
        self.materias_estudiantes = []  # Guarda relaciones estudiante-materia

    # Recibir listas desde otras clases
    def recibir_docentes(self, lista_docentes):
        self.lista_docentes = lista_docentes

    def recibir_estudiantes(self, lista_estudiantes):
        self.lista_estudiantes = lista_estudiantes

    # Asignar materia a un docente
    def inscribir_materia_docente(self):
        if not self.lista_docentes:
            print("\n No hay docentes registrados aún. Agrega docentes antes de inscribir materias.\n")
            return

        print("\n Lista de docentes disponibles:\n")
        for docente in self.lista_docentes:
            print(f"ID: {docente[0]} - Nombre: {docente[1]} - Email: {docente[4]}")

        print("--------------------------------------")
        id_docente = input("Digite el id del docente al que le quiere inscribir materias: ")

        docente_encontrado = None

        for docente in self.lista_docentes:
            if docente[0] == id_docente:
                docente_encontrado = docente
                break

        if not docente_encontrado:
            print(f"No se encontró el docente con el id: {id_docente}")
            return

        nombre_materia = input("Digite el nombre de la materia: ")

        inscripcion_materias = [docente_encontrado[0], docente_encontrado[1], nombre_materia]
        self.materias_asignadas.append(inscripcion_materias)

        print(f"\nLa materia '{nombre_materia}' ha sido asignada correctamente al docente: {docente_encontrado[1]} (ID: {docente_encontrado[0]}).\n")

        print("Listado de materias asignadas a docentes:\n")
        for m in self.materias_asignadas:
            print(f"Docente: {m[1]} - Materia: {m[2]}")

        # Guarda los datos en un archivo CSV
        encabezados = ["Id", "Nombre", "Materia"]
        GestorCSV.añadir_datos_csv(
            nombre_archivo="inscribir_materia_docente.csv", 
            encabezados=encabezados, 
            datos=self.materias_asignadas
        )

    # Inscribir estudiante en una materia
    def inscribir_estudiante_materia(self):
        if not self.lista_estudiantes:
            print("\n No hay estudiantes registrados aún. Agrega estudiantes antes de inscribirlos en materias.\n")
            return

        if not self.materias_asignadas:
            print("\n No hay materias disponibles aún. Asigna materias a docentes antes de inscribir estudiantes.\n")
            return

        print("\n Lista de estudiantes disponibles:\n")
        for estudiante in self.lista_estudiantes:
            print(f"ID: {estudiante[0]} - Nombre: {estudiante[1]} - Email: {estudiante[4]}")

        id_estudiante = input("\nDigite el id del estudiante que desea inscribir: ")
        estudiante_encontrado = None

        for estudiante in self.lista_estudiantes:
            if estudiante[0] == id_estudiante:
                estudiante_encontrado = estudiante
                break

        if not estudiante_encontrado:
            print(f"No se encontró el estudiante con el id: {id_estudiante}")
            return

        print("\n Materias disponibles:\n")
        for m in self.materias_asignadas:
            print(f"{m[2]} - Docente: {m[1]} (ID: {m[0]})")

        nombre_materia = input("\nDigite el nombre de la materia a la que desea inscribir al estudiante: ")

        materia_encontrada = None
        for m in self.materias_asignadas:
            if m[2].lower() == nombre_materia.lower():
                materia_encontrada = m
                break

        if not materia_encontrada:
            print(f"No se encontró la materia '{nombre_materia}'.")
            return

        inscripcion_estudiante = [estudiante_encontrado[0], estudiante_encontrado[1], materia_encontrada[2]]
        self.materias_estudiantes.append(inscripcion_estudiante)

        print(f"\nEl estudiante '{estudiante_encontrado[1]}' ha sido inscrito correctamente en la materia '{materia_encontrada[2]}'.\n")

        print("Listado de inscripciones de estudiantes:\n")
        for ins in self.materias_estudiantes:
            print(f"Estudiante: {ins[1]} - Materia: {ins[2]}")
        # Guarda los datos en un archivo CSV
        encabezados = ["Id", "Nombre", "Materia"]
        GestorCSV.añadir_datos_csv(
            nombre_archivo="inscribir_materia_estudiante.csv", 
            encabezados=encabezados, 
            datos=self.materias_estudiantes
        )
    def obtener_materia_estudiantes(self):
        return self.materias_estudiantes