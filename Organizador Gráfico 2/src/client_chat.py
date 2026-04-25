import socket
import threading
import logging   #Permite guardar eventos en archivos

# Configuración: Aquí debes poner la IP del equipo donde corre el servidor
# Si están en la misma red, usa la IP local (ej. '192.168.1.XX')
HOST = '192.168.43.44'  # '127.0.0.1' si es en la misma PC, o la IP local del servidor
PORT = 5000         # Debe coincidir exactamente con el del servidor
#Configuración del sistema de logs
logging.basicConfig(
    filename='client_test1.log', #Ruta del archivo de log
    level=logging.INFO,                          #Nivel de registro (INFO)
    format='%(asctime)s - %(message)s'           #Formato del mensaje
)

def recibir_mensajes(cliente):
    while True:
        try:
            data = cliente.recv(1024)
            if not data:
                print("\nServidor desconectado.")
                break
            print(f"\nServidor: {data.decode('utf-8')}")
        except Exception as e:
            print("Error al recibir:", e)
            break

def enviar_mensajes(cliente):
    while True:
        try:
            mensaje = input("Tú: ")

            if mensaje.lower() == "exit":
                cliente.close()
                break

            cliente.sendall(mensaje.encode('utf-8'))

        except Exception as e:
            print("Error al enviar:", e)
            break

# Función principal del Cliente
def iniciar_cliente():
    # 1. Crear el socket (TCP)
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. Conectar al servidor
    print(f"Intentando conectar a {HOST}:{PORT}...")

    try:
        cliente.connect((HOST, PORT))
    except Exception as e:
        print("Error al conectar:", e)
        return

    print("Conectado al servidor.")
    # 3. Crear hilos (igual que en el servidor para enviar/recibir simultáneamente)
    threading.Thread(
        target=recibir_mensajes,
        args=(cliente,),
        daemon=True
    ).start()

    enviar_mensajes(cliente)

if __name__ == "__main__":
    iniciar_cliente()

