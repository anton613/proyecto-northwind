"""
Configuración centralizada del proyecto Northwind.
Todas las rutas y variables compartidas van aquí.
"""

from pathlib import Path

# ==========================================
# RUTAS DEL PROYECTO
# ==========================================

# Raíz del proyecto (subir desde src/)
PROJECT_ROOT = Path(__file__).parent.parent

# Carpetas de datos
DATA_PATH = PROJECT_ROOT / "data"
RAW_PATH = DATA_PATH / "01_raw"           # Datos extraídos de MySQL
SILVER_PATH = DATA_PATH / "02_silver"     # Datos limpios
GOLD_PATH = DATA_PATH / "03_gold"       # Datos transformados (futuro)

# Crear carpetas si no existen
for path in [RAW_PATH, SILVER_PATH, GOLD_PATH]:
    path.mkdir(parents=True, exist_ok=True)

# ==========================================
# TABLAS DE NORTHWIND
# ==========================================

# Todas las tablas disponibles
TABLAS_RAW = [
    'customers',                    # 29 registros
    'employees',                    # 9 registros
    'employee_privileges',          # 1 registro
    'inventory_transaction_types',  # 4 registros
    'inventory_transactions',       # 102 registros
    'invoices',                     # 35 registros
    'order_details',                # 58 registros
    'order_details_status',         # 6 registros
    'orders',                       # 48 registros
    'orders_status',                # 4 registros
    'orders_tax_status',            # 2 registros
    'privileges',                   # 1 registro
    'products',                     # 45 registros
    'purchase_order_details',       # 55 registros
    'purchase_order_status',        # 4 registros
    'purchase_orders',              # 28 registros
    'sales_reports',                # 5 registros
    'shippers',                     # 3 registros
    'strings',                      # 62 registros
    'suppliers'                     # 10 registros
]

# Tablas principales para análisis (subset importante)
TABLAS_CORE = [
    'customers',
    'orders',
    'order_details',
    'products',
    'employees',
    'suppliers',
    'shippers'
]

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def get_raw_file(tabla: str) -> Path:
    """Retorna la ruta del archivo CSV en 01_raw."""
    return RAW_PATH / f"{tabla}.csv"

def get_silver_file(tabla: str) -> Path:
    """Retorna la ruta del archivo CSV en 02_silver."""
    return SILVER_PATH / f"{tabla}.csv"

def listar_tablas_raw() -> list:
    """Lista todas las tablas disponibles en 01_raw."""
    if not RAW_PATH.exists():
        return []
    return [f.stem for f in RAW_PATH.glob("*.csv")]

def listar_tablas_silver() -> list:
    """Lista todas las tablas disponibles en 02_silver."""
    if not SILVER_PATH.exists():
        return []
    return [f.stem for f in SILVER_PATH.glob("*.csv")]

def verificar_extraccion() -> dict:
    """Verifica qué tablas están extraídas vs las esperadas."""
    extraidas = set(listar_tablas_raw())
    esperadas = set(TABLAS_RAW)
    
    return {
        'extraidas': sorted(extraidas),
        'faltantes': sorted(esperadas - extraidas),
        'total_extraidas': len(extraidas),
        'total_esperadas': len(esperadas)
    }