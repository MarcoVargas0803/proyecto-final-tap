from tkinter.ttk import Treeview, Style
from sqlalchemy.orm import sessionmaker

from consult_AssistanceClasses import Assistant_consult
from consult_AssistanceClasses import Event_consult
from consult_AssistanceClasses import Assistance_consult
from ORM_classes import Assistance, engine
import customtkinter as ct
from AsisstantForm import AssistantForm
from Event_Form import EventForm

class AssistanceForm(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registro de asistencia")
        self.geometry("850x450")
        self.resizable(False, False)

        #self.personalized_font = tkfont.Font(family="SF-Pro-Rounded-Regular",size=10)

        #self.foto_path = "usuario.png"

        # Crear instancia de las clases de consulta
        self.assistant_consult = Assistant_consult()
        self.event_consult = Event_consult()
        self.assistance_consult = Assistance_consult()

        # Consultar todos los asistentes y eventos
        self.assistants = self.assistant_consult.get_all_assistants()
        self.events = self.event_consult.get_all_events()


        self.configurar_grid_main()
        self.frame_main_creation()
        self.configure_grid_frameMain()
        self.frametitle_creation()
        self.configurar_grid_tree()
        self.frameTree_creation()
        self.progress_bar_creation()
        self.bind_creation()



    def configurar_grid_main(self):
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0,weight=0)
        self.grid_rowconfigure(index=1,weight=1)

    def frame_main_creation(self):
        self.FrameMain = ct.CTkFrame(self, corner_radius=0, fg_color="#ffe5f0")
        self.frameTree = ct.CTkFrame(self, fg_color="#ffe5f0", corner_radius=0)
        self.FrameMain.grid(column=0, row=0, sticky="nsew")
        self.frameTree.grid(column=0, row=1, sticky="nsew")

    def configure_grid_frameMain(self):
        self.FrameMain.grid_columnconfigure(index=(0,1), weight=1)
        self.FrameMain.grid_rowconfigure(index=(0, 1,2), weight=1)

    def frametitle_creation(self):
        self.title_label = ct.CTkLabel(self.FrameMain, text_color="#121212", text="Registro de Asistencia", font=("Verdana", 30))
        self.title_label.grid(column=0,row=0,sticky="w", pady=10, padx =10,columnspan=2)

        #Combobox event
        self.select_event = ct.CTkComboBox(self.FrameMain, values=self.events,state="readonly",text_color="#171616",fg_color="#e0dede")
        self.select_event.grid(column=0,row=1,sticky="nsew",pady=10,padx=10)


        #Combobox assistant
        self.select_assistant = ct.CTkComboBox(self.FrameMain, values=self.assistants,state="readonly",text_color="#171616",fg_color="#e0dede")
        self.select_assistant.grid(column=1, row=1, sticky="nsew", pady=10, padx=10)

        #Register event label
        self.register_event_label = ct.CTkLabel(self.FrameMain,text="Registrar evento",font=("Helvetica",20),text_color="#121212",fg_color="#c999af",corner_radius=20,width=30, height= 30)
        self.register_event_label.grid(column=0, row= 2 , sticky="nsew", pady=10, padx=10)
        #Register assistant label
        self.register_assistant_label = ct.CTkLabel(self.FrameMain, text=" Registrar asistente ", font=("Helvetica", 20),
                                                text_color="#121212", fg_color="#c999af", corner_radius=20)
        self.register_assistant_label.grid(column=1, row=2, sticky="nsew", pady=10, padx=10)

    def configurar_grid_tree(self):
        self.frameTree.grid_rowconfigure(index=(0,1,2,3), weight=0)
        self.frameTree.grid_columnconfigure(index=(0,1), weight=1)

    def frameTree_creation(self):
        style = Style()
        style.configure("Custom.Treeview",
                        foreground="black",
                        background="lightgray",
                        font=('Helvetica', 12),
                        rowheight=25)
        style.map("Custom.Treeview",
                  background=[('selected', 'lightblue')],
                  foreground=[('selected', 'black')])
        self.tv = Treeview(self.frameTree, columns=("Columna1", "Columna2"),style="Custom.Treeview")


        self.tv.heading("#0", text="Id")
        self.tv.heading("Columna1", text="Event")
        self.tv.heading("Columna2", text="Num_asistencias")


        # Column tv configure
        self.tv.column("#0", width=2, minwidth=2, stretch=True)

        # tv.configure()
        self.tv.tag_configure('par', background='#302c2c', font=("Arial", 15), foreground="#4e585d")
        self.tv.tag_configure('impar', background='#28241c', font=("Arial", 15), foreground="#4e585d")

        self.tv.grid(column=0,row=0,sticky="nsew",columnspan=2)
        self.llenar_treeview()

        self.label_register = ct.CTkLabel(self.frameTree, text_color="#121212", text=" Registrar asistente ",
                                          font=("Helvetica", 15),fg_color="#fdcae7",corner_radius=20)
        self.view_list = ct.CTkLabel(self.frameTree, text_color="#121212", text=" Ver lista ",
                                          font=("Helvetica", 15),fg_color="#e3b1c8", corner_radius=20)

        self.label_message = ct.CTkLabel(self.frameTree, text="TEXTO DE PRUEBA ", font=("Helvetica", 15), corner_radius=20)


        self.label_register.grid(column=0, row=1, sticky="e", padx=20)
        self.view_list.grid(column=1,row=1,sticky="w",padx=20)
        self.label_message.grid(column=0,row=2,columnspan=2,sticky="nsew",padx=10)

    def llenar_treeview(self):
        # Limpiar el Treeview antes de cargar nuevos datos
        for row in self.tv.get_children():
            self.tv.delete(row)

        # Obtener todos los eventos y contar cuántos asistentes tienen
        eventos = self.event_consult.consult_all_events()
        for evento in eventos:
            asistencias_count = self.assistance_consult.count_by_event(evento.id_event)
            # Agregar la fila al Treeview
            self.tv.insert("", "end", text=evento.id_event, values=(evento.name_event, asistencias_count))

    def progress_bar_creation(self):
        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self.frameTree,progress_color="#c999af")
        self.progress.grid(column=0,row=3, padx=10, sticky="ew",columnspan=2)
        self.progress.set(0)  # Iniciar en 0

    def start_loading(self):
        """Inicia la simulación de carga al iniciar sesión"""
        #self.label_register.configure(state="disabled")  # Deshabilitar botón
        self.progress.set(0)  # Reiniciar barra de progreso
        self.update_progress(0)  # Iniciar progreso

    def update_progress(self, value):
        """Simula el progreso y carga la nueva ventana"""
        if value < 1:
            value += 0.1  # Incremento del progreso
            self.progress.set(value)
            self.after(300, self.update_progress, value)  # Esperar 300ms y actualizar
        else:
            self.llenar_treeview() #Actualiza el treeview


    def bind_creation(self):
        # Eventos bind
        self.label_register.bind("<Enter>",lambda e: self.on_focus_in(self.label_register,"Confirmar registro de asistencia"))
        self.label_register.bind("<Leave>",lambda e: self.on_focus_out(self.label_register))

        self.label_register.bind("<Button-1>", self.register_user)
        self.bind("<Return>", self.register_user)

        self.view_list.bind("<Enter>",lambda e: self.on_focus_in(self.view_list,"Ver lista de asistencia especifica"))
        self.view_list.bind("<Leave>",lambda e: self.on_focus_out(self.view_list))

        self.view_list.bind("<Button-1>", self.view_listWindow)

        #Register_event_label.bind
        self.register_event_label.bind("<Enter>",lambda e: self.on_focus_in(self.register_event_label," Registrar evento "))
        self.register_event_label.bind("<Leave>",lambda e: self.on_focus_out(self.register_event_label))
        #Register_event_label.bind ==> Modal Callback
        self.register_event_label.bind("<Button-1>",self.open_event_window)
        #Register_assistance_label.bind
        self.register_assistant_label.bind("<Enter>",lambda e: self.on_focus_in(self.register_assistant_label, " Registrar asistencia "))
        self.register_assistant_label.bind("<Leave>", lambda e: self.on_focus_out(self.register_assistant_label))
        #Register_event_label.bind ==> Modal Callback
        self.register_assistant_label.bind("<Button-1>",self.open_assistant_window)

    def display_selected(self):
        selected_event = self.select_event.get()
        selected_assistant = self.select_assistant.get()

        print(f"Evento seleccionado: {selected_event}")
        print(f"Asistente seleccionado: {selected_assistant}")

    def on_enter_label_in_register(self, event):
        self.label_register.configure(text_color="#121212")

    def on_leave_label_out_register(self, event):
        self.label_register.configure(text_color="#121212")

    def on_label_in_view_list(self,event):
        self.view_list.configure(text_color="#121212")

    def on_label_out_view_list(self,event):
        self.view_list.configure(text_color="#121212")

    def on_log_error_entry(self, text_color="#121212", message="Todos los campos son obligatorios."):
        self.label_message.configure(text=message, text_color=text_color, corner_radius=20)

    def hide_label(self):
        self.label_message.configure(text="", fg_color="transparent")  # Oculta el Label

    def on_focus_in(self, entry, message):
        entry.configure(text_color="#757575")
        self.label_message.configure(text=message, fg_color="lightgray", text_color="#171616")
        self.after(1500, self.hide_label)

    def on_focus_out(self, entry):
        entry.configure(text_color="#121212")

    def validate_user(self, event):
        # Verificar en tiempo real si el usuario existe.

        # usuarios = self.db.obtain_user()
        """if any(user == u[0] for u in usuarios):
            self.label_message.configure(text="Usuario ya registrado", text_color="white", fg_color="#f04735")
        else:
            self.label_message.configure(text="Disponible para registrar", text_color="white", fg_color="green")
"""
        print("Validar usuario")


    def view_listWindow(self,event=None):
        print("Funcionalidad en proceso")

    def open_event_window(self,event=None):
        modalEvent = EventForm()
        modalEvent.grab_set()  # Se asegura de que la ventana modal esté bloqueada
        modalEvent.wait_window()
        self.refresh_combobox()
        self.llenar_treeview()

    def open_assistant_window(self,event=None):
        modalAssistant = AssistantForm()
        modalAssistant.grab_set()  # Se asegura de que la ventana modal esté bloqueada
        modalAssistant.wait_window()
        self.refresh_combobox()
        self.llenar_treeview()

    def register_user(self, event=None):

        #Abrir sesión
        Session = sessionmaker(bind=engine)
        sesion = Session()

        # Obtener los datos seleccionados de los comboboxes
        evento_seleccionado = self.select_event.get()
        asistente_seleccionado = self.select_assistant.get()

        # Verificaciones de datos nulos
        if not evento_seleccionado or not asistente_seleccionado:
            self.label_message.configure(text="No debe de haber datos nulos")
            return  # Salir de la función si hay datos nulos

        event_id = self.event_consult.consult_by_name_for_id(evento_seleccionado)
        assistant_id = self.assistant_consult.consult_by_name_for_id(asistente_seleccionado)


        # Registrar la asistencia (esto depende de cómo esté definida la clase Assistance en tu ORM)
        nueva_asistencia = Assistance(event_id, assistant_id)
        sesion.add(nueva_asistencia)
        sesion.commit()

        print(f"Asistencia registrada para el asistente {asistente_seleccionado} en el evento {evento_seleccionado}")
        self.refresh_combobox()
        self.start_loading()

    def refresh_combobox(self):
        # Consultar los datos más recientes de los asistentes y eventos
        self.assistants = self.assistant_consult.get_all_assistants()
        self.events = self.event_consult.get_all_events()

        # Actualizar los valores de los ComboBox
        self.select_event.configure(values=self.events)
        self.select_assistant.configure(values=self.assistants)

        # Opcionalmente, reiniciar la selección actual (si lo deseas)
        self.select_event.set("")  # Si quieres que el ComboBox quede vacío
        self.select_assistant.set("")  # Si quieres que el ComboBox quede vacío


app = AssistanceForm()
app.mainloop()


