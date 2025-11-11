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
    if opcion < 1 or opcion > 9:
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

        while True:
            pregunta = input("\nPresiona\n1. Estudiante\n2. Profesor\n3. Salir: ")

            if pregunta == "":
                print("\nDebes ingresar una opción.")
                continue

            try:
                pregunta = int(pregunta)
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            if pregunta < 1 or pregunta > 3:
                print("")
                print("-"*40)
                print("Opción no disponible. Intente nuevamente.")
                print("-"*40)
                continue

            if pregunta == 1:
                
                if not estudiante1.obtener_estudiantes():
                    print("\nNo hay estudiantes")
                
                else:
                    while True:
                        comando = input("\nElige una opcion\n1. Mostrar libros\n2. Solicitar un libro\n3. Devolver un libro\n4. Mostrar libros prestados\n5. Salir: ")

                        if comando == "":
                            print("\nDebes ingresar una opción.")
                            continue

                        try:
                            comando = int(comando)
                        except ValueError:
                            print("")
                            print("-"*40)
                            print("Ingrese un número válido.")
                            print("-"*40)
                            continue
            
                        if comando < 1 or comando > 5:
                            print("")
                            print("-"*40)
                            print("Opción no disponible. Intente nuevamente.")
                            print("-"*40)
                            continue

                        if comando == 1:

                            Libros1.mostrar_libros()

                        elif comando == 2:

                            print("\nPrestamo de libros")
                            
                            id_estudiante = input("\nIngrese el id del estudiante: ")
                            while not id_estudiante:
                                id_estudiante = input("\nDebe ingresar el id del estudiante: ")

                            libro_solicitado = input("\nIngrese el libro que desea adquirir: ")
                            while not libro_solicitado: 
                                libro_solicitado = input("\nDebe ingresar un libro: ")

                            encontrar_estudiante = estudiante1.buscar_estudiante(id_estudiante)
                            Libros1.prestar_libros(encontrar_estudiante,libro_solicitado)

                        elif comando == 3:

                            print("\nDevolucion de libros")
                            
                            id_estudiante = input("\nIngrese el id del estudiante: ")
                            while not id_estudiante:
                                id_estudiante = input("\nDebe ingresar el id del estudiante: ")

                            libro_solicitado = input("\nIngrese el libro que desea adquirir: ")
                            while not libro_solicitado: 
                                libro_solicitado = input("\nDebe ingresar un libro: ")
                            
                            encontrar_estudiante = estudiante1.buscar_estudiante(id_estudiante)
                            Libros1.devolver_libros(encontrar_estudiante,libro_solicitado)

                        elif comando == 4:

                            Libros1.mostrar_prestamos()

                        elif comando == 5:
                            print("\nSaliendo")
                            break


                        

            elif pregunta == 2:

                if not docente1.obtener_docentes():
                    print("\nNo hay docentes")

                else:
                    while True:
                        comando = input("\nElige una opcion\n1. Mostrar libros\n2. Solicitar un libro\n3. Devolver un libro\n4. Mostrar libros prestados\n5. Salir: ")

                        if comando == "":
                            print("\nDebes ingresar una opción.")
                            continue

                        try:
                            comando = int(comando)
                        except ValueError:
                            print("")
                            print("-"*40)
                            print("Ingrese un número válido.")
                            print("-"*40)
                            continue
            
                        if comando < 1 or comando > 5:
                            print("")
                            print("-"*40)
                            print("Opción no disponible. Intente nuevamente.")
                            print("-"*40)
                            continue

                        if comando == 1:

                            Libros1.mostrar_libros()

                        elif comando == 2:

                            print("\nPrestamo de libros")
                            
                            id_docente = input("\nIngrese el id del docente: ")
                            while not id_docente:
                                id_docente = input("\nDebe ingresar el id del docente: ")

                            libro_solicitado = input("\nIngrese el libro que desea adquirir: ")
                            while not libro_solicitado: 
                                libro_solicitado = input("\nDebe ingresar un libro: ")

                            encontar_docente = docente1.buscar_docente(id_docente)
                            Libros1.prestar_libros(encontar_docente,libro_solicitado)

                        elif comando == 3:

                            print("\nDevolucion de libros")
                            
                            id_docente = input("\nIngrese el id del docente: ")
                            while not id_docente:
                                id_docente = input("\nDebe ingresar el id del docente: ")

                            libro_solicitado = input("\nIngrese el libro que desea devolver: ")
                            while not libro_solicitado: 
                                libro_solicitado = input("\nDebe ingresar un libro: ")

                            encontar_docente = docente1.buscar_docente(id_docente)
                            Libros1.devolver_libros(encontar_docente,libro_solicitado)

                        elif comando == 4:

                            Libros1.mostrar_prestamos()

                        elif comando == 5:
                            print("\nSaliendo")
                            break

            elif pregunta == 3:
                print("\nSalir de biblioteca")
                break

             
    elif opcion == 9:
        print("\n Saliendo del programa...")
        break