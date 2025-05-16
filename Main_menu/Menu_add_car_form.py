import customtkinter as ct
from customtkinter import CTkImage
from PIL import Image
from auto_class import Auto
import bd_management as bd
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
        self.grid_rowconfigure(index=(0,1,2,3,4), weight=1)

        #Lista de los textos a agregar a los entries y labels
        self.placeholders_text = placeholders_text
        self.labels_text = labels_text

        self.entries_list_to_db = []

        #LLamamos a la función para agregar los labels
        self.add_text_to_label()
        #Llamamos a la función para agregar los entries
        self.add_entries()
        #Llamamos a la función para agregar el combobox
        self.add_year_Combobox()
        #Llamamos a la función para agregar el label de confirmación
        self.confirm_label()

    # Label de confirmación
    def confirm_label(self):
        confirm_label = ct.CTkLabel(self, text="Auto agregado correctamente", font=("Arial", 25))
        confirm_label.grid(column=1, row=4, sticky="nsew", padx=10, pady=10)

        confirm_label.bind("<Enter>", lambda event: confirm_label.configure(fg_color="green"))
        confirm_label.bind("<Leave>", lambda event: confirm_label.configure(fg_color="transparent"))

        confirm_label.bind("<Return>", lambda e: self.add_cars_from_db())
        confirm_label.bind("<Button-1>", lambda e: self.add_cars_from_db())

    # Bucle for para texto a los labels
    def add_text_to_label(self):
        # Se realiza el zip entre los textos y los colores, y después se realiza enumérate para el índice
        for index, text in enumerate(self.labels_text):
            texts_labels_main = ct.CTkLabel(self, text=text, font=("Arial", 25))
            texts_labels_main.grid(column=0, row=index, sticky="w", padx=10, pady=10)

    def add_year_Combobox(self):
        # Crear un Combobox para el año
        self.year_combobox = ct.CTkComboBox(self, values=[str(year) for year in range(1900, 2024)], font=("Arial", 25))
        self.year_combobox.grid(column=1, row=3, sticky="ew", padx=10, pady=10)

    def add_entries(self):
        # Bucle for para crear los entries
        for index, text in enumerate(self.placeholders_text):
            entry = ct.CTkEntry(self, placeholder_text=text, font=("Arial", 25))
            self.entries_list_to_db.append(entry)
            entry.grid(column=1, row=index, sticky="we", padx=10, pady=10)

    def add_cars_from_db(self):
        # Crea un nuevo objeto Auto y asignar valores desde los entries
        new_car = Auto()
        atributos = ["propietario", "marca", "modelo", "anio"]  # Atributos del objeto Auto

        #Recorre los entries y realiza el setattr para asignar los valores al objeto
        for index, entry in enumerate(self.entries_list_to_db):
            if index < len(atributos):
                setattr(new_car, atributos[index], entry.get())  # Asignar el valor del entry al atributo correspondiente

        # Asignar el año desde el combobox
        new_car.anio = int(self.year_combobox.get())

        # Aquí podrías guardar el auto en la base de datos
        bd.guardar_auto(new_car)
        # Limpiar los entries después de agregar el auto
        for entry in self.entries_list_to_db:
            entry.delete(0, ct.END)

class AppAddCar(ct.CTkToplevel):
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



