# CHANGELOG

## 1.0.0 – 2026-04-08 – Profesor - Dominguez Chavez Jose Alfonso
### Cambios
- Versión inicial del proyecto.
- Implementación de adquisición de datos en modo simulación y serial.
- Generación de archivo CSV con lecturas.
- Creación de archivo `metadata.json` con estadísticas.
- Generación de gráfica (`plot.png`) de temperatura y LDR.
- Implementación de manejo de errores básico.
- Escritura atómica para evitar corrupción de archivos.

---

## 1.0.1 – 2026-04-09 – Profesor - Dominguez Chavez Jose Alfonso
### Cambios
- Corrección de error en la simulación:
  - Se reemplazó `random.sin()` por `math.sin()`.
- Se importó correctamente el módulo `math`.
- Se actualizó la versión del código a 1.0.1.
- Se corrigió un bug que impedía la ejecución correcta del programa.

---

## 1.1.0 – 2026-04-10 – Jonathan Sánchez Pérez - Perez-png2  
### Cambios
- Se implementó un filtro de media móvil para la señal de temperatura.
- Se agregó una nueva columna en el CSV: `temp_filtered`.
- Se actualizó la gráfica para mostrar:
  - Temperatura original.
  - Temperatura filtrada.
- Mejora en el análisis de datos al reducir el ruido en la señal.

---

