# LEARNED_PYTHON.md

## Sockets y funciones clave

Se utilizó la librería `socket` para implementar comunicación cliente-servidor mediante TCP.

Funciones principales:

* `socket.socket()` → crea el socket
* `bind((host, port))` → asocia IP y puerto al servidor
* `listen(n)` → pone al servidor en modo escucha
* `accept()` → acepta conexiones entrantes
* `connect((host, port))` → conecta el cliente al servidor
* `sendall(data)` → envía datos completos
* `recv(buffer)` → recibe datos (en bytes)

Aprendizaje:
Se comprendió cómo establecer una conexión TCP entre dos dispositivos dentro de una red.


## Manejo de archivos

Se aprendió el uso básico de archivos en Python:

* `open("archivo.txt", "r/w/a")`
* Lectura por bloques:

  ```python
  while True:
      data = file.read(1024)
      if not data:
          break
  ```
* Envío por chunks (fragmentos de datos)

Permite transferir archivos grandes sin consumir demasiada memoria.


## Hashing (SHA256)

Uso de la librería `hashlib`:

```python
import hashlib
hash = hashlib.sha256(data).hexdigest()
```

* Verificar la integridad de datos
* Asegurar que un archivo no ha sido modificado


## Logging

Uso de la librería `logging` para registrar eventos:

```python
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
```


* Registrar mensajes enviados y recibidos
* Guardar historial de comunicación


## Argparse

Permite recibir parámetros desde la terminal:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--host")
parser.add_argument("--port")
parser.add_argument("--file")
args = parser.parse_args()
```

Hace los programas más flexibles sin necesidad de modificar el código.


## Concurrencia básica

### threading

Permite ejecutar múltiples tareas al mismo tiempo:

```python
threading.Thread(target=funcion).start()
```


* Enviar y recibir mensajes simultáneamente


### select

Permite monitorear múltiples sockets sin bloquear el programa.

Cuándo usar:

* Cuando se manejan múltiples conexiones y se quiere evitar el uso excesivo de hilos


### asyncio

Modelo asíncrono basado en eventos.

Cuándo usar:

* Aplicaciones que requieren alta escalabilidad (como servidores o chats con muchos usuarios)


## Utilidades

### pathlib

Manejo moderno de rutas:

```python
from pathlib import Path
Path("archivo.txt")
```

### os

Interacción con el sistema:

```python
os.listdir()
os.remove("archivo.txt")
```

### subprocess

Ejecutar comandos del sistema:

```python
subprocess.run(["ipconfig"])
```

Permite obtener información del sistema, como la dirección IP.


## Buenas prácticas

* Usar mensajes claros en commits (ej. "fix: conexión TCP")
* Enviar metadatos antes de datos (por ejemplo, tamaño del archivo)
* Manejar errores con `try/except`
* Cerrar conexiones correctamente con `close()`
* Validar entradas del usuario
* Mantener el código organizado y documentado
