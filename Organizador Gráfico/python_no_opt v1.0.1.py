# python_no_opt.py
# Versión: 1.0.1
# Gabriel_10/03/2026, Primera Optimización, Entrada Lista numerica/Salida Estadísticas modales esperada_opt.py
# MOD: v1.1.0 — Se eliminarion las lineas de codigos inecesarias 

numeros = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]

# Contar las frecuencias de forma limpia
frecuencias_dict = {}
for num in numeros:
    if num in frecuencias_dict:
        frecuencias_dict[num] += 1
    else:
        frecuencias_dict[num] = 1

# Se convierte el diccionario a la lista de tuplas que pedía el código original
frecuencias = list(frecuencias_dict.items())

# Encontrar el valor que más se repite ósea el modo
modo = None
max_cuenta = -1

for valor, cuenta in frecuencias:
    if cuenta > max_cuenta:
        max_cuenta = cuenta
        modo = valor

# Se calcula la suma de los dígitos del modo
# abs() lo hace positivo, str() lo separa en caracteres, int() los vuelve a sumar
x_str = str(abs(modo))
suma_digitos = sum(int(d) for d in x_str)

# Resultados
print("Frecuencias:", frecuencias)
print("Modo:", modo, "con cuenta:", max_cuenta)
print("Suma de dígitos del modo:", suma_digitos)