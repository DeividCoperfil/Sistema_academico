from modelos.docente import Docente
from modelos.estudiante import Estudiante
from modelos.materia import Materia
from modulos.actividad import Actividad
from modulos.notas import Notas
from modulos.asistencia import Asistencia
from modulos.biblioteca import Biblioteca

# --- PROGRAMA PRINCIPAL ---
docente1 = Docente()
estudiante1 = Estudiante()
materia1 = Materia()
actividad1 = Actividad()
nota1 = Notas()
asistencia1 = Asistencia()
Libros1 = Biblioteca()

# (AQUÍ VA TODO TU CÓDIGO EXACTO DEL MENÚ, SIN CAMBIOS)
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar estudiante")
    print("2. Agregar docente")
    print("3. Inscribir materia (docente)")
    print("4. Inscribir estudiante en materia")
    print("5. Agregar actividad")
    print("6. Agregar notas a estudiante en materia")
    print("7. Añadir asistencia a materia")
    print("8. Acceder a biblioteca")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    # Validación: entrada vacía
    if opcion == "":
        print("\n Debes ingresar una opción.")
        continue

    # Validación: número entero
    try:
        opcion = int(opcion)
    except ValueError:
        print("\n Por favor ingrese un número válido.")
        continue

    # Validación: rango correcto
    if opcion < 1 or opcion > 8:
        print("\n Opción fuera de rango. Intente nuevamente.")
        continue

    # --- Ejecución de opciones ---
    if opcion == 1:
        estudiante1.agregar_estudiante()

    elif opcion == 2:
        docente1.agregar_docente()

    elif opcion == 3:
        # Verifica si hay docentes antes de asignar materias
        if not docente1.obtener_docentes():
            print("\n Primero debes agregar docentes antes de inscribir materias.\n")
        else:
            materia1.recibir_docentes(docente1.obtener_docentes())
            materia1.inscribir_materia_docente()

    elif opcion == 4:
        # Verifica si hay estudiantes y materias antes de inscribir
        if not estudiante1.obtener_estudiantes():
            print("\n Primero debes agregar estudiantes antes de inscribirlos en materias.\n")
        elif not materia1.materias_asignadas:
            print("\n No hay materias disponibles aún. Asigna materias a docentes primero.\n")
        else:
            materia1.recibir_estudiantes(estudiante1.obtener_estudiantes())
            materia1.inscribir_estudiante_materia()
    elif opcion == 5:
        actividad1.agregar_actividad()
    elif opcion == 6:
        if not materia1.obtener_materia_estudiantes():
            print("\n Primero debes agregar estudiantes y materias antes de agregar notas.\n")
        else:
            nota1.recibir_estudiantes(materia1.obtener_materia_estudiantes())
            nota1.agregar_notas_estudiantes()
    elif opcion ==7:
        if not materia1.obtener_materia_estudiantes():
            print("\n Primero debes agregar estudiantes y materias antes de agregar asistencia.\n")
        else:
            asistencia1.recibir_estudiantes(materia1.obtener_materia_estudiantes())
            asistencia1.registrar_inasistencias()

    elif opcion == 8:

        print("\nBienvenido al sistema de biblioteca")

        # Verifica si hay estudiantes o docentes
        if not estudiante1.obtener_estudiantes():
                print("\nPrimero debes agregar un estudiante.\n")
        
        
        else:
            accion = input("\n¿Que accion deseas hacer?, presiona\n1. Mostrar lista de libros\n2. Prestar libro\n3. Mostrar libros prestados\n4. Devolver un libro\nSelecciona una opcion: ")
            try:
                accion = int(accion)
            except ValueError:
                print("\nPor favor ingrese un número válido.")

            if accion == 1:

                Libros1.mostrar_libros()
            
            elif accion == 2:
                print("\nPrestamos")
                id_solicitado = input("\nIngrese su Id: ")
                nombre_libro = input("\nIngrese el nombre del libro que desea adquirir: ")

                tilin= estudiante1.buscar_estudiante(id_solicitado)
                
                if tilin:

                    Libros1.prestar_libros(tilin,nombre_libro)


                else:

                    print("\nNo se encontro estudiante con ese id")

            elif accion == 3:

                Libros1.mostrar_prestamos()

            elif accion == 4:

                print("\nDevolucion de libros")
                id_solicitado = input("\nIngrese su Id: ")
                nombre_libro = input("\nIngrese el nombre del libro que desea devolver: ")
                Libros1.devolver_libros(tilin,nombre_libro)
            else:
                print("Opcion no valida")     
    elif opcion == 9:
        print("\n Saliendo del programa...")
        break
