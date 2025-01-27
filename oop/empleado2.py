class Empleado2:
    
    listaEmpleados = []
    n_empleados = 0
    
    def __init__(self, nombre: str, cargo: str, salario=10000):
        if salario < 0:
            raise ValueError("Error, el salario no puede ser negativo")
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        
        Empleado2.listaEmpleados.append(self)
        Empleado2.n_empleados +=1
    
    def get_salario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre}, con cargo de {self.cargo}, cobra {self.get_salario()} €"
    
    
    
emp1 = Empleado2("Edward", "Programador Web", 21500)
emp2 = Empleado2("Jose", "Piloto de F1", 1200000)

for emp in Empleado2.listaEmpleados:
    print(emp)

print(f"Numero de empleados: {Empleado2.n_empleados}")

    
        