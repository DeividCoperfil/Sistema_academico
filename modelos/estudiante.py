from modelos.persona import Persona
from datos.gestor_csv import GestorCSV

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.registro = []

    def agregar_estudiante(self):
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
        print("\nESTUDIANTES REGISTRADOS:")
        for e in self.registro:
            print(f"ID: {e[0]} | Nombre: {e[1]} | Edad: {e[2]} | Email: {e[4]}")
        encabezados = ["Id", "Nombre", "Edad", "Direccion", "Email", "Fecha_nacimiento"]
        GestorCSV.añadir_datos_csv("estudiantes.csv", encabezados, self.registro)

    def modificar_datos_estudiante(self):
        if not self.registro: #Si no hay nada en la lista de estudiantes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print("")
        print("-"*40)
        print(f"Actualmente tiene: {len(self.registro)} estudiantes") #muestra al cantidad de registros
        print("-"*40)
        print("")

        valor = 0 #variable para indicar el numero del registro
        for i in self.registro:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} Edad: {i[2]} direccion: {i[3]} correo: {i[4]}")

        while True:
            cambio_registro = input("\nPor favor, ingrese el numero del registro que desea modificar: ")

            #Verifica que se ingrese algun dato
            if cambio_registro == "":
                print("\n Debes ingresar una opción.")
                continue

            #Valida que sea un numero entero
            try:
                cambio_registro = int(cambio_registro)-1
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que el numero este entre el rango de registros
            if cambio_registro <= -1 or cambio_registro+1 > len(self.registro):
                print("")
                print("-"*40)
                print(f"Ingrese un número entre 1 y {len(self.registro)}.")
                print("-"*40)
                continue

            print(f"\nVas a modificar los datos del usuario: {self.registro[cambio_registro][1]}")
            
            
            #Solicitud de nuevos datos / verificador de ingreso de datos
            Nuevo_id = input("\nIngresa el nuevo id: ")
            while not Nuevo_id:
                 Nuevo_id = input("\nDebes ingresar un id: ")

            nuevo_nombre = input("\nIngresa el nuevo nombre: ")
            while not nuevo_nombre:
                nuevo_nombre = input("\nDebes ingresar un nombre: ")

            nuevo_telefono = input("\nIngresa el nuevo telefono: ")
            while not nuevo_telefono:
                nuevo_telefono = input("\nDebes ingresar un telefono")

            nuevo_direccion = input("\nIngresa la nueva direccion: ")
            while not nuevo_direccion:
                nuevo_direccion = input("\nDebes ingresar una direccion: ")

            nuevo_correo = input("\nIngresa el nuevo correo: ")
            while not nuevo_correo:
                nuevo_correo = input("\nDebes ingresar un correo: ")
            
            #Cambio de datos
            self.registro[cambio_registro][0]= Nuevo_id
            self.registro[cambio_registro][1]= nuevo_nombre
            self.registro[cambio_registro][2]= nuevo_telefono
            self.registro[cambio_registro][3]= nuevo_direccion
            self.registro[cambio_registro][4]= nuevo_correo

            print("")
            print("-"*40)
            print("Datos actulizados con exito :)")
            print("-"*40)
            break

    #Metodo para eliminar un registro de la lista de estudiantes
    def eliminar_estudiantes(self):
        if not self.registro: #Si no hay nada en la lista de estudiantes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print("")
        print("-"*40)
        print(f"Actualmente tiene: {len(self.registro)} estudiantes") #muestra al cantidad de registros
        print("-"*40)
        print("")

        valor = 0 #variable para indicar el numero del registro
        for i in self.registro:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} edad: {i[2]} direccion: {i[3]} correo: {i[4]}")

        while True:
            eliminador = input("\nPor favor, ingrese el numero del registro que desea eliminar: ")

        #Verifica que se ingrese algun dato
            if eliminador == "":
                print("\n Debes ingresar una opción.")
                continue

            #Valida que sea un numero entero
            try:
                eliminador = int(eliminador)-1
            except ValueError:
                print("")
                print("-"*40)
                print("Ingrese un número válido.")
                print("-"*40)
                continue
            
            #Verifica que el numero este entre el rango de registros
            if eliminador <= -1 or eliminador+1 > len(self.registro):
                print("")
                print("-"*40)
                print(f"Ingrese un número entre 1 y {len(self.registro)}.")
                print("-"*40)
                continue
            
            print(f"\nVas a eliminar los datos del usuario: {self.registro[eliminador][1]}")

            del self.registro[eliminador] #Eliminar lista de datos del estudiante elegido

            print("")
            print("-"*40)
            print("Datos eliminados con exito :)")
            print("-"*40)
            break

    #Metodo para mostrar los estudiantes
    def mostrar_estudiantes(self):
        if not self.registro: #Si no hay nada en la lista de estudiantes, se muestra lo siguiente:
            print("\nNo hay registros de estudiantes aun, debes agregar uno primero")
            return
        
        print(f"\nActualmente tiene: {len(self.registro)} estudiantes") #muestra al cantidad de registros

        #Imprimir los datos de cada estudiante
        valor = 0
        for i in self.registro:
            valor = valor+1
            print(f"Registro: {valor} ID: {i[0]} Nombre: {i[1]} edad: {i[2]} direccion: {i[3]} correo: {i[4]}")

    def obtener_estudiantes(self):
        return self.registro

    def buscar_estudiante(self, id_buscar):
        for estudiante in self.registro:
            if estudiante[0] == id_buscar:
                return estudiante
        return None
