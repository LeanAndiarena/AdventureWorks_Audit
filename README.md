### 📋 Texto para copiar y pegar en `README.md`


# 🚴 AdventureWorks Lead Auditor

Este proyecto es un **Pipeline de Datos Automatizado** diseñado para el departamento de ventas de AdventureWorks. Su objetivo es evitar la duplicidad de registros al cruzar nuevos leads potenciales con la base de datos histórica de clientes.

El sistema utiliza **Lógica Difusa (Fuzzy Logic)** para detectar coincidencias en nombres que no son idénticos al 100% (ej: "Ken Sanchez" vs "Kenneth Sanchez"), genera un reporte en PDF y lo distribuye automáticamente por correo electrónico.

## 🚀 Funcionalidades Principales

* **Extracción (ETL):** Conexión segura a SQL Server para obtener clientes existentes e importación de archivos CSV para nuevos leads.
* **Análisis de Datos:** Uso de la librería `thefuzz` para calcular un *score* de similitud entre nombres.
* **Reporte Automático:** Generación de PDFs dinámicos usando `Jinja2` (HTML templates) y `WeasyPrint`.
* **Alertas:** Envío automático del reporte vía Gmail (SMTP).
* **Observabilidad:** Sistema de Logging completo (`registro_ejecucion.log`) con filtrado de ruido para monitorear la ejecución y errores.
* **Seguridad:** Gestión de credenciales mediante variables de entorno (`.env`).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.12+
* **Manipulación de Datos:** Pandas
* **Base de Datos:** PyODBC (SQL Server)
* **Lógica Difusa:** TheFuzz & Levenshtein
* **Reportes:** Jinja2, WeasyPrint
* **Entorno:** Python-dotenv

## 📂 Estructura del Proyecto

```text
AdventureWorks_Audit/
├── data/                   # Archivos de entrada (leads_nuevos.csv)
├── src/                    # Código fuente modular
│   ├── db.py               # Módulo de conexión a Base de Datos
│   ├── logic.py            # Lógica de detección de duplicados
│   ├── reporter.py         # Generación de PDF
│   └── email_sender.py     # Envío de correo
├── templates/              # Plantillas HTML para el reporte
│   └── template.html
├── .env                    # Variables de entorno (NO subir a Git)
├── .gitignore              # Archivos ignorados
├── main.py                 # Script principal (Orquestador)
├── registro_ejecucion.log  # Log de actividad
└── README.md               # Documentación

```

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
```bash
git clone [https://github.com/TU_USUARIO/AdventureWorks_Audit.git](https://github.com/TU_USUARIO/AdventureWorks_Audit.git)
cd AdventureWorks_Audit

```


2. **Crear entorno virtual:**
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate

```


3. **Instalar dependencias:**
```bash
pip install -r requirements.txt

```


4. **Configurar Variables de Entorno:**
Crea un archivo `.env` en la raíz del proyecto con las siguientes claves:
```env
DB_PASS=tu_contraseña_sql
PASS=tu_app_password_gmail

```



## ▶️ Ejecución

Para correr el pipeline completo manualmente:

```bash
python main.py

```

El script generará un archivo PDF con la fecha actual (ej: `reporte_duplicados_yyyy-mm-dd.pdf`) y lo enviará por correo.

## 📊 Ejemplo de Lógica (Snippet)

El sistema considera un duplicado si el *score* de similitud supera el 80%:

```python
ratio = fuzz.ratio(nombre_nuevo, nombre_db)
if ratio > 80:
    # Se marca como posible duplicado

```

## ✒️ Autor

**Leandro Andiarena** - *Data Scientist in training*
Desarrollado como parte de un portafolio de Ingeniería de Datos y BI.

---


