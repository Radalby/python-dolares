#Variable
dolares = 0.0
bolivar = 0.0

#variables 2
venta_Bolivares = 0.0
venta_Dolares = 0.0

#variable 3
regresar_Bolivares = 0.0
regresar_Dolares = 0.0

#variable 4
cambio_Bolivares = 0.0



#Programa
dolares = float (input("¿Cuantos dolares tiene?: "))
bolivar = float (input("¿A que precio?: "))

bc=dolares*bolivar
print("Tiene %f" %(bc) +" bolivares")


venta_Bolivares = float (input("Precio de la venta: "))
venta_Dolares = venta_Bolivares/bolivar


regresar_Bolivares = (dolares*bolivar)-venta_Bolivares
regresar_Dolares = dolares-venta_Dolares

print("Tienes que regresar %f" %(regresar_Bolivares) +" Bolivares")
print("Tienes que regresar %f" %(regresar_Dolares) +" Dolares")

cambio_Bolivares = float (input("Cuanto cambio quiere dar en bolivares (valor en dolar): "))

dolares_Recortado = regresar_Dolares-cambio_Bolivares
bolivar_Recortado = cambio_Bolivares*bolivar

print("Tiene que dar: %f" %(dolares_Recortado) +" Dolares")
print("Tiene que dar: %f" %(bolivar_Recortado) +" Bolivares")

#por jijija