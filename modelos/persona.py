class Persona:
    def __init__(self, id="", nombre="", edad="", direccion="", email="", fecha_nacimiento=""):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento

    def solicitar_datos_persona(self):
        campos = ["id", "nombre", "edad", "direccion", "email", "fecha_nacimiento"]
        datos = []
        for campo in campos:
            valor = input(f"Ingrese {campo}: ").strip()
            while not valor:
                valor = input(f"El {campo} no puede estar vacío, ingrese nuevamente: ").strip()
            datos.append(valor)
        return datos
