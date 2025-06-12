import tkinter as tk
from tkinter import messagebox

class JuegoGato:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Gato (Tic-Tac-Toe)")
        self.root.geometry("300x320")
        self.root.resizable(False, False)
        self.turno = "X"
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.crear_tablero()

    def crear_tablero(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(
                    self.root, text="", font=("Arial", 20),
                    width=5, height=2,
                    command=lambda f=fila, c=col: self.jugada(f, c)
                )
                boton.grid(row=fila, column=col, padx=5, pady=5)
                self.botones[fila][col] = boton

    def jugada(self, fila, col):
        boton = self.botones[fila][col]
        if boton["text"] == "":
            boton["text"] = self.turno
            if self.turno == "X":
                boton["fg"] = "red"
            else:
                boton["fg"] = "blue"

            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.turno} ha ganado!")
                self.reiniciar_juego()
            elif self.verificar_empate():
                messagebox.showinfo("Empate", "¡El juego terminó en empate!")
                self.reiniciar_juego()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        b = self.botones
        t = self.turno
        for fila in b:
            if all(boton["text"] == t for boton in fila):
                return True
        for col in range(3):
            if all(b[fila][col]["text"] == t for fila in range(3)):
                return True
        if all(b[i][i]["text"] == t for i in range(3)) or all(b[i][2 - i]["text"] == t for i in range(3)):
            return True
        return False

    def verificar_empate(self):
        return all(self.botones[fila][col]["text"] != "" for fila in range(3) for col in range(3))

    def reiniciar_juego(self):
        for fila in self.botones:
            for boton in fila:
                boton["text"] = ""
                boton["fg"] = "black"
        self.turno = "X"

if __name__ == "__main__":
    ventana = tk.Tk()
    juego = JuegoGato(ventana)
    ventana.mainloop()
