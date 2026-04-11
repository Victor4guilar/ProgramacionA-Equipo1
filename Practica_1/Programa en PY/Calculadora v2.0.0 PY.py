#Programa: Calculadora de suma
#Autor: Equipo 1 SD
#Versión: 2.0.0
#Descripción: Calcula: suma, resta, multiplicación y división

print("Bienvenido, selecciona que operación deseas realizar:")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")

operacion = int(input("Operación:"))

if operacion==1:
    try: 
        N1 = float(input("Ingresa el dato 1: "))
        N2 = float(input("Ingresa el dato 2: "))
        
        suma = N1 + N2
        
        print("La suma es:", suma)

    except ValueError:
        print("Error: Debes ingresar solo números.")

elif operacion==2:
    try:
        N1 = float(input("Ingresa el dato 1: "))
        N2 = float(input("Ingresa el dato 2: "))
        
        resta = N1 - N2
        
        print("La resta es:", resta)

    except ValueError:
        print("Error: Debes ingresar solo números.")

elif operacion==3:
    try:
        N1 = float(input("Ingresa el dato 1: "))
        N2 = float(input("Ingresa el dato 2: "))
       
        multi = N1 * N2
    
        print("La multiplicación es:", multi)

    except ValueError:
        print("Error: Debes ingresar solo números.")
        
elif operacion==4:
    try:
        N1 = float(input("Ingresa el dato 1: "))
        N2 = float(input("Ingresa el dato 2: "))
        
        div = N1 / N2
    
        print("La división es:", div)

    except ValueError:
        print("Error: Debes ingresar solo números.")

else:
    print("Opción no válida")
    
    
    
    
    
    
    