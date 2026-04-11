ANALYSIS.md

# Análisis de Resultados: Sistema de Captura de Datos
Materia: Ingeniería en Instrumentación Electrónica
Equipo: Victor Aguilar Ortíz, Gabriel Beltrán Amezcua, Jonathan Sánchez Pérez, Axel de Jesús Ronzón Pérez
Fecha: 10 de Abril de 2026
Versión. 1. 2. 0 

1. Introducción
El presente documento examina el avance técnico del sistema diseñado para el registro de sensores de temperatura y LDR. Este proyecto ha progresado de un registrador simple a una herramienta de monitoreo avanzada que incorpora filtrado digital de señales y detección automática de anomalías térmicas. 

2. Justificación Técnica de Estructuras de Datos
Se escogieron estructuras fundamentales de Python para asegurar una gestión eficiente de los datos provenientes de los instrumentos:

* Tuplas (`tuple`): Se emplean para agrupar lecturas `(timestamp, temp, ldr)`. Su característica inmutable garantiza la consistencia de los datos originales frente a modificaciones no deseadas. 
* Listas (`list`): Funcionan como un buffer dinámico del sistema, permitiendo el almacenamiento secuencial de las muestras a través del método `. append()`. 
* Diccionarios (`dict`): Utilizados en los objetos `config` y `stats` para estructurar metadatos. Su diseño favorece una exportación ordenada a JSON, facilitando la compatibilidad con otros sistemas analíticos. 

3. Evolución y Mejoras del Software

# 3. 1 Historial de Versiones
* v1. 0. 1: Se corrigió la simulación mediante la inclusión del módulo `math` para generar señales senoidales más realistas. 
* v1. 1. 0: Se llevó a cabo la Mejora A (Media Móvil) para disminuir el ruido en la señal de temperatura sin perder la tendencia original. 
* v1. 2. 0: Se incorporó la Supervisión Automatizada y la rectificación de metadatos en el archivo (`environment. txt`). 

# 3. 2 Análisis de la v1. 2. 0: Supervisión y Alerta
La actualización más reciente transforma el registrador en un sistema de monitoreo inteligente:
* Umbral Crítico: Se ha definido un límite de 25. 0°C. 
* Lógica de Decisión: El software analiza el 100% de las muestras al concluir la recolección. En caso de detectar valores superiores, emite una notificación de "¡ALERTA! ".  Esta funcionalidad es esencial en instrumentación para proteger los activos y prevenir fallos por sobrecalentamiento. 

4. Robustez e Integridad de Datos
El sistema asegura la continuidad y protección de la información mediante:
1. Manejo de Errores (`try / except`): Alta tolerancia a fallos en el puerto serie; en tales casos, el sistema asigna `NaN` y continúa funcionando, evitando bloqueos. 
2. Escritura Atómica: La utilización de archivos temporales evita la corrupción del historial `raw_readings. csv` en situaciones de cortes de energía o cierres inesperados. 

5. Interpretación de Resultados
Gracias al filtro de media móvil y a la nueva lógica de alertas, el sistema ofrece:
- Una señal de temperatura suavizada que permite un mejor control. 
- Un diagnóstico instantáneo del estado del sensor (Estable vs Alerta). 
- Un registro exhaustivo del entorno de ejecución (versiones de Python y bibliotecas). 

6. Conclusión
La versión 1. 2. 0 representa la culminación de un proceso ingenieril integral: desde la recolección de datos en crudo hasta su procesamiento digital y la toma de decisiones automatizadas. El sistema se ha convertido en una herramienta operativa para el monitoreo de procesos térmicos.