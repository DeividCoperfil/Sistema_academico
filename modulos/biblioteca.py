class Biblioteca:

    def __init__(self):
        self.lista_libros = [["principito",True],
                             ["pinocho",True],
                             ["matilda",True],
                             ["momo",True],
                             ["programacion",True],
                             ["medicina",True],
                             ["historia",True],
                             ["ingles",True],
                             ["calculo",True],
                             ["videojuegos",True]
                             ]
        self.prestamos = []

    def mostrar_libros(self):
        print("")
        print("Libro"," Estado")
        for x in self.lista_libros:
            estado = "disponible" if x[1] else "Prestado"
            print("")
            print(f"{x[0]} {estado}")


    def prestar_libros(self,persona,nombre_libro):
        for x in self.lista_libros:
            if x[0] == nombre_libro:
                if x[1]:
                    x[1] = False
                    self.prestamos.append([persona[0],nombre_libro])
                    print(f"{x[0]} prestado a {persona[1]}")
                    return
                else:
                    print(f"el libro {x[0]} no esta disponible")
                    return
        print("\nLibro no encontrado")

    def mostrar_prestamos(self):
        print("\nLista de prestamos")
        for p in self.prestamos:
            print(f"Estudiante ID: {p[0]} libro {p[1]}")

    def devolver_libros(self,persona,nombre_libro):
        for x in self.prestamos:
            if x[0] == persona[0] and x[1] == nombre_libro:
                for i in self.lista_libros:
                    if i[0] == nombre_libro:
                        i[1] = True
                        break
                self.prestamos.remove(x)
                print(f"{nombre_libro} devuelto por {persona[1]}")
        print(f"No se encontró un prestamo activo del libro {nombre_libro} para {persona[1]}")