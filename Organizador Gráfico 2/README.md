# Sistema de Mensajería P2P basado en TCP
## 1. Introducción y Objetivo del Proyecto

Este documento describe la creación y puesta en marcha de una estructura de comunicación punto a punto (P2P) diseñada en el lenguaje de programación Python. El objetivo principal del sistema es posibilitar que dos terminales autónomos configuren un canal de comunicación seguro, sincrónico y confiable a través de una red inalámbrica (WLAN). 

El proyecto va más allá de la simple creación de una interfaz de chat; se adentra en el campo de la Ingeniería de Redes, examinando cómo los datos se comportan a través de las distintas capas del modelo OSI, superando importantes barreras técnicas como la segmentación de red, cortafuegos y configuraciones de traducción de direcciones de red (NAT) dinámicas. En esta etapa final, el sistema es compatible con diversas plataformas, incorporando herramientas de automatización de red tanto para Linux (Bash) como para Windows (Batch). 

# 2. Marco Teórico Ampliado (Fundamentos de Redes)
## 2.1. Estructura y Ciclo Vital de un Socket TCP

Un socket es la representación de software que actúa como punto final de un enlace de comunicación bidireccional. Para este proyecto, se ha implementado el uso de sockets de flujo (stream sockets), que funcionan mediante una combinación de una dirección IPv4 y un puerto de red determinado. 

Dirección IP: Funciona como el identificador único del host dentro de la topología de la red. 

Puerto (5000): Se eligió el puerto 5000 como canal lógico. Al ser un puerto de rango registrado, se minimizan espacios de choque con servicios críticos del sistema operativo. 

## 2.2. Protocolo de Transporte: Ventajas de TCP sobre UDP

Para una aplicación de mensajería, la integridad y el orden son aspectos esenciales. Por ello, se optó por TCP (Protocolo de Control de Transmisión):

Mecanismo de Handshake: TCP asegura la disponibilidad en ambos extremos mediante un intercambio inicial de paquetes (SYN, SYN-ACK, ACK). 

Secuenciación y Reensamblaje: Permite que el receptor reconstruya el mensaje original de manera precisa, incluso si los paquetes llegan en un orden diferente. 

Control de Flujo y Errores: TCP identifica la congestión y solicita automáticamente la retransmisión de paquetes dañados. 

## 2.3. Automatización de Infraestructura en Múltiples Plataformas   

El sistema debió abordar dificultades de visibilidad entre los dispositivos a través de scripts de configuración automática:

Entornos Linux: Empleo de create_hotspot. sh con la herramienta nmcli para generar puntos de acceso rápidos. 

Entornos Windows: Uso de create_hotspot_win. bat mediante el comando netsh wlan. Este script automatiza la creación de la red hospedada y ajustes de seguridad WPA2. 

Diagnóstico de Conectividad: Se estandarizó el uso de ping para confirmar que la tasa de pérdida de paquetes sea del 0% previo a la ejecución del software. 

# 3. Arquitectura del Software y Modularización

## 3.1. Implementación de Multithreading (Hilos de Ejecución)

Para resolver el bloqueo de funciones (donde el programa se detiene al esperar una entrada), se aplicó una arquitectura de Multithreading:

Hilo Principal: Se encarga de la interfaz de usuario y la lógica de envío. 

Hilo Secundario: Dedicado exclusivamente a escuchar el socket (recv) en paralelo. 
Esto permite una comunicación Full-Duplex, donde ambos usuarios pueden interactuar de manera simultánea. 

## 3.2. Modularización con utils. py
Se ha desarrollado una capa de servicios complementarios para homogeneizar el tratamiento de datos:

Manejo de Registros: Mediante la utilización de la biblioteca logging, se documentan los eventos con marcas de tiempo precisas para fines de auditoría. 

Verificación de Datos: Se han implementado filtros para prevenir el envío de mensajes vacíos y se ha incorporado una lógica para el formato visual de las conversaciones (HH:MM:SS). 

Protocolo de Comandos: Se lleva a cabo la identificación de órdenes específicas, como exit, para iniciar un procedimiento de cierre de sockets de manera coordinada. 

## 3.3. Ambiente de Ejecución

El proyecto está fundamentado únicamente en la Biblioteca Estándar de Python, garantizando así total portabilidad y compatibilidad con versiones de Python iguales a 3. 14. 3 sin requerir la instalación de dependencias externas. 

# 4. Descripción de la Lógica de Conexión

## 4.1. Lógica del Servidor (Host)

El servidor actúa como una entidad pasiva que asigna el puerto 5000 (bind), se coloca en modo de escucha (listen) y, al detectar al cliente, establece un socket de comunicación específico (accept). 

## 4.2. Lógica del Cliente (Iniciador)

El cliente opera como una entidad activa que demanda la conexión utilizando la IP proporcionada por el Hotspot (usualmente 10. 42. 0. 1 en Linux o 192. 168. 137. 1 / 192. 168. 43. 44 en Windows). Una vez que la conexión se ha establecido, se activa su hilo de recepción. 

# 5. Bitácora de Pruebas y Resultados (Evidencias)

## 5.1. Análisis de Registros de Interacción

Las pruebas evidenciaron una estabilidad del 100%. La implementación de scripts. bat y. sh disminuyó considerablemente los errores humanos durante la configuración de la IP y la red alojada. 

[SISTEMA] Red alojada iniciada correctamente en Windows. 

[CONEXIÓN] Conexión TCP establecida sin pérdida de paquetes. 

## 5.2. Conclusiones

Adaptabilidad: El proyecto ha sido optimizado para poder llevarse a cabo en los dos sistemas operativos más comunes mediante herramientas nativas de shell. 

Sólidez: La distinción entre la lógica de red y las funciones de utilidad favorece el mantenimiento y la escalabilidad futura (transferencia de archivos).
