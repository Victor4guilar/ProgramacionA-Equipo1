
@echo off

echo CONFIGURACION DE RED PARA CLIENTE-SERVIDOR

echo.
echo Paso 1: Creando hotspot (red WiFi)
netsh wlan set hostednetwork mode=allow ssid=RedSocket key=12345678

echo.
echo Paso 2: Iniciando hotspot
netsh wlan start hostednetwork

echo.
echo CONFIGURACION PARA EL PROGRAMA PYTHON

echo.
echo IMPORTANTE:
echo - Ejecuta este archivo en la laptop que sera el SERVIDOR
echo - Luego ejecuta "ipconfig" para obtener la direccion IPv4
echo - Ejemplo esperado: 192.168.43.44

echo.
echo CONFIGURA TU CODIGO ASI:

echo.
echo SERVIDOR:
echo HOST = 0.0.0.0
echo PORT = 5000

echo.
echo CLIENTE:
echo HOST = 192.168.43.44
echo PORT = 5000

echo.
echo PRUEBA DE CONEXION

echo.
echo Desde la laptop cliente ejecuta:
echo ping 192.168.43.44

echo.
echo Resultado esperado:
echo Datos enviados: 4
echo Datos recibidos: 4
echo Perdidos: 0

echo.
echo ORDEN DE EJECUCION

echo.
echo 1. Ejecutar servidor (python servidor.py)
echo 2. Ejecutar cliente (python cliente.py)

echo.
echo Si no conecta:
echo - Desactivar Firewall de Windows
echo - Verificar misma red WiFi
echo - Revisar IP correcta

echo.
echo Hotspot listo para usar
pause

