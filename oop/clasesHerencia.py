class Reptil:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        return f"Soy un reptil llamado {self.nombre}."

class Serpiente(Reptil):
    def __init__(self, nombre, venenosa=False):
        super().__init__(nombre)
        self.venenosa = venenosa

    def describir(self):
        tipo = "venenosa" if self.venenosa else "no venenosa"
        return f"Soy una serpiente {tipo} llamada {self.nombre}."

class Culebra(Serpiente):
    def __init__(self, nombre):
        super().__init__(nombre)

    def describir(self):
        return f"Soy una culebra llamada {self.nombre}, y no soy venenosa."
    

reptil1 = Reptil("Lagarto")
reptil2 = Serpiente("Mamba Negra")
reptil3 = Culebra("Culebra Iberica")

print(f"{type(reptil1).__name__}\t{type(reptil2).__name__} {type(reptil3).__name__}")

for cls1 in[Reptil, Serpiente, Culebra]:
    for cls2 in[Reptil, Serpiente, Culebra]:
        print(issubclass(cls1, cls2), end="\t")
    print()