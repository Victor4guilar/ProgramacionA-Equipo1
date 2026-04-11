# Sistema de Adquisición de Datos de Sensores

## Descripción
Este proyecto consiste en el desarrollo de un sistema en Python para la adquisición, almacenamiento y visualización de datos de sensores (temperatura y LDR).

El sistema puede trabajar en modo simulación, generando datos automáticamente, lo que permite probar el funcionamiento sin necesidad de hardware físico.

---

## Objetivo
Registrar datos de sensores en tiempo real, almacenarlos en archivos y generar una representación gráfica para su análisis.

---

## Funcionamiento
El programa realiza las siguientes tareas:

- Simula lecturas de sensores
- Registra datos con timestamp
- Guarda los datos en un archivo CSV
- Genera estadísticas básicas
- Crea una gráfica de los datos obtenidos

---

## Ejecución

Para ejecutar el programa:

```bash
python src/run_acquisition.py --mode sim
