#Programa: Calculadora de suma
#Autor: Equipo 1 SD
#Versión: 1.2.0
#Descripción: Se agrega validación de datos con manejo de errores.

try:
    N1 = float(input("Ingresa el dato 1: "))
    N2 = float(input("Ingresa el dato 2: "))
    
    suma = N1 + N2
    
    print("La suma es:", suma)

except ValueError:
    print("Error: Debes ingresar solo números.")