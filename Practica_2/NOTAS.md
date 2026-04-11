# Notas del Proyecto: Registro de Sensores

## Objetivo
Comprender y documentar los conceptos de programación utilizados en la adquisición de datos de sensores (temperatura y LDR), así como su procesamiento, almacenamiento y visualización.

---

## 1. Diccionarios (dict)
Los diccionarios permiten almacenar datos en pares clave-valor.

Ejemplo en el proyecto:
Se utiliza un diccionario llamado `config` para guardar la configuración del experimento:
- duración del experimento
- intervalo de muestreo
- modo de ejecución (simulación o serial)

Esto facilita modificar parámetros sin cambiar todo el código.

---

## 2. Listas (list)
Las listas almacenan múltiples elementos de forma ordenada.

Ejemplo:
La lista `readings` guarda todas las lecturas del sensor.

Cada elemento contiene:
- timestamp
- temperatura
- LDR

---

## 3. Tuplas (tuple)
Las tuplas son estructuras inmutables (no se pueden modificar).

Ejemplo:
Cada lectura se guarda como una tupla:

(timestamp, temperatura, ldr)

Esto asegura que los datos no cambien accidentalmente.

---

## 4. Ciclos (while / for)

### while
Se utiliza para ejecutar la adquisición durante un tiempo determinado.

Ejemplo:
El programa toma lecturas durante 60 segundos.

### for
Se usa para recorrer listas y procesar datos.

Ejemplo:
Calcular estadísticas o generar archivos.

---

## 5. Condicionales (if / else)
Permiten tomar decisiones dentro del programa.

Ejemplo:
- Determinar si se usa modo simulación o serial
- Detectar errores en lectura

---

## 6. Manejo de errores (try / except)
Permite evitar que el programa se detenga por errores inesperados.

Ejemplo:
Si falla la lectura del sensor:
- se registra el error
- el programa continúa ejecutándose

Esto hace el sistema más robusto.

---

## 7. Archivos CSV
Formato de almacenamiento de datos en texto plano separados por comas.

Ejemplo generado:
timestamp,temp_raw,ldr_raw

Se utiliza para guardar las lecturas y analizarlas posteriormente.

---

## 8. JSON
Formato utilizado para guardar datos estructurados.

Ejemplo en el proyecto:
Se usa para guardar:
- configuración del experimento
- estadísticas de los sensores

Archivo generado:
metadata.json

---

## 9. Matplotlib
Librería utilizada para generar gráficas.

En este proyecto se usa para:
- visualizar temperatura
- visualizar valores del LDR

Permite analizar el comportamiento de los sensores en el tiempo.

---

## 10. Timestamp (ISO 8601)
Formato estándar de fecha y hora.

Ejemplo:
2026-03-24T09:00:00Z

Se utiliza para registrar el momento exacto de cada lectura.

---

## 11. Escritura atómica de archivos
Técnica que evita corrupción de archivos.

Proceso:
1. Se escribe en un archivo temporal
2. Se reemplaza el archivo original

Esto garantiza que el CSV no se dañe si el programa se interrumpe.

---

## 12. Simulación de sensores
El programa puede generar datos sin hardware real.

Se utiliza:
- ruido aleatorio
- funciones matemáticas

Esto permite probar el sistema antes de usar Arduino o Wokwi.

---

## Conclusión
El proyecto integra múltiples conceptos de programación para resolver un problema real de ingeniería: la adquisición y análisis de datos de sensores. Se aplican estructuras de datos, control de flujo, manejo de errores y visualización de datos de forma práctica.