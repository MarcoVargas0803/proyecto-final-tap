from tkinter.ttk import Style, Treeview
import customtkinter as ct
from customtkinter import CTkImage, CTkLabel
from PIL import Image
import bd_management
#Esta es una clase que permite hacer de diferentes funcionalidades con las imagenes
class ImageManagement:
    def __init__(self, path_list: list):
        self.paths = path_list

    #Función que recibe lista de paths y devuelve lista de CTkImage o None
    def open_images(self) -> list[CTkImage | None]:
        images = []
        for path in self.paths:
            try:
                image_pil = Image.open(path)
                image_pil.thumbnail((100, 100))  # Ajusta el tamaño máximo manteniendo la relación de aspecto
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
        self.configure(border_width=2,corner_radius=0)


        #Llamamos a la clase ImageManagement.open_images() para abrir la imagen
        # open_images recibe una lista de rutas y devuelve una lista de CtkImage
        images_main_title = ImageManagement(["logo_empresa.jpg"]).open_images()

        #Operación ternaria para agregar imagen a image_label_title
        # Si no se encuentra la imagen, se muestra un texto alternativo
        for index, image in enumerate(images_main_title):
            self.image_label_title = ct.CTkLabel(self, image=image, text="") \
                if image else ct.CTkLabel(self, text="Sin imagen")
            self.image_label_title.grid(row=0, column=index, sticky="nsew", padx=10, pady=10)

        #Text_Label de la parte superior
        self.text_label_title = ct.CTkLabel(self,text=text_title,font=("Arial",50))
        self.text_label_title.grid(column=1,row=0,sticky= "ew",padx=10,pady=10)

class FrameMain(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)
        self.treeview_creation()
        self.configure(border_width=2,corner_radius=0)

    def treeview_creation(self):
        style = Style()
        style.configure("Custom.Treeview",
                        foreground="black",
                        background="lightgray",
                        font=('Arial', 20),
                        rowheight=35)
        style.map("Custom.Treeview",
                  background=[('selected', 'lightblue')],
                  foreground=[('selected', 'black')])
        self.tv = Treeview(self, columns=("Columna1", "Columna2","Columna3","Columna4","Columna5","Columna6"), style="Custom.Treeview")

        self.tv.heading("#0", text="Id")
        self.tv.heading("Columna1", text="Propietario")
        self.tv.heading("Columna2", text="Marca")
        self.tv.heading("Columna3", text="Modelo")
        self.tv.heading("Columna4", text="Año")
        self.tv.heading("Columna5", text="Costo Total")
        self.tv.heading("Columna6", text="Tipo de Mantenimiento")

        # Column tv configure
        self.tv.column("#0", width=2, minwidth=2, stretch=True)

        # tv.configure()
        self.tv.tag_configure('par', background='#302c2c', font=("Arial", 20), foreground="#4e585d")
        self.tv.tag_configure('impar', background='#28241c', font=("Arial", 20), foreground="#4e585d")

        self.tv.grid(column=0, row=0, sticky="nsew")
        self.llenar_treeview()

    def llenar_treeview(self):
        # Limpiar el Treeview antes de cargar nuevos datos
        for row in self.tv.get_children():
            self.tv.delete(row)

        # Obtener todos los eventos y contar cuántos asistentes tienen
        lista_autos = bd_management.obtener_autos()
        for auto in lista_autos:
            # Agregar la fila al Treeview
            self.tv.insert("", "end", text=auto.id, values=(auto.propietario,
                                                            auto.marca,auto.modelo,
                                                            auto.anio,auto.costo_total,
                                                            auto.tipo_mantenimiento))

class FrameSecond(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(index=(0,1), weight=1)
        self.grid_rowconfigure(index=0, weight=1)
        self.configure(border_width=2,corner_radius=0)
        self.create_botton_send_pdf()
        self.botton_exit()

    def send_pdf(self):
        print("Probando PDF")

    def salir_ventana(self):
        self.master.destroy()

    def create_botton_send_pdf(self):
        botton_to_pdf = ct.CTkButton(self,corner_radius=10,hover_color="red",text="Imprimir",command=self.send_pdf)
        botton_to_pdf.grid(column=0,row=0, pady=(10,20), padx=10)

    def botton_exit(self):
        botton_to_pdf = ct.CTkButton(self,corner_radius=10,hover_color="red",text="salir",command=self.salir_ventana)
        botton_to_pdf.grid(column=1,row=0, pady=(10,20), padx=10)

class AppMenuShowCars(ct.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")

        self.resizable(True, True)
        self.title("Add Car")
        self.configure(fg_color="#D2DFD9")

        # Modo de apariencia
        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")

        #Configuración Inicial de self
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=2)
        self.grid_rowconfigure(2,weight=0)

        frame_title_show_cars = FrameTitle(self,"Mostrar autos")
        frame_title_show_cars.grid(column=0,row=0)

        frame_main_show_cars = FrameMain(self)
        frame_main_show_cars.grid(column=0,row=1,sticky="nsew")

        frame_second_options = FrameSecond(self)
        frame_second_options.grid(column=0,row=2,sticky="nsew")


