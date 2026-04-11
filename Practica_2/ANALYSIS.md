ANALYSIS.md

# Análisis de Resultados: Sistema de Captura de Datos
Materia: Ingeniería en Instrumentación Electrónica
Equipo: Victor Aguilar Ortiz, Gabriel Beltrán Amezcua, Jonathan Sánchez Pérez, Axel de Jesús Ronzón Perez,
Fecha: 10 de Abril de 2026

---

1. Introducción
El presente documento expone el análisis técnico del sistema de registro para sensores de temperatura y fotoceldas. Este proyecto ha progresado desde una etapa básica hasta desarrollar un sistema sólido que incluye filtrado digital de señales, garantizando adherencia a los estándares de integridad de datos y gestión de errores utilizando Python. 

2. Justificación Técnica de Estructuras de Datos
Para satisfacer las necesidades de la asignatura, se han implementado diversas estructuras, cada una destinada a un propósito particular dentro del flujo de instrumentación:

* Tuplas (`tuple`): Cada lectura se almacena en el formato `(timestamp, temp, ldr)`. Su característica de inmutabilidad asegura que los datos originados por el ADC permanezcan intactos durante la transmisión de datos. 
* Listas (`list`): La lista `readings` actúa como un búfer de memoria dinámico. Facilita un almacenamiento ordenado y cronológico de las muestras a través del método `. append()`. 
* Diccionarios (`dict`): Se aplicaron para los archivos `config` y `stats`. Su diseño de pares clave-valor simplifica la exportación a formato JSON, asegurando que los metadatos del experimento sean fácilmente interpretables tanto por humanos como por sistemas automáticos. 

3. Control de Flujo y Robustez
La fiabilidad del sistema se asienta sobre tres fundamentos de programación:

1. Ciclos (`while` y `for`): El ciclo `while` determina la duración precisa del experimento (60 segundos), mientras que los ciclos `for` permiten iterar a través de las listas de datos para aplicar filtros y calcular estadísticas. 
2. Manejo de Errores (`try / except`): Esencial para la robustez del sistema. En caso de desconexión del puerto serial, el programa continúa su funcionamiento; registra un error y asigna un valor `NaN`, asegurando la continuidad del registro. 
3. Escritura Atómica: Se utilizó un método de almacenamiento donde primero se crea un archivo temporal que posteriormente se renombra. Esto previene la corrupción del archivo CSV si el script se interrumpe inesperadamente. 

4. Evolución y Mejoras del Software

# 4. 1 De v1. 0. 0 a v1. 0. 1: Corrección de Simulación
Se detectó y corrigió un fallo significativo en el que se utilizaba `random. sin()`. La solución mediante el módulo `math` garantizó que la señal del LDR simulara adecuadamente los ciclos de luz ambiental, validando la lógica de visualización. 

# 4. 2 De v1. 0. 1 a v1. 1. 0: Implementación de la Mejora A
En la versión final (v1. 1. 0), se añadió un Filtro de Media Móvil (`moving_average`) con una ventana de $n=5$. 

* Propósito: Disminuir el ruido de alta frecuencia presente en la señal de temperatura. 
* Resultado: Como se observa en `plot. png`, la línea de "Temp filtrada" atenúa las variaciones de ruido gaussiano, proporcionando una lectura más estable sin perder la tendencia térmica real. 

5. Interpretación de Archivos Generados

| Archivo | Formato | Contenido Técnico |
| :--- | :--- | :--- |
| `raw_readings. csv` | Texto Plano (CSV) | Datos en bruto y filtrados con marca de tiempo ISO 8601. |
| `metadata. json` | JSON | Configuración del sistema y estadísticas (Media, Desviación Estándar). |
| `grafico. png` | Imagen (PNG) | Comparación visual entre la señal sin tratar y la señal elaborada. |

6. Cierre
El trabajo une de manera exitosa principios complejos de programación en el ámbito de la electrónica. La evolución hacia la versión 1. 1. 0 evidencia que el programa no solo recopila información, sino que también la elabora para optimizar la calidad de los datos, una habilidad esencial para cualquier profesional en instrumentación.