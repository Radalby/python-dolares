int_Edad = 0
float_Estatura = 0.0
str_Inicial = ""
str_Apellido = ""

#Introducir Datos
int_Edad = int (input("Ingrese su edad: "))
float_Estatura = float (input("Ingrese su estatura: "))
str_Inicial = input("Ingrese su primer nombre: ")
str_Apellido = input("Ingrese su Apellido: ")
print("")


# Salida de datos:
print("Sus datos son:")
print("Edad: %d" %(int_Edad))
print("Estatura: %1.2f" %(float_Estatura))
print("Inicial: %s" %(str_Inicial))
print("Apellido: %s" %(str_Apellido))