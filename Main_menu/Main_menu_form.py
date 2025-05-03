import customtkinter as ct
from PIL import Image



class AssistanceForm(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Servicio Automotriz")
        self.geometry("850x450")
        self.resizable(False, False)

        #Creamos 2 filas para Frames principales
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=(0,1),weight=1)

        self.run_window()

    def run_window(self):
        self.configure_grid_title()
        self.frame_title_creation()
        self.configure_grid_frame_main()
        self.frame_main_creation()
        self.bind_creation()

    def open_images(self,path: str):
        try:
            image = ct.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(150, 70))
            return image
        except FileNotFoundError:
            print("imagen no encontrada")
            image = None
            return image

    def configure_grid_title(self):
        self.frame_title = ct.CTkFrame(self)
        self.frame_title.grid(column=0,row=0, sticky="nsew")
        self.frame_title.grid_columnconfigure(index=(0,1),weight=1)
        self.frame_title.grid_rowconfigure(index=0,weight=1)

    def frame_title_creation(self):
        image_main_title = self.open_images("logo_empresa.jpg")
        self.image_label_title = ct.CTkLabel(self.frame_title, image=image_main_title, text="") \
            if image_main_title else ct.CTkLabel(self.frame_title, text="Sin imagen")
        self.image_label_title.grid(row=0, column=0, sticky="nsew")

        self.text_label_title = ct.CTkLabel(self.frame_title,text="Servicio_Automotriz",font=("Arial",50))
        self.text_label_title.grid(column=1,row=0,sticky= "nsew",padx=10, pady=15)

    def configure_grid_frame_main(self):
        self.frame_main = ct.CTkFrame(self,border_color="white")
        self.frame_main.grid(column=0,row=1, sticky="nsew", pady=5)
        self.frame_main.grid_columnconfigure(index=(0,1), weight=1)
        self.frame_main.grid_rowconfigure(index=(0,1,2,3), weight=1)

    def frame_main_creation(self):
        #Imagenes
        image_main1 = self.open_images("imagen_main_1.png")
        image_main2 = self.open_images("imagen_main_2.png")
        image_main3 = self.open_images("imagen_main_3.png")
        image_main4 = self.open_images("imagen_main_4.png")

        self.image_label_main1= ct.CTkLabel(self.frame_main, image=image_main1,
                                             text="") if image_main1 else ct.CTkLabel(self.frame_main, text="Sin imagen")
        self.image_label_main1.grid(row=0, column=0, padx=5,pady=5, sticky="nsew")

        self.image_label_main2 = ct.CTkLabel(self.frame_main, image=image_main2,
                                             text="") if image_main2 else ct.CTkLabel(self.frame_main, text="Sin imagen")
        self.image_label_main2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.image_label_main3 = ct.CTkLabel(self.frame_main, image=image_main3,
                                             text="") if image_main3 else ct.CTkLabel(self.frame_main, text="Sin imagen")
        self.image_label_main3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        self.image_label_main4 = ct.CTkLabel(self.frame_main, image=image_main4,
                                             text="") if image_main4 else ct.CTkLabel(self.frame_main, text="Sin imagen")
        self.image_label_main4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")


        #Text_Label
        self.text_label_main1 = ct.CTkLabel(self.frame_main, text="Agregar Auto", font=("Arial",30))
        self.text_label_main1.grid(row=0,column=1, padx=10, pady=10, sticky = "nsew")
        self.text_label_main2 = ct.CTkLabel(self.frame_main, text="Realizar mantenimiento", font=("Arial",30))
        self.text_label_main2.grid(row=1,column=1, padx=10, pady=10, sticky = "nsew")
        self.text_label_main3 = ct.CTkLabel(self.frame_main, text="Mostrar Autos", font=("Arial",30))
        self.text_label_main3.grid(row=2,column=1, padx=10, pady=10, sticky="nsew")
        self.text_label_main4 = ct.CTkLabel(self.frame_main, text="Salir del programa", font=("Arial",30))
        self.text_label_main4.grid(row=3,column=1, padx=10, pady=10, sticky="nsew")

    def bind_change_color(self, widget, color_on_enter="blue", color_on_leave="transparent"):
        # Cambiar color al pasar el mouse
        widget.bind("<Enter>", lambda e: widget.configure(fg_color=color_on_enter))
        # Restaurar color al salir el mouse
        widget.bind("<Leave>", lambda e: widget.configure(fg_color=color_on_leave))

    def enter_add_car_window(self):
        pass

    def enter_repairing_window(self):
        pass

    def enter_show_cars_window(self):
        pass

    def exit_window(self):
        pass

    def bind_creation(self):
        # Cambiar color de text_label_main1
        self.bind_change_color(self.text_label_main1, color_on_enter="blue")

        # Cambiar color de text_label_main2
        self.bind_change_color(self.text_label_main2, color_on_enter="green")

        # Cambiar color de text_label_main3
        self.bind_change_color(self.text_label_main3, color_on_enter="orange")

        # Cambiar color de text_label_main4
        self.bind_change_color(self.text_label_main4, color_on_enter="red")

app = AssistanceForm()
app.mainloop()


