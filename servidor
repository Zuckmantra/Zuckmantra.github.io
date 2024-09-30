import socket
import sqlite3

# Configuración de la base de datos
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Crear una tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Función para insertar un nuevo usuario
def register_user(username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return "Registro exitoso."
    except sqlite3.IntegrityError:
        return "El usuario ya existe."

# Función para verificar el inicio de sesión
def login_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    return user is not None

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Servidor escuchando en el puerto 12345...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Conexión establecida con {address}")

    # Recibir solicitud del cliente
    data = client_socket.recv(1024).decode()
    command, *params = data.split(',')

    if command == 'REGISTER':
        username, password = params
        response = register_user(username, password)
        client_socket.sendall(response.encode())
    elif command == 'LOGIN':      
        username, password = params
        if login_user(username, password):
            response = "Inicio de sesión exitoso."
        else:
            response = "Usuario o contraseña incorrectos."
        client_socket.sendall(response.encode())
    
    client_socket.close()
