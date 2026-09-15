from email.message import EmailMessage
import smtplib
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

ventana = Tk()
ventana.title("✨ APLICACIÓN DE MENSAJERIA ✨")
ventana.geometry("390x590")
ventana.resizable(0,0)


BG_COLOR = "#fff0f3"          
ACCENT_PINK = "#ffb3c6"       
TEXT_COLOR = "#785964"       
WHITE = "#ffffff"
INPUT_BG = "#fff9fb"

ventana.config(bd=12, bg=BG_COLOR)

MI_CORREO = "cuentaotradeotra@gmail.com"
MI_CLAVE = "ljzs vndb hxar rizm"

Label(ventana, text="💌 ENVIAR CORREO 💌", fg=TEXT_COLOR, bg=BG_COLOR, font=("Helvetica", 14, "bold"), padx=5, pady=2).grid(row=0, column=0, columnspan=2)

# IMAGEN PERSONALIZADA
try:
    imagen_gmail = Image.open("logo_uwu.jpg")
    nueva_imagen = imagen_gmail.resize((110, 80))
    render = ImageTk.PhotoImage(nueva_imagen)
    label_imagen = Label(ventana, image=render, bg=BG_COLOR)
    label_imagen.image = render
    label_imagen.grid(row=1, column=0, columnspan=2, pady=10)
except Exception:
    # Espacio alternativo por si no se encuentra la imagen localmente
    Label(ventana, text="୨ৎ", fg=ACCENT_PINK, bg=BG_COLOR, font=("Helvetica", 20)).grid(row=1, column=0, columnspan=2, pady=10)

# Tarjeta bonita para el correo remitente
correo_frame = Frame(ventana, bg=ACCENT_PINK, bd=0)
correo_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")
Label(correo_frame, text=f"♡ Mi correo: {MI_CORREO} ♡", fg=WHITE, bg=ACCENT_PINK, font=("Helvetica", 9, "bold"), padx=10, pady=6).pack()

destinatario = StringVar(ventana)
asunto = StringVar(ventana)
opcion_seleccionada = StringVar(ventana)

# Lista de correos requerida
lista_correos = [
    "Seleccionar contacto...",
    "fjcoronati@gmail.com",        
    "mfedullo@gmail.com",
    "lafortaleza246@gmail.com",
    "Katsukibakugouteamo20@gmail.com",       
]
opcion_seleccionada.set(lista_correos[0])

# Función para sincronizar el OptionMenu con el campo Entry
def actualizar_destinatario(*args):
    seleccion = opcion_seleccionada.get()
    if seleccion != "Seleccionar contacto...":
        destinatario.set(seleccion)

opcion_seleccionada.trace("w", actualizar_destinatario)

# Estilos estéticos para campos de entrada
label_font = ("Helvetica", 9, "bold")
entry_font = ("Helvetica", 10)

Label(ventana, text="Contactos:", fg=TEXT_COLOR, bg=BG_COLOR, font=label_font).grid(row=3, column=0, sticky="e", pady=8, padx=5)

# OptionMenu personalizado estilo coquette
opt_menu = OptionMenu(ventana, opcion_seleccionada, *lista_correos)
opt_menu.config(bg=WHITE, fg=TEXT_COLOR, activebackground=ACCENT_PINK, activeforeground=WHITE, font=("Helvetica", 9), highlightthickness=0, bd=1, relief="solid")
opt_menu["menu"].config(bg=WHITE, fg=TEXT_COLOR, font=("Helvetica", 9))
opt_menu.grid(row=3, column=1, sticky="ew", pady=8)

Label(ventana, text="Destinatario:", fg=TEXT_COLOR, bg=BG_COLOR, font=label_font).grid(row=4, column=0, sticky="e", pady=8, padx=5)
entry_dest = Entry(ventana, textvariable=destinatario, width=28, bg=INPUT_BG, fg=TEXT_COLOR, font=entry_font, bd=1, relief="solid", highlightcolor=ACCENT_PINK)
entry_dest.grid(row=4, column=1, pady=8, ipady=3, sticky="w")

Label(ventana, text="Asunto:", fg=TEXT_COLOR, bg=BG_COLOR, font=label_font).grid(row=5, column=0, sticky="e", pady=8, padx=5)
entry_asunto = Entry(ventana, textvariable=asunto, width=28, bg=INPUT_BG, fg=TEXT_COLOR, font=entry_font, bd=1, relief="solid", highlightcolor=ACCENT_PINK)
entry_asunto.grid(row=5, column=1, pady=8, ipady=3, sticky="w")

Label(ventana, text="Mensaje:", fg=TEXT_COLOR, bg=BG_COLOR, font=label_font).grid(row=6, column=0, sticky="ne", pady=8, padx=5)
mensaje = Text(ventana, height=5, width=26, padx=8, pady=8, bg=INPUT_BG, fg=TEXT_COLOR, font=("Helvetica", 9), bd=1, relief="solid")
mensaje.grid(row=6, column=1, pady=8, sticky="w")

# ENVÍO DE CORREO
def enviar_email():
    try:
        # Validación básica
        if destinatario.get() == "" or destinatario.get() == "Seleccionar contacto...":
            messagebox.showwarning("Atención 💌", "Por favor, ingresa un destinatario válido.")
            return

        email = EmailMessage()
        email["From"] = MI_CORREO
        email["To"] = destinatario.get()
        email["Subject"] = asunto.get()
        email.set_content(str(mensaje.get(1.0, 'end')))

        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(MI_CORREO, MI_CLAVE)
        smtp.sendmail(MI_CORREO, destinatario.get(), email.as_string())
        messagebox.showinfo("¡Éxito! 🎀", "Mensaje enviado correctamente ✨")
        smtp.quit()
        
    except smtplib.SMTPAuthenticationError:
         messagebox.showerror("Error de Inicio", "Fallo de autenticación. Verifica tu correo y contraseña de aplicación.")
    except Exception as e:
         messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Botón estilo coquette con tonos rosados y bordes suaves
btn_enviar = Button(ventana, text="ENVIAR 🎀", command=enviar_email, height=1, width=14, bg=ACCENT_PINK, fg=WHITE, font=("Helvetica", 10, "bold"), bd=0, activebackground="#ff8fab", activeforeground=WHITE, cursor="hand2")
btn_enviar.grid(row=7, column=0, columnspan=2, padx=5, pady=12)

ventana.mainloop()
