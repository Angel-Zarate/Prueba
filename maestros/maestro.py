from datetime import datetime

class Maestro:
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    ano_nacimiento: int
    numero_control: str
    
    def __init__(self, nombre: str, apellido: str, rfc: str, sueldo: float,ano_nacimiento:int,numero_control:str):
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.ano_nacimiento = ano_nacimiento
        self.numero_control = numero_control
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"- Número de control: {self.numero_control}\n- Nombre completo: {nombre_completo}\n- RFC: {self.rfc}\n- Sueldo: {self.sueldo}\n- Año de nacimiento: {self.ano_nacimiento}\n"
        return info
