import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from pathlib import Path
from contextlib import contextmanager

# Cargar .env desde la raíz
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

def get_db_config():
    """Retorna configuración de la base de datos."""
    return {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'port': int(os.getenv('DB_PORT', 3306)),
        'auth_plugin': 'mysql_native_password'
    }

@contextmanager
def conexion_mysql():
    """
    Context manager para manejar conexión MySQL automáticamente.
    Uso: with conexion_mysql() as conn:
    """
    config = get_db_config()
    
    # Verificar configuración
    if None in [config['user'], config['password'], config['host'], config['database']]:
        raise ValueError("❌ Faltan variables en el archivo .env")
    
    conn = None
    try:
        conn = mysql.connector.connect(**config)
        print(f"✅ Conectado a MySQL ({config['database']}@{config['host']})")
        yield conn
        
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        raise
        
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("🔒 Conexión cerrada automáticamente")

def extraer_tabla(conn, tabla):
    """
    Extrae datos de una tabla. Requiere conexión activa.
    Retorna: (datos, nombres_columnas)
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabla}")
        
        datos = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]
        
        print(f"📊 {len(datos)} registros de '{tabla}'")
        return datos, columnas
        
    except Error as e:
        print(f"❌ Error en tabla '{tabla}': {e}")
        return [], []
    finally:
        cursor.close()