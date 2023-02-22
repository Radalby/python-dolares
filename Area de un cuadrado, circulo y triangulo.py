
#Variables

#Cuadrado
float_Cuadrado = 0.0
float_Lado= 0.0

#Triangulo
float_Triangulo=0.0
float_Base = 0.0
float_Altura = 0.0

#Circulo
float_Circulo=0.0
float_Radio= 0.0
const_PI = 3.14

#INICIALIZAR CODIGO

#Area de un Cuadrado
float_Lado = float(input("Introducir el valor del lado: "))
float_Cuadrado = float_Lado**2
print(" El Area de un cuadrado es: %1.2f" %(float_Cuadrado))

#Area de un Triangulo
float_Altura = float(input("Introduce el valor de la Altura: "))
float_Base = float(input("Introduce el valor de la base: "))
float_Triangulo = (float_Base*float_Altura)/2
print(" El area de un triangulo es: %1.2f" %(float_Triangulo))

#Area de un Circulo
float_Radio= float(input("Introduce el valor del Radio: "))
float_Circulo = const_PI*(float_Radio**2)
print(" El area de un circulo es: %1.2f" %(float_Circulo))
