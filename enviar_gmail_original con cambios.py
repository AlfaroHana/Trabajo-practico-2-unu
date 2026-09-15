from email.message import EmailMessage
import smtplib
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

ventana = Tk()
ventana.title("APLICACIÓN DE MENSAJERIA")
ventana.geometry("380x550") 
ventana.resizable(0,0)
ventana.config(bd=10, bg="#f2f2f2")

MI_CORREO = "cuentaotradeotra@gmail.com"
MI_CLAVE = "clave"

Label(ventana, text="ENVIAR CORREO VIA GMAIL", fg="black", bg="#f2f2f2", font=("Arial", 15,"bold"), padx=5, pady=5).grid(row=0, column=0, columnspan=2)

#IMAGEN PERSONALIZADA

imagen_gmail = Image.open("logo_uwu.jpg")
nueva_imagen = imagen_gmail.resize((125, 90))
render = ImageTk.PhotoImage(nueva_imagen)
label_imagen = Label(ventana, image=render, bg="#f2f2f2")
label_imagen.image = render
label_imagen.grid(row=1, column=0, columnspan=2, pady=20)

Label(ventana, text=f"Mi correo: {MI_CORREO}", fg="white", bg="blue", font=("Arial", 10,"bold"), padx=5, pady=5).grid(row=2, column=0, columnspan=2, pady=5)

destinatario = StringVar(ventana)
asunto = StringVar(ventana)
opcion_seleccionada = StringVar(ventana)

# Lista de correos requerida
lista_correos = [
    "Seleccionar contacto...",
    "correo@gmail.com",       

]
opcion_seleccionada.set(lista_correos[0])

# Función para sincronizar el OptionMenu con el campo Entry
def actualizar_destinatario(*args):
    seleccion = opcion_seleccionada.get()
    if seleccion != "Seleccionar contacto...":
        destinatario.set(seleccion)

opcion_seleccionada.trace("w", actualizar_destinatario)

Label(ventana, text="Contactos:", fg="black", bg="#f2f2f2", font=("Arial", 10,"bold")).grid(row=3, column=0, sticky="e", pady=5)
OptionMenu(ventana, opcion_seleccionada, *lista_correos).grid(row=3, column=1, sticky="w", pady=5)

Label(ventana, text="Destinatario:", fg="black", bg="#f2f2f2", font=("Arial", 10,"bold")).grid(row=4, column=0, sticky="e", pady=5)
Entry(ventana, textvariable=destinatario, width=34).grid(row=4, column=1)

Label(ventana, text="Asunto:", fg="black", bg="#f2f2f2", font=("Arial", 10,"bold")).grid(row=5, column=0, sticky="e", pady=5)
Entry(ventana, textvariable=asunto, width=34).grid(row=5, column=1)

Label(ventana, text="Mensaje:", fg="black", bg="#f2f2f2", font=("Arial", 10,"bold")).grid(row=6, column=0, sticky="ne", pady=5)
mensaje = Text(ventana, height=5, width=28, padx=5, pady=5)
mensaje.grid(row=6, column=1, pady=5)
mensaje.config(font=("Arial", 9))


# ENVÍO DE CORREO
def enviar_email():
    try:
        # Validación básica
        if destinatario.get() == "" or destinatario.get() == "Seleccionar contacto...":
            messagebox.showwarning("Atención", "Por favor, ingresa un destinatario válido.")
            return

        email = EmailMessage()
        email["From"] = MI_CORREO
        email["To"] = destinatario.get()
        email["Subject"] = asunto.get()
        email.set_content(str(mensaje.get(1.0, 'end')))

        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(MI_CORREO, MI_CLAVE)
        smtp.sendmail(MI_CORREO, destinatario.get(), email.as_string())
        messagebox.showinfo("MENSAJERIA", "Mensaje enviado correctamente")
        smtp.quit()
        
    except smtplib.SMTPAuthenticationError:
         messagebox.showerror("Error de Inicio", "Fallo de autenticación. Verifica tu correo y contraseña de aplicación.")
    except Exception as e:
         messagebox.showerror("Error", f"Ocurrió un error: {e}")

Button(ventana, text="ENVIAR", command=enviar_email, height=2, width=10, bg="black", fg="white", font=("Arial", 10,"bold")).grid(row=7, column=0, columnspan=2, padx=5, pady=15)

ventana.mainloop()
