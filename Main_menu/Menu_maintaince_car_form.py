import customtkinter as ct
from customtkinter import CTkImage
from PIL import Image
from tkinter.ttk import Treeview, Style
import bd_management
from auto_class import Auto
#Esta es una clase que permite hacer de diferentes funcionalidades con las images
class ImageManagement:
    def __init__(self, path_list: list):
        self.paths = path_list

    #Función que recibe lista de paths y devuelve lista de CTkImage o None
    def open_images(self) -> list[CTkImage | None]:
        images = []
        for path in self.paths:
            try:
                image_pil = Image.open(path)
                image_pil.thumbnail((100,100))  # Ajusta el tamaño máximo manteniendo la relación de aspecto
                image = ct.CTkImage(light_image=image_pil, dark_image=image_pil, size=image_pil.size)
                images.append(image)
            except FileNotFoundError:
                print(f"Imagen no encontrada: {path}")
                images.append(None)
        return images


#Clase que crea el frame de la parte superior
class FrameTitle(ct.CTkFrame):
    def __init__(self, master, text_title: str = "Servicio Automotriz"):
        super().__init__(master)
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(index=(0,1),weight=1)
        self.grid_rowconfigure(index=0,weight=1)

        #Llamamos a la clase ImageManagement.open_images() para abrir la imagen
        # open_images recibe una lista de rutas y devuelve una lista de CtkImage
        images_main_title = ImageManagement(["logo_empresa.jpg"]).open_images()

        #Operación ternaria para agregar imagen a image_label_title
        # Si no se encuentra la imagen, se muestra un texto alternativo
        for index, image in enumerate(images_main_title):
            self.image_label_title = ct.CTkLabel(self, image=image, text="") \
                if image else ct.CTkLabel(self, text="Sin imagen")
            self.image_label_title.grid(row=0, column=index, sticky="nsew", padx=10, pady=(10, 8))

        #Text_Label de la parte superior
        self.text_label_title = ct.CTkLabel(self,text=text_title,font=("Arial",50))
        self.text_label_title.grid(column=1,row=0,sticky= "nsew",padx=10, pady=15)

class FrameMain(ct.CTkFrame):
    def __init__(self, master, placeholders_text: list, labels_text: list):
        super().__init__(master)
        self.master = master
        self.grid(row=1, column=0, sticky="nsew")
        self.grid_columnconfigure(index=(0,1), weight=1)
        self.grid_rowconfigure(index=(0,1), weight=1)

    def treeview_creation(self):
        #Estilo del mensaje
        style = Style()
        style.configure("Custom.Treeview",
                        foreground="black",
                        background="lightgray",
                        font=('Helvetica', 12),
                        rowheight=25)
        style.map("Custom.Treeview",
                  background=[('selected', 'lightblue')],
                  foreground=[('selected', 'black')])
        self.tv = Treeview(self, columns=("Columna1", "Columna2"),style="Custom.Treeview")
        self.tv.heading("#0", text="Id")
        self.tv.heading("Columna1", text="propietario")
        self.tv.heading("Columna2", text="marca")
        self.tv.heading("Columna2", text="modelo")
        self.tv.heading("Columna2", text="año")
        self.tv.heading("Columna2", text="costo_total")
        self.tv.heading("Columna2", text="mantenimiento")

        # Column tv configure
        self.tv.column("#0", width=2, minwidth=2, stretch=True)

        # tv.configure()
        self.tv.tag_configure('par', background='#302c2c', font=("Arial", 15), foreground="#4e585d")
        self.tv.tag_configure('impar', background='#28241c', font=("Arial", 15), foreground="#4e585d")

        self.tv.grid(column=0,row=0,sticky="nsew",columnspan=2)
        self.llenar_treeview()

    def llenar_treeview(self):
        # Limpiar el Treeview antes de cargar nuevos datos
        for row in self.tv.get_children():
            self.tv.delete(row)

        # Obtener todos los eventos y contar cuántos asistentes tienen
        lista_bd_autos = bd_management.obtener_autos()
        for auto in lista_bd_autos:
            # Agregar la fila al Treeview
            self.tv.insert("", "end", text=evento.id_event, values=(evento.name_event, asistencias_count))

class AppMaintenanceCar(ct.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Servicio Automotriz")
        self.geometry("1000x600")
        self.resizable(False, False)

        # Creamos 2 filas para Frames principales
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0,weight=0)
        self.grid_rowconfigure(1,weight=1)

        # Llamamos a la clase FrameTitle para crear el frame de la parte superior
        self.frame_title_add_car = FrameTitle(self,"Agregar Auto")
        self.frame_title_add_car.grid(column=0,row=0)
        # Llamamos a la clase FrameMain para crear el frame principal
        self.frame_main_add_car = FrameMain(self, ["Propietario","Marca", "Modelo"],
        ["Propietario","Ingrese la marca", "Ingrese el modelo", "Seleccione el año"])
        self.frame_main_add_car.grid(column=0, row=1, sticky="nsew", padx=10, pady=10)

        # Modo de apariencia
        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")