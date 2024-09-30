import socket

# Función para enviar comandos al servidor
def send_request(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', 12345))
            client_socket.sendall(command.encode())
            response = client_socket.recv(1024).decode()
            return response
    except ConnectionRefusedError:
        return "Error: No se pudo conectar al servidor."
    except Exception as e:
        return f"Error: {e}"

# Función para registrarse
def register_user():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    response = send_request(f"REGISTER,{username},{password}")
    print(f"Respuesta del servidor: {response}")

# Función para iniciar sesión
def login_user():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    response = send_request(f"LOGIN,{username},{password}")
    print(f"Respuesta del servidor: {response}")

# Menú para el cliente
def menu():
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        choice = input("Elija una opción: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
