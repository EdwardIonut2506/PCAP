fecha = input("Ingrese una fecha en foramto dd/mm/aaaa: ")

mesesito = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}

dia = int(fecha.split("/")[0])
mes = int(fecha.split("/")[1])
año = int(fecha.split("/")[2])

if (mes in mesesito):
    print("La fecha es:",dia," de ", mesesito[mes], " del año ",año)
else:
    print("Error")