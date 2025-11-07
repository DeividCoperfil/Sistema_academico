from datos.gestor_csv import GestorCSV

class Actividad:
    def __init__(self):
        self.actividades = []  # Lista donde se guardarán las actividades registradas

    def agregar_actividad(self):
        print("-------------------------------------")

        # Solicita los datos de la persona a la que se asocia la actividad
        print("\n--- Datos de la persona asociada ---")
        id_persona = input("ID de la persona: ").strip()
        while not id_persona:
            id_persona = input("El ID no puede estar vacío: ").strip()

        nombre_persona = input("Nombre de la persona: ").strip()
        while not nombre_persona:
            nombre_persona = input("El nombre no puede estar vacío: ").strip()

        email_persona = input("Email de la persona: ").strip()
        while not email_persona:
            email_persona = input("El email no puede estar vacío: ").strip()

        # Solicita cuántas actividades se desean registrar
        while True:
            try:
                n = int(input("\n¿Cuántas actividades deseas registrar? "))
                if n <= 0:
                    print(" Debes ingresar al menos una actividad.")
                else:
                    break
            except ValueError:
                print(" Por favor ingresa un número válido.")

        # Registro de cada actividad
        for i in range(n):
            print(f"\nRegistro de actividad {i+1}:")
            id_actividad = input("ID de la actividad: ").strip()
            while not id_actividad:
                id_actividad = input("El ID no puede estar vacío: ").strip()

            tipo_actividad = input("Tipo de actividad (Futbol,Lectura,Baile): ").strip()
            while not tipo_actividad:
                tipo_actividad = input("El tipo no puede estar vacío: ").strip()

            descripcion = input("Descripción (opcional): ").strip() or "Sin descripción"

            # Guarda la actividad asociada a la persona
            self.actividades.append([
                id_actividad,
                tipo_actividad,
                descripcion,
                id_persona,
                nombre_persona,
                email_persona
            ])

        # Muestra en pantalla todas las actividades registradas
        print("\nACTIVIDADES REGISTRADAS:")
        for act in self.actividades:
            print(f"Actividad: {act[1]} -- Tipo: {act[2]} -- Persona: {act[4]}")

        # Guarda las actividades en un archivo CSV
        encabezados = ["id_actividad", "tipo_actividad", "descripcion", "id_persona", "nombre_persona", "email_persona"]
        GestorCSV.añadir_datos_csv(
            nombre_archivo="actividades.csv", 
            encabezados=encabezados, 
            datos=self.actividades
        )