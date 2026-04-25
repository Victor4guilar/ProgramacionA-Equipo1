# Sistema P2P de Mensajería mediante TCP

# 1. Introducción y Objetivo del Proyecto

El presente documento describe el diseño y la ejecución de una red de comunicación punto a punto (P2P) creada en el lenguaje de programación Python.  La intención principal de este sistema es facilitar que dos dispositivos independientes establezcan un canal de comunicación seguro, eficiente y confiable a través de una red inalámbrica (WLAN). 

Este proyecto va más allá de la mera programación de una interfaz de chat; se adentra en la Ingeniería de Redes, estudiando el              comportamiento de la información a través de las diferentes capas del modelo OSI (especialmente en las capas de red y transporte),          superando barreras técnicas significativas como la segmentación de redes, los cortafuegos y las configuraciones de traducción de            direcciones de red (NAT) dinámicas. 

# 2. Marco Teórico Desarrollado (Fundamentación de Redes)

2.1. Estructura y Ciclo de Vida de un Socket TCP

Un socket es la representación en software que actúa como el extremo de un vínculo de comunicación bidireccional. Para el desarrollo de este proyecto, se implementaron sockets de flujo (*stream sockets*), que funcionan mediante una dirección IPv4 combinada con un puerto de red determinado. 

* Dirección IP: Cumple la función de identificador único del equipo dentro de la estructura de la red. Durante las evaluaciones, se destacó la relevancia de las IP privadas otorgadas por DHCP en entornos locales. 
* Puerto (5000): El puerto 5000 fue elegido como el canal lógico de comunicación. Al corresponder a un número de puerto registrado (fuera del rango de puertos bien conocidos de 0 a 1023), se previenen conflictos con servicios esenciales del sistema operativo, como servidores web o protocolos para la transferencia de archivos. 

2.2. Protocolo de Transporte: Ventajas de TCP sobre UDP

Para una aplicación destinada a mensajería y transferencia de datos, la integridad y el orden son indispensables. Por esta razón, se optó por TCP (Transmission Control Protocol) en lugar de UDP, debido a sus mecanismos de control inherentes:

1. Proceso de Handshake (Conexión de Tres Vías): TCP asegura la disponibilidad en ambos extremos mediante un intercambio inicial de paquetes (SYN, SYN-ACK, ACK). Esto garantiza que no se envíen datos a un host que no esté preparado para recibirlos. 
2. Secuenciación y Reensamblaje: En redes inalámbricas, los paquetes pueden seguir rutas diferentes y llegar en un orden alterado. La implementación de TCP en nuestra aplicación asigna un número a cada segmento, permitiendo que el receptor reconstruya el mensaje original con precisión. 
3. Control de Flujo y Detección de Errores: TCP utiliza una "ventana deslizante" que identifica la congestión en la red Wi-Fi. Si un paquete llega dañado debido a interferencias electromagnéticas, el protocolo demanda automáticamente su reenvío sin necesidad de la intervención del usuario. 

2.3. Obstáculos de Comunicación en Entornos Reales

En la etapa de implementación, el sistema se enfrentó a dos principales desafíos arquitectónicos:
* NAT (Traducción de Direcciones de Red): Dado que las computadoras portátiles funcionan a través de un enrutador que oculta las direcciones IP reales, el sistema fue creado para funcionar en el contexto de una LAN (Red de Área Local).  Este diseño permite que las direcciones privadas (clase C, tipo 192. 168. x. x) se puedan visualizar directamente, evitando así la complicación de configuraciones de *Port Forwarding* en redes externas. 
* Normas de Seguridad y Cortafuegos: Las versiones más recientes de los sistemas operativos por defecto impiden todas las conexiones entrantes para proteger la seguridad del sistema. La solución técnica consistió en la configuración de reglas de excepción en el cortafuegos del sistema, lo que permite el acceso al tráfico entrante específicamente en el puerto 5000, asegurando así el paso de los segmentos TCP hacia el proceso de Python. 

# 3. Arquitectura del Software y Concurrencia

3.1. Implementación de Hilos de Ejecución

El principal reto al programar sockets es el bloqueo de funciones. En una aplicación secuencial, la función que permite la lectura de teclado (`input`) interrumpiría completamente la capacidad del programa para recibir mensajes de la red. 

Para superar este desafío, se adoptó una arquitectura de Multithreading:
* Hilo Principal (Main Thread): Encargado de gestionar la interfaz de usuario y la lógica para enviar datos. Se mantiene a la espera de que el usuario escriba un mensaje. 
* Hilo Secundario (Background Thread): Se ejecuta de manera paralela y está dedicado exclusivamente a la escucha del socket mediante la función `recv`. 

Esta distribución de tareas permite una comunicación Full-Duplex, donde ambos usuarios pueden transmitir y recibir información simultáneamente sin interrupciones. 

3.2. Administración de Registros y Auditoría del Sistema

Se incorporó el módulo `logging` de Python para registrar cada evento ocurrido durante la sesión. Esta práctica es crucial en la ingeniería de software para:
* Trazabilidad: Mantener un registro cronológico preciso de los mensajes enviados y recibidos. 
* Depuración: Permitir la identificación de las causas subyacentes de desconexiones inesperadas o fallas en el protocolo mediante el registro de excepciones. 
* Validación de Datos: Asegurarse de que la decodificación de caracteres (UTF-8) se ha realizado correctamente en ambos extremos. 

#4. Descripción de la Lógica de Conexión

4.1. Lógica del Servidor (Host)

El servidor actúa como una entidad pasiva. Su ciclo de operación incluye:
1. Vinculación (Bind): Reservar el puerto 5000 en el sistema. 
2. Escucha (Listen): Permanecer en un estado de espera para las solicitudes de conexión. 
3. Aceptación (Accept): Al identificar al cliente, crea un nuevo socket que se dedicará exclusivamente a esa conversación, liberando el puerto original para futuras interacciones. 

4.2. Lógica del Cliente (Iniciador)

El cliente es la entidad activa. Necesita conocer previamente la dirección IPv4 asignada al servidor en la red inalámbrica. Al comenzar, el cliente intenta "tocar la puerta" del servidor. Una vez que se completa satisfactoriamente el *handshake* de TCP, el cliente inicia su hilo de recepción y se conecta al túnel de datos.

# 5. Registro de Pruebas y Resultados (Evidencias)

5.1. Examen de Registros de Interacción

Luego de realizar pruebas de integración en una red Wi-Fi local, los archivos de registro indicaron una estabilidad del 100% en la entrega de paquetes. Los registros validan que el sistema maneja adecuadamente los caracteres especiales y preserva la consistencia temporal de la comunicación. 

Extracto de Registro de Auditoría:
* `[CONEXIÓN] Conexión establecida con éxito al host remoto. `
* `[TRANSMISIÓN] Mensaje enviado: Activación de verificación de canal TCP. `
* `[RECEPCIÓN] Mensaje recibido: Confirmación de recepción en el cliente. `

5.2. Conclusiones y Mejoras Futuras

* Estabilidad: La implementación de TCP garantizó que no se produjeran pérdidas de mensajes ni que estos llegaran incompletos, incluso con fluctuaciones en la señal inalámbrica. 
* Configuración del Entorno: Se concluyó que la configuración del firewall es tan esencial como el propio código para alcanzar el éxito en la comunicación P2P. 
* Escalabilidad: La estructura basada en hilos representa el primer avance hacia un servidor de chat para múltiples clientes, donde un único servidor puede manejar decenas de conexiones simultáneas mediante la generación de hilos dinámicos para cada nuevo cliente.
