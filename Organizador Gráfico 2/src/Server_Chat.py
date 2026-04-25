import socket    #Librería para comunicación por red
import threading #Permite ejecutar tareas en paralelo
import logging   #Permite guardar eventos en archivos

HOST = '0.0.0.0' #Escucha en todas las interfaces de red
PORT = 5000      #Puerto donde trabajará el servidor
#Configuración del sistema de logs
logging.basicConfig(
    filename='server_test1.log', #Ruta del archivo de log
    level=logging.INFO,                          #Nivel de registro (INFO)
    format='%(asctime)s - %(message)s'           #Formato del mensaje
)

#FUNCIÓN PARA RECIBIR MENSAJES
def recibir_mensajes(conn):                     #Función que recibe datos del cliente
    while True:                                 #Bucle infinito para escuchar mensajes
        try:
            data = conn.recv(1024)              #Recibe hasta 1024 bytes
            if not data:                        #Si no hay datos
                print("Cliente desconectado.")  #Muestra desconexión
                break                           #Sale del ciclo
            mensaje = data.decode('utf-8')      #Convierte bytes a texto
            print(f"\nCliente: {mensaje}")      #Imprime mensaje recibido
            logging.info(f"Cliente: {mensaje}") #Guarda mensaje en log
        except Exception as e:                                 #Si ocurre un error
            print("Error al recibir mensaje:", e)  #Muestra error
            break                               #Termina el ciclo

#FUNCIÓN PARA ENVIAR MENSAJES
def enviar_mensajes(conn):                        #Función que envía datos al cliente
    while True:                                   #Bucle infinito para enviar mensajes
        try:
            mensaje = input("Tú: ")               #Lee mensaje desde teclado
            if mensaje.lower() == "exit":         #Para salir de la comunicación se escribe exit
                conn.close()                      #Termina la conección
                break                             #Termina el ciclo
            conn.sendall(mensaje.encode('utf-8')) #Envía mensaje codificado
            logging.info(f"Servidor: {mensaje}")  #Guarda mensaje en log

        except Exception as e:                                   #Si ocurre un error
            print("Error al enviar mensaje:", e)     #Muestra error
            break                                 #Termina el ciclo


#FUNCIÓN PRINCIPAL
def iniciar_servidor():                          #Función principal del servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Crea socket TCP
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reutiliza inmediatamente una IP y un puerto
    server.bind((HOST, PORT))                    #Asocia IP y puerto al socket
    server.listen(1)                             #Escucha máximo 1 cliente
    print(f"Servidor escuchando en {HOST}:{PORT}...")  #Muestra estado del servidor
    conn, addr = server.accept()                 #Acepta conexión entrante
    print(f"Conexión establecida con {addr}")    #Muestra dirección del cliente
    logging.info(f"Conexión con {addr}")         #Guarda conexión en log
    puente_recibir = threading.Thread(           #Crea "puente" para recibir mensajes
        target=recibir_mensajes, args=(conn,)
    )
    puente_enviar = threading.Thread(            #Crea "puente" para enviar mensajes
        target=enviar_mensajes, args=(conn,)
    )
    puente_recibir.start()                       #Inicia recepción
    puente_enviar.start()                        #Inicia envío
    puente_recibir.join()                        #Espera a que termine recibir
    puente_enviar.join()                         #Espera a que termine envi
    conn.close()               #Cierra conexión con cliente
    server.close()             #Cierra el servidor
    print("Servidor cerrado.") #Mensaje final

#EJECUCIÓN
if __name__ == "__main__": #Verifica ejecución directa
    iniciar_servidor()     #Llama a la función principal