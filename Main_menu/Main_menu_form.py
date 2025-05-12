import customtkinter as ct
from Menu_add_car_form import AppAddCar
from Menu_maintaince_car_form import AppMaintenanceCar
from Menu_show_cars_form import AppMenuShowCars

import customtkinter as ct
from customtkinter import CTkImage
from PIL import Image
#Esta es una clase que permite hacer de diferentes funcionalidades con las imagenes
class ImageManagement:
    ("logo_empresa.jpg", "imagen_main_1.png", "imagen_main_2.png",)
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


#Clase Frame_Main para crear el frame principal
class FrameMain(ct.CTkFrame):
    def __init__(self, master, values_text: list):
        super().__init__(master)
        self.master = master
        self.grid(row=1, column=0, sticky="nsew")
        self.grid_columnconfigure(index=(0,1), weight=1)
        self.grid_rowconfigure(index=(0,1,2,3), weight=1)
        #Lista de los textos a agregar a los labels
        self.values_text = values_text

        self.add_images_frame_main()
        self.add_text_to_labels()

    def window_add_car(self):
        add_car_win = AppAddCar()
        add_car_win.grab_set()
        add_car_win.wait_window()
        print("Abriendo ventana de agregar auto")

    def window_maintaince_car(self):
        maintance_car_win = AppMaintenanceCar
        maintance_car_win.grab_set()
        maintance_car_win.wait_window()
        print("Abriendo ventana de dar mantenimiento al auto")

    def window_show_cars(self):
        show_cars_win = AppMenuShowCars()
        show_cars_win.grab_set()
        show_cars_win.wait_window()
        print("Abriendo ventana de visualizar autos")

    def window_exit_menu(self):
        self.master.destroy()
        print("Saliendo del menu principal")


    def add_images_frame_main(self):
        #Llamamos a la clase ImageManagement para abrir la imagen
        images_frame_main = ImageManagement(["imagen_main_1.png", "imagen_main_2.png",
                                          "imagen_main_3.png", "imagen_main_4.png"]).open_images()

        # Operación ternaria para agregar imagen a image_label_title
        # Si no se encuentra la imagen, se muestra un texto alternativo
        for index, image in enumerate(images_frame_main):
            image_label_title = ct.CTkLabel(self, image=image, text="") \
                if image else ct.CTkLabel(self, text="Sin imagen")
            image_label_title.grid(row=index, column=0, sticky="nsew", padx=10, pady=10)

    #Bucle for para texto a los labels
    def add_text_to_labels(self):
        # Lista de colores para los labels
        color_to_bind = ["green", "red", "blue", "yellow"]
        #Lista de funciones para cada label
        functions_to_bind = [self.window_add_car, self.window_maintaince_car,
                             self.window_show_cars, self.window_exit_menu]

        # Se realiza el zip entre los textos y los colores, y después se realiza enumérate para el índice
        for index, (text, color, functions) in enumerate(zip(self.values_text, color_to_bind, functions_to_bind)):
            texts_labels_main = ct.CTkLabel(self, text=text, font=("Arial", 30))

            #Llamos a la función .bind para cambiar el color al pasar el mouse
            #Le pasamos la lista color_to_bind para cambiar los colores dinámicamente
            #c=color es un parametro de la función lambda
            texts_labels_main.bind("<Enter>", lambda e, c=color, widget=texts_labels_main: widget.configure(fg_color=c))
            texts_labels_main.bind("<Leave>", lambda e, c="transparent", widget=texts_labels_main: widget.configure(fg_color=c))

            # Agregamos .bind para llamar funciones de ventana
            texts_labels_main.bind("<Button-1>", lambda e, func=functions: func())
            texts_labels_main.grid(row=index, column=1, padx=10, pady=20, sticky="nsew")



#Esta es la clase principal de la ventana
class AppForm(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Servicio Automotriz")
        self.geometry("1000x600")
        self.resizable(False, False)

        #Creamos 2 filas para Frames principales
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=(0,1),weight=1)

        #Llamamos a la clase FrameTitle para crear el frame de la parte superior
        self.frame_title = FrameTitle(self)
        self.frame_title.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        #Llamamos a la clase FrameMain para crear el frame principal
        self.frame_main = FrameMain(self, ["Agregar Auto", "Reparar Auto",
                                           "Mostrar Autos", "Salir"])
        self.frame_main.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

app = AppForm()
app.mainloop()


