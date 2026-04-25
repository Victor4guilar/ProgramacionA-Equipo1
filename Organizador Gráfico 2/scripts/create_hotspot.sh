#!/bin/bash

echo "Configuracion de red para cliente-servidor"

echo ""
echo "Paso 1: Crear hotspot (red WiFi)"
echo "Nota: cambia 'wlan0' si tu interfaz tiene otro nombre (ej. wlp2s0)"
nmcli dev wifi hotspot ifname wlan0 ssid RedSocket password 12345678

echo ""
echo "Configuracion para el programa Python"

echo ""
echo "IMPORTANTE:"
echo "- Ejecuta este script en la laptop que sera el SERVIDOR"
echo "- Obtiene la direccion IP con el siguiente comando:"

hostname -I

echo ""
echo "Ejemplo esperado: 10.42.0.1 o similar"

echo ""
echo "Configura tu codigo asi:"

echo ""
echo "SERVIDOR:"
echo "HOST = 0.0.0.0"
echo "PORT = 5000"

echo ""
echo "CLIENTE:"
echo "HOST = (IP mostrada arriba)"
echo "PORT = 5000"

echo ""
echo "Prueba de conexion"

echo ""
echo "Desde la laptop cliente ejecuta:"
echo "ping (IP del servidor)"

echo ""
echo "Resultado esperado:"
echo "0%% packet loss"

echo ""
echo "Orden de ejecucion"

echo ""
echo "1. Ejecutar servidor: python3 servidor.py"
echo "2. Ejecutar cliente: python3 cliente.py"

echo ""
echo "Si no conecta:"
echo "- Verificar que ambos dispositivos esten en la misma red"
echo "- Revisar IP correcta"
echo "- Permitir el puerto 5000 en el firewall (si aplica)"

echo ""
echo "Hotspot listo para usar"
