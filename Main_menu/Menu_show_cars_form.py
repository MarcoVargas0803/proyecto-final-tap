import customtkinter as ct
from PIL import Image
from customtkinter import CTkImage

class AppMenuShowCars(ct.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.resizable(False, False)
        self.title("Add Car")
        self.configure(fg_color="#D2DFD9")

        # Modo de apariencia
        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")