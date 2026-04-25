Un **socket** es el punto final de un enlace de comunicación bidireccional entre dos programas que se ejecutan en una red. Es la interfaz que permite que el software se conecte al hardware de red para enviar y recibir datos.

Para tu Notepad, aquí tienes el resumen clave:


**DEFINICIÓN DE SOCKET**

**1. El Concepto Lógico**
Es una abstracción de software que actúa como un "enchufe" digital. Para que dos aplicaciones se comuniquen (por ejemplo, tu navegador y el servidor de una web), ambas deben abrir un socket en sus respectivos extremos.

**2. Los Componentes (La Dirección)**
Un socket queda definido por la combinación de:
* **Dirección IP:** Identifica el dispositivo en la red (el edificio).
* **Puerto:** Identifica la aplicación específica dentro del dispositivo (el departamento).
* **Protocolo:** Define las reglas de comunicación (usualmente TCP para confiabilidad o UDP para velocidad).

**3. Analogía del Sistema Postal**
* **IP:** El código postal y número de calle.
* **Puerto:** El número de buzón específico para una persona.
* **Socket:** El acto de poner la carta en el buzón y recibir una respuesta por el mismo medio.

**4. Tipos de Sockets de Software**
* **Stream Sockets (TCP):** Orientados a la conexión. Garantizan que los datos lleguen completos y en orden (ej. transferencia de archivos).
* **Datagram Sockets (UDP):** Sin conexión. Son más rápidos pero pueden perder datos por el camino (ej. videollamadas).

**5. El Socket de Hardware**
En el contexto físico de una computadora, el socket es el **zócalo de la placa base** donde se instala físicamente el procesador (CPU). Es la matriz de contactos que conecta los pines del chip con el resto de la placa.


TCP vs UDP: características, ventajas y cuándo usar cada uno.

1. TCP (Transmission Control Protocol)
Prioridad: Fiabilidad y Orden.
Es como una conversación telefónica: ambos confirman que se escuchan antes de hablar.

* Características principales:
- Orientado a conexión: Realiza un "apretón de manos" antes de enviar datos.
- Confirmación (ACK): El receptor avisa que recibió cada paquete.
- Reenvío: Si algo se pierde, lo vuelve a mandar automáticamente.
- Orden garantizado: Si el paquete 2 llega antes que el 1, TCP los acomoda antes de entregarlos.

2. UDP (User Datagram Protocol)
Prioridad: Velocidad y Fluidez.
Es como un megáfono: lanzas el mensaje y no te detienes a preguntar si todos escucharon.

* Características principales:
- Sin conexión: Empieza a enviar datos sin previo aviso.
- Sin confirmación: No espera a que el receptor diga "lo recibí".
- Sin reenvío: Si un paquete se pierde, se ignora y se sigue con el siguiente.
- Latencia mínima: Al no tener que revisar errores, es extremadamente rápido.
Aquí tienes el resumen estructurado para tu Notepad, sin tablas y con la información clave sobre cómo se organizan las conexiones en red.


DIRECCIONES IP Y PUERTOS: 

1. LA DIRECCIÓN IP 
La dirección IP identifica de forma única a un dispositivo en una red. Es la dirección global que permite que los datos lleguen al equipo correcto.

2. EL PUERTO 
El puerto es un número (del 0 al 65535) que identifica una aplicación o servicio específico dentro de ese dispositivo. Permite que el sistema operativo sepa si los datos que llegan son para el navegador, para un juego o para el correo.

CLASIFICACIÓN DE LOS PUERTOS (0 al 65535)

A. PUERTOS BIEN CONOCIDOS (0 al 1023)
Son puertos reservados para servicios universales y estandarizados. Normalmente, solo el sistema operativo o servicios de administrador pueden usarlos.

Ejemplos esenciales:
- Puerto 20/21: FTP (Transferencia de archivos).
- Puerto 22: SSH (Acceso remoto seguro).
- Puerto 25: SMTP (Envío de correos).
- Puerto 53: DNS (Resolución de nombres de dominio).
- Puerto 80: HTTP (Navegación web sin cifrar).
- Puerto 443: HTTPS (Navegación web segura/cifrada).

