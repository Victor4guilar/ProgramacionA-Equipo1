# CHANGELOG

## [v0.1.0] - 22-04-2026
### Axel de Jesús Ronzón Pérez - IAtevoy

* chore: creación de la estructura inicial del repositorio
* chore: creación de carpetas principales (/src, /docs, /images, /results, /scripts)
* chore: organización de subcarpetas (images/tests, results/logs, results/received)
* docs: creación de archivos base (README.md, THEORY.md, DECISION.md, LEARNED_PYTHON.md)
* chore: creación de requirements.txt
* chore: configuración inicial del archivo `.gitignore`
* feat: creación del archivo `server_chat.py` en /src
* feat: implementación inicial del servidor TCP para chat usando sockets
* feat: configuración básica de logging en el servidor

---

## [v0.2.0] - 24-04-2026
### Víctor Aguilar Ortiz - Victor4guilar
* feat: implementación del cliente TCP (`client_chat.py`) para conexión con el servidor
* feat: generación de logs del cliente (`client_test1.log`)
* test: creación y organización de archivos de prueba en `/results/logs`
* test: carga de evidencias visuales en `/images/tests` (capturas de conexión y funcionamiento)
* docs: actualización del archivo `requirements.txt` con dependencias del proyecto

---

### Axel de Jesús Ronzón Pérez - IAtevoy
* fix: corrección del archivo `.gitignore` para permitir su inclusión en el repositorio
* feat: creación del archivo `utils.py` para futuras funciones auxiliares
* refactor: ajustes generales en la estructura del repositorio para mejorar organización

---

### Jonathan Sánchez Pérez - Perez-png2
* docs: elaboración de la documentación técnica en `/docs`
    * `THEORY.md` (conceptos de redes y sockets)
    * `DECISION.md` (justificación del método de conexión)
    * `LEARNED_PYTHON.md` (resumen de conceptos aprendidos en Python)

---

### Gabriel Beltrán Amezcua - Th3PapaY0ch1S08
* docs: creación del archivo `README.md` con la descripción general del proyecto
* feat: incorporación de scripts de automatización en `/scripts`
    * `create_hotspot.sh`
    * `create_hotspot_win.bat`


---

Notas (recordatorio de los significados):
- feat - Nueva funcionalidad
- fix - Corrección de error
- docs - Documentación
- test - Pruebas
- refactor - Reorganización de código
- chore - Tareas generales (configuración, carpetas, etc.)
