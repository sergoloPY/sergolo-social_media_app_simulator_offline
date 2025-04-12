import tkinter as tk
from PIL import Image, ImageTk
import base64
import io

# 1. Crear la ventana raíz
window = tk.Tk()

# 2. Leer y codificar la imagen
with open("imagenes_social_media_app_simulator_offline/verification.png", "rb") as imagen:
    imagen_base64 = base64.b64encode(imagen.read())
    imagen_decodeada = imagen_base64.decode("utf-8")

# 3. Decodificar la cadena Base64 y cargar la imagen con Pillow
img_data = base64.b64decode(imagen_decodeada)
img_bytes = io.BytesIO(img_data)
img_pil = Image.open(img_bytes)

# 4. Convertir la imagen para Tkinter, especificando el master (ventana raíz)
img_tk = ImageTk.PhotoImage(img_pil, master=window)

# 5. Crear un canvas y mostrar la imagen
canvas = tk.Canvas(window, width=img_pil.width, height=img_pil.height)
canvas.pack()
canvas.create_image(img_pil.width // 2, img_pil.height // 2, image=img_tk)
canvas.img = img_tk  # Guardar referencia para evitar que la imagen sea recolectada por el recolector de basura de python

# 6. Ejecutar el bucle principal
window.mainloop()
