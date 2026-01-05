¡Excelente decisión! Vamos a construir el **"Sistema de Auditoría de Duplicados" (Customer Deduplication Audit)**.

Este proyecto te va a quedar como portafolio estrella porque toca: **Ingeniería de Datos + Lógica Difusa (IA básica) + Reporting Corporativo + Automatización**.

Aquí tienes el Roadmap Técnico detallado fase por fase.

---

### 📂 FASE 0: Arquitectura y Cimientos (El Setup)

Antes de escribir lógica, preparamos el quirófano. Un proyecto serio no tiene archivos tirados en el escritorio.

1. **Estructura de Carpetas:** Crea esta estructura exacta en tu VS Code:
```text
AdventureWorks_Audit/
│
├── src/                 # Todo tu código Python va aquí
│   ├── __init__.py      # (Archivo vacío, marca la carpeta como paquete)
│   ├── db.py            # Módulo de conexión a SQL
│   ├── email_sender.py  # Módulo de envío de correos (tu script anterior refactorizado)
│   ├── logic.py         # Lógica de RapidFuzz
│   └── reporter.py      # Generación de PDF con Jinja2
│
├── templates/           # Tus archivos HTML base
│   ├── report_template.html
│   └── email_template.html
│
├── output/              # Aquí se guardarán los PDFs generados (ignorado por git)
│
├── .env                 # TUS CLAVES (SQL y Email) - ¡NO SUBIR A GIT!
├── .gitignore           # Configurado para ignorar .env, venv/ y output/
├── requirements.txt     # Lista de librerías
└── main.py              # El orquestador que une todo

```


2. **Git:** Inicializa el repositorio (`git init`) y haz tu primer commit con la estructura vacía y el `.gitignore` listo.

---

### 🌑 FASE 1: Ingesta de Datos (SQL Strategy)

Necesitamos comparar dos fuentes. Vamos a simular que Marketing te manda un Excel sucio ("Leads Nuevos") y tú debes chequear si ya existen en la base de AdventureWorks ("Clientes Históricos").

1. **El Dataset de Entrada (Simulado):** Crea un CSV manual (`data/leads_nuevos.csv`) con 5 o 6 nombres, algunos inventados y otros que *sabes* que existen en AdventureWorks pero escritos un poco mal (ej: "Jonh Yang" en vez de "John Yang").
2. **La Query SQL (`src/db.py`):**
* Conecta a `AdventureWorks2022`.
* Extrae: `BusinessEntityID`, `FirstName`, `LastName` de la tabla `Person.Person`.
* *Tip:* Concatena Nombre y Apellido en SQL o en Pandas para tener un campo `FullName` limpio para comparar.
* **Objetivo:** Tener un DataFrame `df_db` (los oficiales) y un DataFrame `df_leads` (los nuevos).



---

### 🌗 FASE 2: El Cerebro Fuzzy (RapidFuzz)

Aquí ocurre la magia en `src/logic.py`. Evitaremos comparar "todos contra todos" (porque explotaría tu PC). Compararemos "Leads vs DB".

1. **Librería:** `rapidfuzz` (instalar con pip).
2. **Lógica:**
* Itera por cada nombre en `df_leads`.
* Usa `process.extractOne` para buscar el mejor candidato en `df_db['FullName']`.
* **Regla de Negocio:** Si el `score` es **> 85**, márcalo como "Posible Duplicado".


3. **Output:** Genera un DataFrame de resultados (`df_resultados`) con columnas:
* `Nombre_Lead`
* `Candidato_DB`
* `ID_DB` (Para saber quién es en el sistema)
* `Score_Similitud` (ej: 92.5)



---

### 🌕 FASE 3: Generación de Reporte PDF (Reporting)

Los gerentes no leen DataFrames, leen PDFs bonitos. Trabajaremos en `src/reporter.py`.

1. **Templating (Jinja2):**
* Diseña `templates/report_template.html`. Debe tener un título, fecha y una **tabla HTML**.
* Usa Jinja2 para inyectar `df_resultados` dentro de esa tabla HTML dinámicamente (`{% for row in data %}...`).


2. **Renderizado (WeasyPrint o pdfkit):**
* Toma ese string HTML gigante que generó Jinja.
* Conviértelo a un archivo físico: `output/Auditoria_Duplicados_YYYY-MM-DD.pdf`.
* *Nota:* Si WeasyPrint te da problemas en Windows (a veces pide GTK), usaremos `xhtml2pdf` que es más simple.



---

### 🌖 FASE 4: Notificación (Email)

Refactoriza tu script de hoy dentro de `src/email_sender.py`.

1. **Función Reutilizable:** Transforma tu script en una función:
```python
def enviar_reporte(destinatario, ruta_pdf, metricas_resumen):
    # ... tu código smtplib ...

```


2. **Cuerpo HTML:** Usa `templates/email_template.html` para que el cuerpo del correo no sea texto plano, sino un resumen bonito ("Se encontraron 5 duplicados de 20 leads analizados").

---

### 🌘 FASE 5: El Orquestador (`main.py`)

Une todo.

1. **Argparse:** Permite ejecutar: `python main.py --archivo "leads_semana_1.csv" --email "gerente@fava.com"`.
2. **Flujo:**
* `main` llama a `db.get_customers()`
* `main` carga el CSV.
* `main` llama a `logic.find_duplicates()`
* `main` llama a `reporter.generate_pdf()`
* `main` llama a `email_sender.send()`


3. **Logging:** `logging.info("Proceso terminado. PDF enviado.")`.

---

### 🚀 Tu Misión Ahora: FASE 0 y 1

No intentes hacer todo hoy. Enfócate en los cimientos.

1. Arma la estructura de carpetas.
2. Crea el entorno virtual y el `requirements.txt`.
3. Crea el módulo `src/db.py` y logra traer los nombres completos de `Person.Person` a un DataFrame.

Cuando tengas ese DataFrame impreso en consola, **muéstramelo** y pasamos a la lógica Fuzzy. ¿Trato hecho?