import customtkinter as ct
from PIL import Image, ImageTk
from db_script import DataBase
from tkinter import filedialog

class Registro(ct.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.db = DataBase()

        self.title("Registro")
        self.geometry("800x650")
        self.resizable(False, False)

        self.foto_path = "Coche2.png"

        self.configurar_grid()
        self.crear_frames()
        self.crear_widgets()

    def configurar_grid(self):
        self.grid_columnconfigure(0, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

    def crear_frames(self):
        self.titulo = ct.CTkFrame(self, border_width=2, fg_color="#041573")
        self.f1 = ct.CTkFrame(self, border_width=2, border_color="#041573")
        self.f2 = ct.CTkFrame(self, border_width=2, border_color="#041573")
        self.f3 = ct.CTkFrame(self, border_width=2, border_color="#041573")
        self.f4 = ct.CTkFrame(self, border_width=2, border_color="#041573")
        self.f5 = ct.CTkFrame(self, border_width=2, border_color="#041573")
        self.f6 = ct.CTkFrame(self, border_width=2, border_color="#041573")
        self.f7 = ct.CTkFrame(self, border_width=2, border_color="#041573")

        self.titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        self.f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        self.f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        self.f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        self.f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
        self.f5.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)
        self.f6.grid(row=6, column=0, sticky="nsew", pady=5, padx=5)
        self.f7.grid(row=7, column=0, sticky="nsew", pady=5, padx=5)

    def crear_widgets(self):
        # Labels
        ct.CTkLabel(self.titulo, text="Registro de usuario", text_color="White", font=("Book Antiqua", 35)).pack(padx=10, pady=10,side="left")
        ct.CTkLabel(self.f1, text="Nombre:", text_color="Black", font=("Book Antiqua",20)).pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f2, text="Apellido:", text_color="Black", font=("Book Antiqua",20)).pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f3, text="Email:", text_color="Black", font=("Book Antiqua",20)).pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f4, text="Password:", text_color="Black", font=("Book Antiqua",20)).pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f5, text="Verify Password:", text_color="Black", font=("Book Antiqua",20)).pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f6, text="Usuario:", text_color="Black", font=("Book Antiqua",20)).pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.titulo, text=" " , text_color="White", font=("Helvetica", 10)).pack(padx=10, pady=10, side="right")

        # Entradas de texto
        self.entrada_nombre = ct.CTkEntry(self.f1,placeholder_text="Fulanito Alberto",width=400, text_color="#041573")
        self.entrada_nombre.pack(padx=20, pady=5, side="right")
        self.entrada_nombre.bind("<FocusIn>")

        self.entrada_apellido = ct.CTkEntry(self.f2,placeholder_text="Alimaña Rodriguez",width=400)
        self.entrada_apellido.pack(padx=20, pady=5, side="right")

        self.entrada_email = ct.CTkEntry(self.f3,placeholder_text="Correo",width=400)
        self.entrada_email.pack(padx=20, pady=5, side="right")

        self.entrada_password = ct.CTkEntry(self.f4,placeholder_text="Juanito123@", show="*",width=400)
        self.entrada_password.pack(padx=20, pady=5, side="right")

        self.entrada_verify_password = ct.CTkEntry(self.f5, show="*",placeholder_text="Juanito123@",width=400)
        self.entrada_verify_password.pack(padx=20, pady=5, side="right")

        self.entrada_usuario = ct.CTkEntry(self.f6,placeholder_text="Juanito1",width=400)
        self.entrada_usuario.pack(padx=20, pady=5, side="right")

        #Photo implement

        try:
            self.foto_login = ct.CTkImage(
                light_image=Image.open(f"usuario.png"),
                dark_image=Image.open(f"usuario.png"),
                size=(100, 100)
            )
        except FileNotFoundError:
            print("Imagen no encontrada.")
            self.foto_login = None

        self.image_label = ct.CTkLabel(self.titulo, image=self.foto_login, text="") if self.foto_login else ct.CTkLabel(self, text="Sin imagen")
        self.image_label.pack(padx=5,pady=15,side="right")

        self.error_label = ct.CTkLabel(self.titulo,text=" ",font=("Helvetica",15),corner_radius=20)
        self.error_label.pack(side="right",padx=10, pady=10)


        # Botón de Registro
        self.boton_registrar = ct.CTkButton(self.f7, text="Registrar", command=self.registrar_usuario,fg_color="#041573",hover_color="#438713",text_color="white", font=("Book Antiqua", 15))
        #self.boton_registrar.grid(row=7, column=0, sticky="nsew", pady=5, padx=5)
        self.boton_registrar.pack(pady=10)


        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self)
        self.progress.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
        self.progress.set(0)  # Iniciar en 0

        # Eventos bind
        self.entrada_nombre.bind("<FocusIn>", self.on_focus_in_name)
        self.entrada_nombre.bind("<FocusOut>", self.on_focus_out_name)
        self.entrada_apellido.bind("<FocusIn>", self.on_focus_in_lastname)
        self.entrada_apellido.bind("<FocusOut>", self.on_focus_out_lastname)
        self.entrada_email.bind("<FocusIn>", self.on_focus_in_email)
        self.entrada_email.bind("<FocusOut>", self.on_focus_out_email)
        self.entrada_password.bind("<FocusIn>", self.on_focus_in_password)
        self.entrada_password.bind("<FocusOut>", self.on_focus_out_password)
        self.entrada_verify_password.bind("<FocusIn>", self.on_focus_in_password_v)
        self.entrada_verify_password.bind("<FocusOut>", self.on_focus_out_password_v)
        self.entrada_usuario.bind("<FocusIn>", self.on_focus_in_user)
        self.entrada_usuario.bind("<FocusOut>", self.on_focus_out_user)
        #KeyRealease user
        self.entrada_usuario.bind("<KeyRelease>",self.validar_usuario)

        #Photo
        self.image_label.bind("<Double-Button-1>",self.update_profile_picture)

        #Bind photo implement

        self.bind("<Return>", self.registrar_usuario)
        self.bind("<Shift_L>", self.on_show_in_password)
        self.bind("<Shift_R>", self.on_show_in_password)

        self.bind("<KeyRelease-Shift_L>", self.on_show_out_password)
        self.bind("<KeyRelease-Shift_R>", self.on_show_out_password)

    def start_loading(self):
        """Inicia la simulación de carga al iniciar sesión"""
        self.boton_registrar.configure(state="disabled")  # Deshabilitar botón
        self.progress.set(0)  # Reiniciar barra de progreso
        self.update_progress(0)  # Iniciar progreso

    def update_progress(self, value):
        """Simula el progreso y carga la nueva ventana"""
        if value < 1:
            value += 0.1  # Incremento del progreso
            self.progress.set(value)
            self.after(300, self.update_progress, value)  # Esperar 300ms y actualizar
        else:
            self.destroy()  # Abrir nueva ventana al llegar a 100%


    def on_log_error_entry(self,text_color="#d1cdcd",message="Todos los campos son obligatorios.",fg_color="#d94b43"):
        self.error_label.configure(text=message,text_color=text_color,fg_color=fg_color,corner_radius=20)

    def hide_label(self):
        self.error_label.configure(text="",fg_color="transparent") # Oculta el Label


    def on_focus_in_name(self, e):
        self.entrada_nombre.configure(text_color="#041573")
        self.error_label.configure(text=" Nombre de pila ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)

    def on_focus_out_name(self, e):
        self.entrada_nombre.configure(text_color="gray")

    def on_focus_in_lastname(self, e):
        self.entrada_apellido.configure(text_color="#041573")
        self.error_label.configure(text=" 1er y 2ndo Apellido ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)

    def on_focus_out_lastname(self, e):
        self.entrada_apellido.configure(text_color="gray")

    def on_focus_in_password(self, e):
        self.entrada_password.configure(text_color="#041573")
        self.error_label.configure(text=" Almenos un caracter especial ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_password(self, e):
        self.entrada_password.configure(text_color="gray")

    def on_focus_in_password_v(self, e):
        self.entrada_verify_password.configure(text_color="#041573")
        self.error_label.configure(text=" Verificar contraseña ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_password_v(self, e):
        self.entrada_verify_password.configure(text_color="gray")

    def on_show_in_password(self,event):
        self.entrada_password.configure(show="")
        self.entrada_verify_password.configure(show="")

    def on_show_out_password(self,event):
        self.entrada_password.configure(show="*")
        self.entrada_verify_password.configure(show="*")

    def on_focus_in_email(self, e):
        self.entrada_email.configure(text_color="#041573")
        self.error_label.configure(text=" Correo personal u institucional ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_email(self, e):
        self.entrada_email.configure(text_color="gray")

    def on_focus_in_user(self, e):
        self.entrada_usuario.configure(text_color="#041573")
        self.error_label.configure(text=" Nombre de usuario ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_user(self, e):
        self.entrada_usuario.configure(text_color="gray")

    def on_button_register(self, event):
        self.registro_win = Registro()
        self.registro_win.mainloop()


    def update_profile_picture(self, event):
        # Abrir explorador de archivos
        file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png")])
        self.foto_path = file_path #Guardar variable en clase para ser implementada en db

        if not file_path:
            return
        # Cargar la nueva imagen con PIL
        image = Image.open(file_path).resize((200, 200))  # Ajusta el tamaño según sea necesario
        self.foto_login_act = ct.CTkImage(light_image=image, dark_image=image, size=(100, 100))

        # Actualizar la imagen en el Label
        self.image_label.configure(image=self.foto_login_act)
        self.error_label.configure(text=f"Imagen Actualizada",text_color="black",fg_color="green")
        self.after(2000,self.hide_label)


    def validar_usuario(self, event):

        #Verificar en tiempo real si el usuario existe.
        user = self.entrada_usuario.get().strip()

        usuarios = self.db.obtain_user()
        if any(user == u[0] for u in usuarios):
            self.error_label.configure(text="Usuario ya registrado", text_color="white",fg_color="#f04735")
        else:
            self.error_label.configure(text="Disponible para registrar", text_color="white",fg_color="green")

    def registrar_usuario(self, event=None):
        nombre = self.entrada_nombre.get()
        apellido = self.entrada_apellido.get()
        password = self.entrada_password.get()
        email = self.entrada_email.get()
        usuario = self.entrada_usuario.get()
        verify_password = self.entrada_verify_password.get()
        foto_pefil = self.foto_path

        # Validaciones
        if not usuario or not password or not verify_password:
            self.on_log_error_entry()
            return

        if password != verify_password:
            self.on_log_error_entry(message="Las contraseñas no coinciden.",fg_color="#c9d134",text_color="black")
            self.after(1500,self.hide_label)
            return

        # Verificar si el usuario ya existe
        for u in self.db.get_users():
            if self.db.user_exists(u) == usuario:
                self.on_log_error_entry(message="El usuario ya existe.")
                self.after(1500, self.hide_label)
                return

        # Agregar usuario a la base de datos
        self.db.insert_user(nombre,apellido,email,usuario,password,foto=foto_pefil)
        self.on_log_error_entry(message=f" usuario {usuario} registrado correctamente.",fg_color="#5ccc58")
        self.start_loading()  # Cierra la ventana de registro

if __name__ == "__main__":
    app = Registro()
    app.mainloop()