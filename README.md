# Proyecto ETL - Base de Datos Northwind

## 📋 Descripción del Proyecto

Este proyecto implementa un proceso completo de **ETL (Extract, Transform, Load)** utilizando la base de datos **Northwind**, una base de datos de ejemplo que modela las operaciones de una empresa comercial. El objetivo principal es transformar un esquema transaccional **OLTP (Online Transaction Processing)** en un esquema analítico **OLAP (Online Analytical Processing)**, optimizado para consultas y análisis de datos.

El proyecto sigue una **arquitectura medallón** (Bronze, Silver, Gold) que garantiza la calidad y trazabilidad de los datos en cada etapa del proceso:

- **🥉 Bronze (Raw)**: Extracción de datos en su estado original
- **🥈 Silver (Clean)**: Limpieza y transformación de tipos de datos, manejo de nulos y duplicados
- **🥇 Gold (Analytics)**: Transformación final del esquema OLTP a OLAP para análisis

## 🗂️ Estructura del Proyecto

```
proyecto-northwind/
├── notebooks/
│   ├── 01_bronze_raw_extract.ipynb    # Extracción de datos crudos
│   ├── 02_silver_clean.ipynb          # Limpieza y transformación
│   └── 03_gold_transform.ipynb        # Conversión OLTP → OLAP
├── BaseDatos_Northwind/               # Base de datos Northwind original
├── data/                              # Datos procesados
├── src/                               # Código fuente auxiliar
├── img/                               # Imágenes y diagramas
├── .env                               # Variables de entorno
├── pyproject.toml                     # Configuración del proyecto
└── uv.lock                            # Lock file de dependencias
```

## 📊 Esquemas de Base de Datos

### Esquema OLTP (Transaccional)

El esquema original de Northwind está diseñado para operaciones transaccionales, con múltiples tablas normalizadas:

![Estructura OLTP](img/Estructura%20de%20OLTP.PNG)

### Esquema OLAP (Analítico)

El esquema transformado está optimizado para análisis, utilizando un modelo dimensional con tablas de hechos y dimensiones:

![Estructura OLAP](img/Estructura%20de%20OLAP.PNG)

## 📓 Notebooks del Proyecto

### 1. Bronze - Extracción de Datos (`01_bronze_raw_extract.ipynb`)

Extrae los datos originales de la base de datos Northwind sin aplicar transformaciones. Esta capa preserva los datos en su estado "crudo" (raw) para garantizar la trazabilidad.

**Principales tareas:**
- Conexión a la base de datos Northwind
- Extracción de todas las tablas
- Almacenamiento en formato raw

### 2. Silver - Limpieza y Transformación (`02_silver_clean.ipynb`)

Aplica procesos de calidad de datos para preparar la información para análisis.

**Principales tareas:**
- Transformación de tipos de datos
- Identificación y manejo de datos nulos
- Detección y eliminación de duplicados
- Estandarización de formatos
- Validación de integridad referencial

### 3. Gold - Transformación OLAP (`03_gold_transform.ipynb`)

Transforma el esquema OLTP normalizado en un esquema OLAP dimensional, creando tablas de hechos y dimensiones.

**Principales tareas:**
- Creación de tablas de dimensiones (clientes, productos, empleados, tiempo, etc.)
- Creación de tablas de hechos (ventas, inventario, etc.)
- Implementación de claves subrogadas
- Optimización para consultas analíticas
- Desnormalización controlada

## 🛠️ Tecnologías Utilizadas

- **Python 3.14+**: Lenguaje de programación principal
- **Pandas**: Manipulación y análisis de datos
- **NumPy**: Operaciones numéricas
- **SQLAlchemy**: ORM para interacción con bases de datos
- **MySQL Connector**: Conector específico para MySQL
- **Jupyter Notebooks**: Entorno de desarrollo interactivo
- **python-dotenv**: Gestión de variables de entorno
- **tqdm**: Barras de progreso para procesos largos
- **uv**: Gestor de paquetes y entornos virtuales

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.14 o superior
- [uv](https://github.com/astral-sh/uv) (gestor de paquetes ultrarrápido)

### Instalación de uv

Si aún no tienes `uv` instalado, puedes instalarlo con:

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clonar el Proyecto

```bash
git clone <url-del-repositorio>
cd proyecto-northwind
```

### Instalar Dependencias

`uv` instalará automáticamente todas las dependencias especificadas en `pyproject.toml`:

```bash
# Sincronizar el entorno virtual con las dependencias del proyecto
uv sync
```

Esto creará un entorno virtual en `.venv` e instalará todas las librerías necesarias:
- pandas
- numpy
- jupyter
- mysql-connector-python
- sqlalchemy
- python-dotenv
- tqdm
- googletrans
- legacy-cgi

### Configurar Variables de Entorno

Crea o edita el archivo `.env` en la raíz del proyecto con tus credenciales de base de datos:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=northwind
```

### Ejecutar los Notebooks

Activa el entorno virtual y abre Jupyter:

```bash
# Activar el entorno virtual (uv lo hace automáticamente)
uv run jupyter notebook
```

Luego ejecuta los notebooks en orden:
1. `01_bronze_raw_extract.ipynb`
2. `02_silver_clean.ipynb`
3. `03_gold_transform.ipynb`

## 📦 Gestión de Dependencias con uv

### ¿Por qué uv?

`uv` es un gestor de paquetes Python extremadamente rápido escrito en Rust, compatible con pip y virtualenv pero con mejor rendimiento.

### Comandos Útiles

```bash
# Instalar una nueva dependencia
uv add nombre-paquete

# Instalar dependencias de desarrollo
uv add --dev nombre-paquete

# Actualizar dependencias
uv sync --upgrade

# Ejecutar un comando en el entorno virtual
uv run python script.py

# Ejecutar un notebook
uv run jupyter notebook
```

## 📈 Resultados Esperados

Al finalizar el proceso ETL, tendrás:

✅ Datos limpios y validados
✅ Esquema OLAP optimizado para análisis
✅ Tablas de hechos y dimensiones bien definidas
✅ Capacidad para realizar análisis complejos de ventas, clientes y productos
✅ Trazabilidad completa de las transformaciones aplicadas

## 📝 Notas

- Asegúrate de tener acceso a una base de datos MySQL con el esquema Northwind cargado
- Los notebooks están diseñados para ejecutarse secuencialmente
- Cada notebook genera outputs que son utilizados por el siguiente
- Se recomienda revisar los resultados de cada etapa antes de continuar

---

**Desarrollado con 💙 usando Python y uv**