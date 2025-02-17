import tkinter as tk
from tkinter import ttk
from ui.main_menu import MenuScreen
from ui.gcd_screen import GcdScreen
from ui.gcd_extended_screen import GcdExtendedScreen
from ui.primality_screen import PrimalityScreen
from ui.factorization_screen import FactorizationScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación TTK Multipágina")
        self.geometry("400x400")
        self.minsize(300, 300)

        # Configuración global del estilo
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Estado de modo: True para oscuro, False para claro.
        self.dark_mode = True

        # Contenedor para las distintas pantallas
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Instanciar las pantallas y registrarlas en el contenedor
        screens = (MenuScreen, GcdScreen, GcdExtendedScreen, PrimalityScreen, FactorizationScreen)
        for F in screens:
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuScreen")

    def show_frame(self, frame_name):
        """Levanta la pantalla indicada."""
        frame = self.frames[frame_name]
        frame.tkraise()

    def toggle_mode(self):
        """Alterna entre modo oscuro y claro y actualiza los estilos en cada pantalla."""
        self.dark_mode = not self.dark_mode
        for frame in self.frames.values():
            if hasattr(frame, "apply_style"):
                frame.apply_style()

if __name__ == "__main__":
    app = App()
    app.mainloop()
