import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def generate_pdf_report(datos, nombre_archivo_salida):
    # 1. Cargar el Molde (Environment)
    # FileSystemLoader('templates') busca la carpeta templates en la raíz del proyecto
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    # 2. El Llenado (Rendering)
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    
    # Aquí pasamos las variables al HTML
    html_str = template.render(datos=datos, fecha_hoy=fecha_actual)

    # 3. La Conversión (WeasyPrint)
    # Transforma el string de HTML lleno a un archivo PDF real
    HTML(string=html_str).write_pdf(nombre_archivo_salida)
    
    print(f"✅ PDF generado exitosamente: {nombre_archivo_salida}")

if __name__ == "__main__":
    # Prueba rápida con datos falsos
    datos_prueba = [
        {'Nombre_Input': 'Test User', 'Coincidencia_DB': 'Test User Real', 'Score': 99, 'ID_AdventureWorks': 123}
    ]
    generate_pdf_report(datos_prueba, "reporte_prueba.pdf")