import sqlite3
from datetime import datetime

class DataBase:
    db_name = "Register_user.db"

    def __init__(self):
        try:
            conexion = sqlite3.connect(self.db_name)
            sqlintruction = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                usuario TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                fecha_registro TEXT NOT NULL,
                foto_perfil TEXT NOT NULL
            )
            """
            conexion.execute(sqlintruction)
            conexion.commit()
            conexion.close()
        except Exception as e:
            print(f"Error al inicializar la base de datos: {e}")

    def insert_user(self, nombre, apellido, email, usuario, password, foto):
        try:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO users(nombre, apellido, email, usuario, password, fecha_registro, foto_perfil) VALUES (?, ?, ?, ?, ?, ?, ?)"
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute(query, (nombre, apellido, email, usuario, password, fecha, foto))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.IntegrityError:
            print("Error: El usuario o email ya existe.")
            return False
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            return False

    def get_users(self):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, apellido, email, usuario, fecha_registro, foto_perfil FROM users")
            usuarios = cursor.fetchall()
            conexion.close()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    def user_exists(self, usuario):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario FROM users WHERE usuario = ?", (usuario,))
            result = cursor.fetchone()
            conexion.close()
            return result is not None
        except Exception as e:
            print(f"Error al verificar usuario: {e}")
            return False

    def validate_user(self, usuario, password):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario FROM users WHERE usuario = ? AND password = ?", (usuario, password))
            result = cursor.fetchone()
            conexion.close()
            return result is not None
        except Exception as e:
            print(f"Error al validar usuario: {e}")
            return False

    def get_photo(self,usuario):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT foto_perfil FROM users WHERE usuario = ? ",(usuario,))
            foto_perfil = cursor.fetchone()
            conexion.close()
            return foto_perfil
        except Exception as e:
            print(f"Error al obtener foto: {e}")
            return []

    def obtain_user(self):
        # Obtener todos los usuarios
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT nombre FROM users")  # Asegúrate de que la tabla y columnas sean correctas
            usuarios = cursor.fetchall()
            conn.close()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    # Dentro de tu clase DataBase
    def get_user_credentials(self, usuario):
        try:
            conexion = sqlite3.connect(self.db_name)
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario, password, foto_perfil FROM users WHERE usuario = ?", (usuario,))
            result = cursor.fetchone()
            conexion.close()
            if result:
                return result  # Devuelve (usuario, password, foto)
            return None  # Si no se encuentra el usuario
        except Exception as e:
            print(f"Error al recuperar las credenciales: {e}")
            return None
