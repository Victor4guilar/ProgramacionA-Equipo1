# python_opt.py
# Versión: 2.0.0
# Autor: Gabriel_14/03/2026
# Descripción: Evolución a reporte tabular con análisis estadístico avanzado.
# MOD: v2.0.0 — Rediseño del programa para generar un reporte estadístico estructurado y soportar múltiples modas.

from collections import Counter

def generar_reporte_frecuencias(datos):
    if not datos:
        return "Error: Lista vacía."

    frecuencias = Counter(datos)
    max_frecuencia = max(frecuencias.values())
    modas = [num for num, count in frecuencias.items() if count == max_frecuencia]
    
    # --- INTERFAZ DE SALIDA MEJORADA ---
    print("\n" + "="*40)
    print(f"{'REPORTE ESTADÍSTICO V2.0.0':^40}")
    print("="*40)
    
    # Tabla de Frecuencias
    print(f"{'VALOR':<15} | {'FRECUENCIA':<15}")
    print("-" * 35)
    for val, freq in sorted(frecuencias.items()):
        # Resaltar la moda con un asterisco
        marca = " (MODA)" if freq == max_frecuencia else ""
        print(f"{val:<15} | {freq:<15}{marca}")
    
    print("-" * 35)
    
    # Resumen de Resultados
    principal_modo = modas[0]
    suma_digitos = sum(int(d) for d in str(abs(principal_modo)))
    
    print(f"Modas detectadas: {modas}")
    print(f"Frecuencia máxima: {max_frecuencia}")
    print(f"Suma dígitos (Moda 1): {suma_digitos}")
    print("="*40 + "\n")

if __name__ == "__main__":
    muestra = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]
    generar_reporte_frecuencias(muestra)