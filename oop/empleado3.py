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
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.nombre}, con cargo de {self.cargo}, cobra {self.get_salario()} €"
    
    
    
emp1 = Empleado2("Edward", "Programador Web", 21500)
emp2 = Empleado2("Jose", "Piloto de F1", 1200000)

for emp in Empleado2.listaEmpleados:
    print(emp)

print(f"Numero de empleados: {Empleado2.n_empleados}")

num1 = 7
num2 = 7.0
num3 = 7.5

if Empleado2.is_integer(num1):
    print(num1," es entero.")
else:
    print(num1," no es entero.")
    
if Empleado2.is_integer(num2):
    print(num2," es entero.")
else:
    print(num2," no es entero.")

if Empleado2.is_integer(num3):
    print(num3," es entero.")
else:
    print(num3," no es entero.")