B. PUERTOS REGISTRADOS (1024 al 49151)
Son puertos que empresas o aplicaciones específicas registran para sus servicios. No son tan universales como los anteriores, pero se usan para software común.

Ejemplos conocidos:
- Puerto 1433: Microsoft SQL Server.
- Puerto 3306: MySQL (Bases de datos).
- Puerto 3389: Escritorio remoto de Windows (RDP).
- Puerto 5432: PostgreSQL.

C. PUERTOS DINÁMICOS O PRIVADOS (49152 al 65535)
También llamados puertos efímeros. No pertenecen a ningún servicio.


NAT y problemas de conectividad entre redes distintas.

1. ¿QUÉ ES NAT?
NAT es una técnica que utiliza tu router para que todos los dispositivos de tu casa (celulares, laptops, consolas) puedan salir a Internet usando una única Dirección IP Pública.

* IP Privada: La que tiene tu dispositivo dentro de tu casa (ej. 192.168.1.15). Nadie fuera de tu red puede verla.
* IP Pública: La que te asigna tu proveedor de Internet (ISP). Es la "cara" de tu red hacia el mundo.

NAT actúa como un recepcionista: cuando pides algo a una web, el router anota quién lo pidió, cambia tu IP privada por la pública y envía la petición. Cuando llega la respuesta, NAT la redirige al dispositivo correcto.


2. EL PROBLEMA DE LA CONECTIVIDAD (LA BARRERA)
El problema principal es que NAT funciona muy bien desde ADENTRO hacia AFUERA, pero bloquea las conexiones que vienen desde AFUERA hacia ADENTRO.

A. El "Muro" de NAT:
Si un servidor externo o un amigo intenta iniciar una conexión contigo directamente, el router recibe los datos pero no sabe a qué dispositivo interno entregárselos (porque nadie los pidió primero). Simplemente los descarta por seguridad.

B. NAT Doble (Double NAT):
Ocurre cuando tienes dos routers conectados en cadena (el del ISP y uno propio). Los datos tienen que pasar por dos recepcionistas distintos, lo que suele romper servicios de juegos, cámaras de seguridad y VPNs.

C. CGNAT (Carrier-Grade NAT):
Es cuando tu proveedor de Internet no te da una IP pública real, sino que te mete en una red gigante con otros miles de clientes. Aquí no tienes control sobre los puertos y es casi imposible ser "host" de un servidor o partida.


3. SOLUCIONES A PROBLEMAS DE CONECTIVIDAD

* Port Forwarding (Reenvío de Puertos):
Le dices al router manualmente: "Todo lo que llegue por el puerto 8080, envíalo directamente a la IP de mi servidor". Esto abre un agujero controlado en el muro de NAT.

* UPnP (Universal Plug and Play):
Permite que las aplicaciones (como juegos o Torrent) le pidan al router que abra los puertos necesarios automáticamente. Es cómodo, pero menos seguro.

* DMZ (Demilitarized Zone):
Abres TODOS los puertos para una sola IP interna. Es efectivo para consolas de videojuegos, pero peligroso para una computadora porque queda totalmente expuesta a ataques.

* NAT Traversal / Hole Punching:
Técnica usada en videollamadas y juegos P2P donde ambos dispositivos envían un paquete al mismo tiempo para "engañar" a sus respectivos NATs y dejar un túnel abierto entre ellos.



FIREWALLS Y PERMISOS DE PUERTO

1. ¿QUÉ ES UN FIREWALL?
Es un sistema de seguridad que actúa como un filtro o "aduana" entre tu red (o computadora) y el resto del mundo. Su función es inspeccionar cada paquete de datos que intenta entrar o salir y decidir, bajo un conjunto de reglas, si le permite el paso o lo bloquea.

Existen dos tipos principales según su ubicación:
- Firewall de Red: Un dispositivo físico o software en el router que protege a todos los equipos de la casa/empresa.
- Firewall de Host: Software que corre directamente en tu sistema operativo (ej. Windows Defender Firewall).


