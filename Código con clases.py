import tkinter as tk
class saludando :
    def __init__(self):
        self.saludo="Hola mundo"
def mostrar():
    hola=saludando()
    tk.Label(ventana, text=f"{hola.saludo}").pack(pady=7)
ventana=tk.Tk()
ventana.title("Hola mundo")
ventana.geometry("300x200")
tk.Button(ventana, text="Mostrar hola mundo", command=mostrar, width=15).pack(pady=7)
ventana.mainloop()
