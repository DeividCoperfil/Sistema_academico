import csv
import os
from utils.constantes import RUTA_BASE_CSV

class GestorCSV:
    @staticmethod
    def guardar_datos_csv(nombre_archivo, encabezados, datos, ruta_guardado=RUTA_BASE_CSV):
        ruta_completa_archivo = os.path.join(ruta_guardado, nombre_archivo)
        if not os.path.exists(ruta_guardado):
            try:
                os.makedirs(ruta_guardado, exist_ok=True)
                print(f" Directorio creado: '{ruta_guardado}'")
            except Exception as e:
                print(f" Error al crear el directorio '{ruta_guardado}': {e}")
                return
        try:
            with open(ruta_completa_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
                escritor = csv.writer(archivo_csv)
                escritor.writerow(encabezados)
                escritor.writerows(datos)
            print(f"\n Datos exportados a: '{ruta_completa_archivo}'")
            return True
        except Exception as e:
            print(f"\n Ocurrió un error al escribir el archivo: {e}")
            return False

    @staticmethod
    def añadir_datos_csv(nombre_archivo, encabezados, datos, ruta_guardado=RUTA_BASE_CSV):
        ruta_completa_archivo = os.path.join(ruta_guardado, nombre_archivo)
        if not os.path.exists(ruta_guardado):
            try:
                os.makedirs(ruta_guardado, exist_ok=True)
                print(f" Directorio creado: '{ruta_guardado}'")
            except Exception as e:
                print(f" Error al crear el directorio '{ruta_guardado}': {e}")
                return False
        archivo_existe = os.path.exists(ruta_completa_archivo)
        try:
            with open(ruta_completa_archivo, mode='a', newline='', encoding='utf-8') as archivo_csv:
                escritor = csv.writer(archivo_csv)
                if not archivo_existe:
                    escritor.writerow(encabezados)
                escritor.writerows(datos)
            print(f"\n Datos añadidos a: '{ruta_completa_archivo}'")
            return True
        except Exception as e:
            print(f"\n Ocurrió un error al escribir el archivo: {e}")
            return False

    @staticmethod
    def leer_csv(nombre_archivo, ruta_guardado=RUTA_BASE_CSV):
        ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
        if not os.path.exists(ruta_completa):
            print(f"El archivo {nombre_archivo} no existe.")
            return []
        with open(ruta_completa, newline='', encoding='utf-8') as f:
            lector = csv.reader(f)
            next(lector, None)
            return list(lector)
