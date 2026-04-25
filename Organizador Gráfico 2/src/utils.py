import logging                                 #Librería para registrar eventos en archivos
from datetime import datetime                  #Permite obtener fecha y hora actual

#CONFIGURAR LOGGER
def configurar_logger(nombre_archivo):         #Función para configurar el sistema de logs
    """Configura el sistema de logs"""
    logging.basicConfig(                       #Configuración básica del logging
        filename=nombre_archivo,               #Nombre del archivo donde se guardarán los logs
        level=logging.INFO,                    #Nivel de registro (INFO guarda mensajes importantes)
        format='%(asctime)s - %(message)s'     #Formato: fecha/hora + mensaje
    )

#GUARDAR MENSAJE EN LOG
def guardar_log(remitente, mensaje):           #Función para guardar mensajes en el log
    """Registra mensajes en el archivo de log"""
    logging.info(f"{remitente}: {mensaje}")    #Guarda quién envía y el mensaje

#FORMATEAR MENSAJE PARA PANTALLA
def formatear_mensaje(remitente, mensaje):     #Función para dar formato visual al mensaje
    """Da formato con hora a los mensajes"""
    hora = datetime.now().strftime("%H:%M:%S") #Obtiene la hora actual en formato HH:MM:SS
    return f"[{hora}] {remitente}: {mensaje}"  #Devuelve mensaje con hora y remitente

#VALIDAR MENSAJE
def mensaje_valido(mensaje):                   #Función para validar mensajes
    """Evita mensajes vacíos"""
    return mensaje.strip() != ""               #Elimina espacios y verifica que no esté vacío

#COMANDO DE SALIDA
def es_comando_salida(mensaje):                #Función para detectar si el usuario quiere salir
    """Detecta si el usuario quiere salir"""
    return mensaje.lower() == "exit"           #Convierte a minúsculas y compara con "exit"