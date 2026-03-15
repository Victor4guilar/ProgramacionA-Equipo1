# CHANGELOG

Registro de versiones y mejoras del proyecto de optimización de código en Python y C.
Formato de registro:
- Archivo afectado
- Versión anterior → nueva versión
- Resumen de cambios
- Fecha y autor del commit

---

# [2026-03-14]
## python_no_opt.py

### 1.0.0 → 1.0.1
Autor: Gabriel  
Resumen:
- Primera optimización del código.
- Eliminación de estructuras innecesarias en el cálculo de frecuencias.
- Mejora de claridad en la entrada y salida de datos.

### 1.0.1 → 1.1.0
Autor: Axel  
Resumen:
- Implementación de diccionario para almacenar frecuencias.
- Uso de `get()` para simplificar la actualización de valores.
- Reducción de estructuras condicionales y mejora de eficiencia.

### 1.1.0 → 1.2.0
Autor: Jonathan  
Resumen:
- Uso de `collections.Counter` para conteo optimizado de frecuencias.
- Implementación de `most_common()` para determinar el modo.
- Código más compacto y legible.

### 1.2.0 → 2.0.0
Autor: Gabriel  
Resumen:
- Rediseño del programa hacia un **reporte estadístico estructurado**.
- Soporte para **múltiples modas**.
- Implementación de tabla de frecuencias y salida formateada en consola.

---

# [2026-03-13]
## c_no_opt.c

### 1.0.0 → 1.0.1
Autor: Victor  
Resumen:
- Eliminación de líneas redundantes sin funcionalidad.
- Reducción de operaciones innecesarias en el algoritmo.
- Código más corto y claro.

### 1.0.1 → 1.1.0
Autor: Axel  
Resumen:
- Optimización del algoritmo de verificación de números primos.
- Se agrega `break` para detener la búsqueda al encontrar el primer divisor.
- Reducción significativa de iteraciones innecesarias.

### 1.1.0 → 1.2.0
Autor: Jonathan  
Resumen:
- Optimización matemática del algoritmo.
- Verificación de divisores solo hasta `√n`.
- Eliminación de evaluación de números pares.

### 1.2.0 → 2.0.0
Autor: Victor  
Resumen:
- Rediseño completo del programa.
- Generación de **reporte estadístico estructurado**.
- Implementación de tabla de frecuencias y soporte para múltiples modas.
