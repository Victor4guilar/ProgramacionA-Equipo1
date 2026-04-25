Método elegido 
CONEXIÓN POR RED LOCAL (LAN/WI-FI)

JUSTIFICACIÓN

La elección de trabajar sobre una red local existente se basa en la búsqueda de un equilibrio entre facilidad de implementación, estabilidad de señal y capacidad de escalabilidad. A diferencia de otras conexiones punto a punto, esta infraestructura permite un entorno de pruebas profesional y realista.

1. VENTAJAS (JUSTIFICACIÓN)

* Infraestructura Existente:
No requiere hardware adicional ni configuraciones complejas de hardware. Aprovecha el router como nodo central de comunicaciones (Switch/Access Point).

* Soporte Multidispositivo:
A diferencia de Wi-Fi Direct, que suele ser 1 a 1, una red LAN permite que múltiples clientes (varias laptops, tablets o sensores) se conecten simultáneamente al mismo servidor.

* Persistencia de Servicios:
Permite que los dispositivos mantengan su conexión a Internet de forma paralela. Esto es vital si la aplicación necesita consultar APIs externas, descargar librerías o sincronizar datos en la nube mientras se comunica localmente.

* Mayor Alcance y Estabilidad:
Los routers cuentan con una gestión de señales y potencia superior a la de un smartphone o una tarjeta de red en modo Direct, lo que reduce la pérdida de paquetes (especialmente crítico si se usa UDP).


2. LIMITACIONES Y DESAFÍOS

* Dependencia del Nodo Central:
Si el router falla o se reinicia, toda la comunicación entre los dispositivos se corta inmediatamente. El sistema no es autónomo.

* Configuración de Seguridad (Firewalls):
Es la limitación más común. Los sistemas operativos suelen ver las redes Wi-Fi como "públicas" y bloquean por defecto cualquier intento de conexión entrante, lo que requiere configuración manual de reglas de puerto.

* Variabilidad de la Dirección IP (DHCP):
En una red estándar, el router asigna IPs dinámicas. Si el servidor se apaga y vuelve a encender, su IP podría cambiar, obligando a reconfigurar todos los clientes.
- Solución: Asignar una IP estática o usar nombres de host (mDNS).

* Saturación del Canal:
Al compartir la red con otros usos (streaming, descargas de otros usuarios), el ancho de banda disponible puede fluctuar, introduciendo latencia o "jitter" en las pruebas de sockets.

COMANDOS USADOS PARA CREAR HOTSPOT O RED AD-HOC


WINDOWS (netsh)

1. Configurar la red:
   netsh wlan set hostednetwork mode=allow ssid=MiRed key=12345678

Descripción:

* mode=allow: habilita el hotspot
* ssid=MiRed: nombre de la red
* key=12345678: contraseña (mínimo 8 caracteres)

2. Iniciar el hotspot:
   netsh wlan start hostednetwork

3. Detener el hotspot:
   netsh wlan stop hostednetwork

4. Ver estado de la red:
   netsh wlan show hostednetwork


LINUX (nmcli)

1. Crear hotspot:
   nmcli dev wifi hotspot ifname wlan0 ssid MiRed password 12345678

Descripción:

* ifname wlan0: interfaz de red (puede variar, por ejemplo wlp2s0)
* ssid: nombre de la red
* password: contraseña

2. Ver conexiones activas:
   nmcli connection show

3. Desactivar hotspot:
   nmcli connection down Hotspot


RELACION CON EL PROGRAMA

* El equipo que ejecuta el servidor crea el hotspot.
* El cliente se conecta a esa red.
* El cliente debe usar la IP del servidor (por ejemplo 192.168.43.44).
* El puerto debe coincidir en ambos programas (en este caso 5000).

PROBLEMAS ENCONTRADOS Y CÓMO SE RESOLVIERON

Durante la implementación de la comunicación cliente-servidor mediante sockets, se presentaron diversos problemas relacionados principalmente con la conectividad entre los equipos.


1. Problema: Falta de conexión entre las laptops

Al ejecutar el cliente y el servidor, inicialmente no se lograba establecer la conexión TCP. El cliente no podía comunicarse con el servidor, aunque ambos programas estaban correctamente escritos.

Solución:
Se identificó que el Firewall de Windows estaba bloqueando la comunicación. Para resolverlo, se desactivó temporalmente el firewall siguiendo esta ruta:

Panel de control → Sistema y Seguridad → Firewall de Windows Defender → Activar o desactivar Firewall de Windows Defender → Desactivar (tanto en red privada como pública)

Esto permitió que el tráfico por el puerto 5000 no fuera bloqueado.


2. Problema: Dirección IP incorrecta

El cliente no lograba conectarse porque no se estaba utilizando la dirección IP correcta del servidor.

Solución:
En la laptop que ejecutaba el servidor, se utilizó el comando:

ipconfig

Se identificó la dirección IPv4 asignada (por ejemplo: 192.168.43.44) y esta se colocó en el código del cliente en la variable HOST.


3. Problema: Duda sobre la conectividad de red

No se tenía certeza de si ambas laptops estaban realmente conectadas dentro de la misma red.

Solución:
Se utilizó el comando:

ping [dirección IPv4]

desde la laptop cliente hacia la del servidor. Al obtener el resultado:

Datos enviados: 4
Datos recibidos: 4
Perdidos: 0

se confirmó que existía comunicación entre ambos dispositivos.


4. Problema: Orden de ejecución

En algunos intentos, la conexión fallaba debido a que se ejecutaba primero el cliente.

Solución:
Se estableció el orden correcto de ejecución:

1. Ejecutar primero el servidor
2. Ejecutar después el cliente

De esta forma, el servidor ya estaba en espera de conexiones cuando el cliente intentaba conectarse.