2. LAS REGLAS DE FILTRADO (EL CORAZÓN DEL FIREWALL)
El firewall no adivina; sigue reglas estrictas basadas en:
- Dirección IP (Origen y Destino).
- Puerto (¿A qué aplicación va esto?).
- Protocolo (TCP o UDP).
- Dirección del tráfico (Entrante o Saliente).

3. PERMISOS DE PUERTO: "OPEN" VS "CLOSED"

A. Puertos de Entrada (Inbound):
Por seguridad, la mayoría de los firewalls bloquean por defecto todas las conexiones que vienen de fuera. 
- Si quieres correr un servidor web, debes "abrir" el puerto 80/443.
- Si no abres el puerto manualmente, el firewall descarta el paquete y la conexión falla, aunque el programa esté encendido.

B. Puertos de Salida (Outbound):
Normalmente están abiertos para que puedas navegar libremente. Sin embargo, en entornos de alta seguridad, se cierran para evitar que un virus o malware "llame a casa" para enviar tu información a un servidor externo.


4. ESTADOS DE UN PUERTO SEGÚN EL FIREWALL
Cuando se escanea un puerto, el firewall puede responder de tres formas:
- Open (Abierto): El firewall permite el paso y hay una aplicación escuchando.
- Closed (Cerrado): El firewall permite el paso, pero no hay ninguna aplicación en ese puerto.
- Filtered (Filtrado): El firewall ni siquiera responde. Ignora el paquete (Drop) para que el atacante no sepa si el equipo está encendido o no.


5. PROBLEMAS COMUNES DE CONECTIVIDAD
Incluso con el NAT configurado correctamente, un firewall mal ajustado puede causar:
- Error de "Connection Refused": El firewall bloquea el puerto de destino.
- Latencia o lag: El firewall está inspeccionando demasiado profundo cada paquete (Deep Packet Inspection), retrasando el flujo.
- Falsos positivos: Bloquea aplicaciones legítimas (como juegos o herramientas de ingeniería) porque usan puertos no estándar que el firewall considera sospechosos.

Wi‑Fi Direct vs hotspot vs misma red: diferencias y limitaciones.

FORMAS DE CONEXIÓN INALÁMBRICA: DIFERENCIAS Y LÍMITES

1. WI-FI DIRECT (CONEXIÓN PUNTO A PUNTO)
Es una tecnología que permite que dos dispositivos se conecten directamente entre sí mediante Wi-Fi, sin necesidad de un router o punto de acceso intermedio.

* Cómo funciona: Uno de los dispositivos actúa como "punto de acceso suave" y el otro se conecta a él.
* Ventajas:
  - No requiere internet ni router.
  - Velocidad muy alta (mucho más rápido que Bluetooth).
  - Ideal para transferencia de archivos pesados.
* Limitaciones:
  - Generalmente solo conecta dos dispositivos a la vez.
  - El dispositivo "emisor" suele perder su propia conexión a internet Wi-Fi mientras lo usa.
* Ejemplos: AirDrop (usa una mezcla de esto), enviar archivos entre celulares Android, conectar impresoras inalámbricas.


2. HOTSPOT / ANCLAJE DE RED (PUNTO DE ACCESO MÓVIL)
Es cuando un dispositivo (normalmente un celular) comparte su conexión de datos móviles creando una red Wi-Fi propia a la que otros pueden unirse.

* Cómo funciona: El celular funciona como un router portátil. Convierte la señal 4G/5G en una señal Wi-Fi.
* Ventajas:
  - Da acceso a Internet a dispositivos que no tienen (como una laptop en la calle).
  - Permite conectar varios dispositivos simultáneamente (típicamente hasta 8 o 10).
* Limitaciones:
  - Consume mucha batería del dispositivo que comparte.
  - Depende de la cobertura de datos móviles.
  - Suele tener límites de datos impuestos por la operadora telefónica.
* Ejemplo: "Compartir datos" desde tu smartphone a tu computadora.


3. MISMA RED / RED LOCAL (LAN/WLAN)
Es cuando todos los dispositivos están conectados a un mismo nodo central, que suele ser el router de la casa o la oficina.

