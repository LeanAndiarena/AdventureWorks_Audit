import pandas as pd
from datetime import datetime  
from src.db import get_customers
from src.logic import find_duplicates
from src.reporter import generate_pdf_report
from src.email_sender import send_email_report

if __name__ == "__main__":
    
    # 1. Me conecto a la base de datos
    print("⏳ Obteniendo clientes de la DB...")
    df_db = get_customers()
    
    # 2. Obtengo el csv de leads nuevos
    print("⏳ Leyendo nuevos leads...")
    csv_nuevos = pd.read_csv('data/leads_nuevos.csv', sep=';')
    
    # 3. Busco duplicados
    print("🔍 Analizando duplicados...")
    lista_duplicados = find_duplicates(csv_nuevos, df_db)
    
    # Obtenemos la fecha de hoy y la convertimos a texto (Año-Mes-Dia)
    fecha_str = datetime.now().strftime('%Y-%m-%d')
    
    # Creamos el nombre dinámico usando esa fecha
    nombre_archivo = f"reporte_duplicados_{fecha_str}.pdf"
    # -------------------------------------------

    # 4. Genero reporte (pasándole el nombre dinámico)
    print(f"📄 Generando PDF: {nombre_archivo}...")
    generate_pdf_report(lista_duplicados.to_dict(orient='records'), nombre_archivo)
    
    # 5. Envio mail (buscando ese mismo nombre)
    print("✉️ Enviando correo...")
    send_email_report(nombre_archivo)