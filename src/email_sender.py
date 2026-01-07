from dotenv import load_dotenv
import os
from email.message import EmailMessage
import ssl
import smtplib
import mimetypes

def send_email_report(pdf_path):
    # Cargamos las variables del correo- Keys

    load_dotenv()

    email_sender = "andiarenaleandro@gmail.com"
    password = os.getenv("PASS")
    email_reciver = "lean3215@gmail.com"
    subject = "Reporte_duplicados"
    body = "Envio reporte con duplicados en la base de datos"

    adj = pdf_path


    # Configuro el mail inicializando la variable

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciver
    em['Subject'] = subject
    em.set_content(body)

    # Adjunto archivo

    try:
        
        # Mime determina el tipo de archivo y codificacion
        mime_type, _ = mimetypes.guess_type(adj)
        
         # Si no detecta tipo se asigna uno generico por seguridad
        # CORRECCIÓN: Verificamos la variable mime_type, no la librería
        if mime_type is None:
            mime_type = 'application/octet-stream'
        
        # Separamos tipo principal y subtipo
        maintype, subtype = mime_type.split('/', 1)
        
        # Abrimos el archivo en modo lectura binaria
        with open(adj, "rb") as file:
            file_data = file.read()
            
            #adjuntamos al correo
            em.add_attachment(
                file_data,
                maintype = maintype,
                subtype = subtype,
                filename = os.path.basename(adj)
                
            )
        print(f"📎 Archivo '{adj}' adjuntado correctamente.")

    except FileNotFoundError:
        print(f"⚠️ ALERTA: No se encontró el archivo '{adj}'. El correo se enviará sin adjunto.")
    except Exception as e:
        print(f"❌ Error al adjuntar archivo: {e}")
        
    #------------------------------------------------------------------------------

    context = ssl.create_default_context()


    # Bloque de envío con manejo de errores básico
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.send_message(em) # Método más moderno y limpio
            print("✅ Correo enviado exitosamente.")
            return True
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")
        return False