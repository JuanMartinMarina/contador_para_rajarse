##La idea es que el código funcione como una suerte de alarma

import datetime
import tkinter as tk

##Ventana
window = tk.Tk()
window.title("CONTADOR PARA IRME")

##Hora
now = datetime.datetime.now()
target_hour = datetime.datetime(now.year, now.month, now.day, 14, 00, 00)
time_left = (target_hour - now).total_seconds()

##Actualizar el contador
def update_counter():
    global time_left
    if time_left > 0:
        # Actualizar la etiqueta del contador con el tiempo restante en formato HH:MM:SS
        counter_label.config(text=datetime.timedelta(seconds=int(time_left)))
        # Restar un segundo al tiempo restante
        time_left -= 1
        # Esperar un segundo antes de volver a actualizar
        window.after(1000, update_counter)
    else:
        # Mostrar un mensaje cuando el tiempo se acaba
        counter_label.config(text="ANDATE A LA COMBI!")

##Etiqueta del contador
counter_label = tk.Label(window, font=("Arial", 60), fg="red")
counter_label.pack(padx=50, pady=50)

##Llamar a la función de actualización del contador
update_counter()

##Mostrar ventana
window.mainloop()
