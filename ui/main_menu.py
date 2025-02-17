import tkinter as tk
from tkinter import ttk

screens = {
    0: "Calcular MCD",
    1: "MCD Extendido",
    2: "Prueba de Primalidad",
    3: "Factorizacion en primos",
}

screens_nav = {
    0: "GcdScreen",
    1: "GcdExtendedScreen",
    2: "PrimalityScreen",
    3: "FactorizationScreen",
}

class MenuScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="Menu.TFrame")
        self.controller = controller

        # --- Frame superior para el botón toggle en la esquina superior derecha ---
        top_frame = ttk.Frame(self, style="Menu.TFrame")
        top_frame.pack(fill="x", padx=10, pady=5)
        
        # --- Título ---
        self.title_label = ttk.Label(self, text="Enteros Gaussianos", background="#2e2e2e", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)
        
        self.toggle_button = ttk.Button(top_frame, text="Modo Claro", command=self.controller.toggle_mode)
        self.toggle_button.pack(side="right")

        # --- Frame para los 4 botones de opciones ---
        buttons_frame = ttk.Frame(self, style="Menu.TFrame")
        buttons_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Configuración del grid para una mejor alineación y adaptabilidad
        for i in range(2):
            buttons_frame.columnconfigure(i, weight=1)
            buttons_frame.rowconfigure(i, weight=1)

        # Creación y posicionamiento de los 4 botones con un diseño mejorado
        self.buttons = []
        for i in range(2):
            for j in range(2):
                num = i * 2 + j 
                btn = ttk.Button(
                    buttons_frame,
                    text=screens[num],
                    command=lambda n=num: self.button_command(n)
                )
                btn.grid(row=i, column=j, padx=15, pady=15, ipadx=20, ipady=10, sticky="nsew")
                self.buttons.append(btn)

        # Aplica el estilo inicial según el modo
        self.apply_style()

    def button_command(self, num):
        print(f"Opción {num} seleccionada")
        self.controller.show_frame(screens_nav[num])

    def apply_style(self):
        """Actualiza los estilos de la pantalla según el modo (oscuro/claro)."""
        if self.controller.dark_mode:
            self.controller.style.configure('Menu.TFrame', background='#2e2e2e')
            self.controller.style.configure('TButton', background='#444444', foreground='white')
            self.controller.style.map('TButton', background=[('active', '#555555')])
            self.configure(style='Menu.TFrame')
            self.toggle_button.config(text='Modo Claro')
            self.title_label.config(foreground='white', background='#2e2e2e')
        else:
            self.controller.style.configure('Menu.TFrame', background='white')
            self.controller.style.configure('TButton', background='#f0f0f0', foreground='black')
            self.controller.style.map('TButton', background=[('active', '#e0e0e0')])
            self.configure(style='Menu.TFrame')
            self.toggle_button.config(text='Modo Oscuro')
            self.title_label.config(foreground='black', background='white')

