import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(message):
    # Definir los parámetros del correo electrónico
    de = 'srtrollxd6@gmail.com'
    para = ['hugopolo2000@gmail.com']
    asunto = 'Ngrok link'

    # Crear un mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = de
    mensaje['To'] = ', '.join(para)
    mensaje['Subject'] = asunto

    # Agregar el cuerpo del mensaje
    cuerpo = message
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Conectar con el servidor de correo electrónico de Gmail
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(de, 'hupogo2000')

    # Enviar el correo electrónico
    texto = mensaje.as_string()
    servidor.sendmail(de, para, texto)

    # Cerrar la conexión
    servidor.quit()
