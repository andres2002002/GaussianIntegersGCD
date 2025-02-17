import tkinter as tk
from tkinter import ttk
from logic.gaussian_prime import is_gaussian_prime

class PrimalityScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="Menu.TFrame")
        self.controller = controller

        # --- Frame superior para el botón toggle en la esquina superior derecha ---
        top_frame = ttk.Frame(self, style="Menu.TFrame")
        top_frame.pack(fill="x", padx=10, pady=5)
        
        # --- Título ---
        self.title_label = ttk.Label(self, text="Prueba de Primalidad", background="#2e2e2e", font=("Arial", 14, "bold"))
        self.title_label.pack(pady=10)
        
        self.toggle_button = ttk.Button(top_frame, text="Modo Claro", command=self.controller.toggle_mode)
        self.toggle_button.pack(side="right")
        self.return_button = ttk.Button(top_frame, text="Return", command=self.button_command)
        self.return_button.pack(side="left")

        # --- Frame para la entrada de números complejos ---
        input_frame = ttk.Frame(self, style="Menu.TFrame")
        input_frame.pack(padx=20, pady=5, fill="x")
        
        font, size, wight = "Arial", 12, ""
        
        ttk.Label(input_frame, text="z:", font=(font, size, wight)).grid(row=0, column=0, padx=5, pady=5)
        self.real1 = ttk.Entry(input_frame, width=10)
        self.real1.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(input_frame, text="+", font=(font, size, wight)).grid(row=0, column=2)
        self.imag1 = ttk.Entry(input_frame, width=10)
        self.imag1.grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(input_frame, text="i", font=(font, size, wight)).grid(row=0, column=4)

        # Botón para calcular la suma
        self.calculate_button = ttk.Button(self, text="Probar", command=self.process)
        self.calculate_button.pack(pady=5)

        # Campo de texto para mostrar el resultado
        self.result_label = ttk.Label(self, text="result:", font=(font, size, wight))
        self.result_label.pack(fill="x", padx=20, pady=2)
        self.result_text = tk.Text(self, height=5, width=40, wrap="word")
        self.result_text.pack(pady=10, fill="x")

        # Aplica el estilo inicial según el modo
        self.apply_style()
    
    def button_command(self):
        print(f"Regrasar al Menu")
        self.controller.show_frame("MenuScreen")

    def get_value_or_zero(self, entry):
        try:
            return float(entry.get())
        except ValueError:
            return 0
    
    def process(self):
        try:
            real1 = self.get_value_or_zero(self.real1)
            imag1 = self.get_value_or_zero(self.imag1)
            
            z = complex(real1, imag1)
            
            is_prime, reason = is_gaussian_prime(z)
            result = "Es primo" if is_prime else "No es primo"
            
            result_str = f"z = {z}\n\n{result}\n\n Razon: {reason}"
        
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, result_str)
        except ValueError:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Entrada no válida")

    def apply_style(self):
        """Actualiza los estilos de la pantalla según el modo (oscuro/claro)."""
        if self.controller.dark_mode:
            self.controller.style.configure('Menu.TFrame', background='#2e2e2e')
            self.controller.style.configure('TButton', background='#444444', foreground='white')
            self.controller.style.configure('TLabel', background='#2e2e2e', foreground='white')
            self.controller.style.map('TButton', background=[('active', '#555555')])
            self.configure(style='Menu.TFrame')
            self.toggle_button.config(text='Modo Claro')
            self.title_label.config(foreground='white', background='#2e2e2e')
        else:
            self.controller.style.configure('Menu.TFrame', background='white')
            self.controller.style.configure('TButton', background='#f0f0f0', foreground='black')
            self.controller.style.configure('TLabel', background='white', foreground='black')
            self.controller.style.map('TButton', background=[('active', '#e0e0e0')])
            self.configure(style='Menu.TFrame')
            self.toggle_button.config(text='Modo Oscuro')
            self.title_label.config(foreground='black', background='white')