* Cómo funciona: El router gestiona el tráfico. Los dispositivos no se hablan directamente "aire con aire", sino que sus mensajes pasan por el router.
* Ventajas:
  - Estabilidad y mayor alcance (gracias a las antenas del router).
  - Todos los dispositivos pueden verse entre sí y tener internet al mismo tiempo.
  - Permite servicios permanentes (servidores multimedia, domótica).
* Limitaciones:
  - Si el router se apaga o falla, se pierde la comunicación entre todos.
  - La velocidad depende de la saturación del canal del router.
* Ejemplo: Tu PC y tu Smart TV conectados al Wi-Fi de tu casa para transmitir pantalla.


RESUMEN DE DIFERENCIAS CLAVE:

- Wi-Fi Direct: Es un "túnel" privado entre dos equipos. Sin intermediarios.
- Hotspot: Es convertir un equipo en "el jefe" de la red para dar internet a otros.
- Misma Red: Es usar una infraestructura común (el router) para que todos convivan.

LIMITACIÓN TÉCNICA COMÚN:
En los tres casos, la interferencia en la banda (2.4GHz o 5GHz) afecta la velocidad. Además, los muros y la distancia degradan la señal, siendo Wi-Fi Direct el que suele tener el rango más corto de los tres.

Seguridad básica: TLS/SSL, recomendaciones para pruebas.

Aquí tienes el resumen de seguridad esencial para comunicaciones en red, diseñado para tu Notepad.


SEGURIDAD BÁSICA: TLS/SSL Y PRUEBAS

1. ¿QUÉ SON SSL Y TLS?
Son protocolos criptográficos que proporcionan comunicaciones seguras por red. Aunque solemos decir "SSL", hoy en día es un término antiguo; lo que usamos realmente es **TLS** (Transport Layer Security).

* SSL (Secure Sockets Layer): Versión original, hoy considerada insegura y obsoleta.
* TLS: El sucesor moderno. Las versiones actuales seguras son **TLS 1.2** y, preferiblemente, **TLS 1.3**.

2. ¿QUÉ HACEN REALMENTE?
- Cifrado: Los datos viajan codificados. Si alguien intercepta el paquete, solo verá basura digital.
- Autenticación: Garantiza que el servidor es quien dice ser (mediante Certificados Digitales).
- Integridad: Evita que los datos sean modificados durante el camino sin que el receptor se de cuenta.


3. RECOMENDACIONES PARA PRUEBAS (ENTORNOS DE DESARROLLO)

Cuando programas o pruebas sockets seguros, aquí tienes las mejores prácticas:

A. Usa Certificados Autofirmados (Self-Signed):
Para pruebas locales no necesitas comprar un certificado. Puedes generar uno propio, aunque el navegador o el sistema te darán una advertencia de "Sitio no seguro". Es normal en desarrollo.

B. No desactives la verificación en producción:
En pruebas es común usar banderas como `verify=False` o `rejectUnauthorized: 0` para evitar errores de certificados. **NUNCA** dejes esto en el código final, ya que anula toda la seguridad.

C. Prueba los Puertos Correctos:
- Si pruebas HTTPS, usa el puerto 443.
- Si pruebas SMTPS (correo), usa el puerto 465 o 587.
- Evita usar puertos estándar de texto plano (80, 21, 23) para tráfico sensible.

D. Herramientas de Diagnóstico:
- **OpenSSL:** La herramienta estándar por línea de comandos para verificar certificados y conexiones.
  Comando útil: `openssl s_client -connect google.com:443`
- **Wireshark:** Para verificar que, efectivamente, no puedes leer el contenido de los paquetes (deben aparecer como "Application Data" cifrada).


4. VULNERABILIDADES A EVITAR

- Cipher Suites Débiles: No permitas algoritmos de cifrado antiguos (como RC4 o DES).
- Versiones obsoletas: Configura tu servidor para rechazar conexiones SSLv3, TLS 1.0 y TLS 1.1.
- Exposición de llaves: Nunca subas tus llaves privadas (.key) a repositorios como GitHub.
