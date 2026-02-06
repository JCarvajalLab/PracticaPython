# No funciona por la seguridad del gmail, triste pero cierto 
import smtplib

salidaCorreo = "enviando@gmail.com"
entradaCorreo = "recibiendo@gmail.com"
password = "password123"


asunto = "Prueba de correo electronico en python"
cuerpo = "Hola Como estan?"

mensaje = f"""From: Aprendiendo a programar{salidaCorreo}
To: Josefa{entradaCorreo}
Subject: {asunto}\n
{cuerpo}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(salidaCorreo, password)
    print("Logeando...")
    server.sendmail(salidaCorreo, entradaCorreo, mensaje)
    print("¡El correo electrónico ha sido enviado!")
except smtplib.SMTPAuthenticationError as e:
    print("Error de autenticación:", e)
finally:
    server.quit()