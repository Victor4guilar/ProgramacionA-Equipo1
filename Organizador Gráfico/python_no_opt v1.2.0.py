# python_opt.py
# Versión: 1.2.0
# Autor: Jonathan
# Fecha: 14/03/2026
# Descripción: Optimización del cálculo de frecuencias y del modo utilizando
# la clase Counter de collections para mejorar rendimiento y legibilidad.
# Entrada esperada: Lista de números enteros.
# Salida esperada: Frecuencias de cada número, valor modal y suma de los dígitos del modo.

from collections import Counter

# Lista de entrada de ejemplo
numeros = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]

# BLOQUE 1: Construcción del diccionario de frecuencias
# MOD v1.2.0 — Se usa Counter, estructura optimizada para conteo
frecuencias = Counter(numeros)

# BLOQUE 2: Determinar el valor modal
# MOD v1.2.0 — most_common(1) devuelve el elemento más frecuente y su cuenta
modo, max_cuenta = frecuencias.most_common(1)[0]

# BLOQUE 3: Cálculo de la suma de los dígitos del valor modal
# MOD v1.2.0 — Se simplifica la suma de dígitos usando comprensión de lista
suma_digitos = sum(int(d) for d in str(abs(modo)))

# BLOQUE 4: Mostrar resultados
print("Frecuencias:", list(frecuencias.items()))
print(f"Modo: {modo} con cuenta: {max_cuenta}")
print("Suma de dígitos del modo:", suma_digitos)