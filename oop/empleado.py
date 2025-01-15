class Empleado:
    def __init__(self, nombre, apellidos, cargo, salario = 1000):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre}, que es {self.cargo}, con apellido {self.apellidos}, y gana {self.getSalario()} €"

listaEmpleados = [
    Empleado("Pepe", "Perez", "CEO" , 1000),
    Empleado("Iñigo", "Martinez", "Defensa", 13000),
    Empleado("Luis", "Galvez", "Gestor de Bases de Datos", 2300),
    Empleado("Jorge", "Herdaldo", "Vigilante", 1200)
]

for empleado in listaEmpleados:
    if empleado.getSalario()>2000 :
        print(empleado)