# Librerias robustas
# librerias modelos predictivos
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
# librerias modelos clasificatorios
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# libreria para la gráfica del proyecto
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# libreria no robustas 
import pandas as pd
from pandastable import Table
# mide exactitud
from sklearn.metrics import accuracy_score
# evalua el margen de error
from sklearn.metrics import mean_squared_error, r2_score
# Libreria para el mapeo 
from sklearn.preprocessing import LabelEncoder

#import del archivo donde se alojan los modelos
from modelos import Modelos


# inicializo la clase
class VentanaPrincipal:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Cargar Dataset")
        self.root.geometry("780x650")
        self.dataframe = None
        self.table_columnas = None
        self.ventana_columnas = None
        self.columnaElejida = None
        #dfdfdfd

        # Creo el frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        self.table = Table(self.frame, showstatusbar=True, showtoolbar=True)
        self.table.show()

        # Botón para cargar el dataset
        cargar_btn = tk.Button(self.root, text="Cargar", bg="orange", command=self.cargar_dataset, width=20)
        cargar_btn.pack(pady=5)

        # Botón "Siguiente"
        siguiente_btn = tk.Button(self.root, text="Siguiente", bg="orange", command=self.abrir_ventana_siguiente, width=20)
        siguiente_btn.pack(pady=20)
        siguiente_btn.place(x=610, y=600)

        # Etiqueta "Limpieza de datos"
        limpieza = tk.Label(self.root, text="Limpieza de datos", font=("Arial", 12, "bold"))
        limpieza.pack(pady=5)

        # Botón "Mostrar datos"
        verdatos_btn = tk.Button(self.root, text="Mostrar datos", width=20, command=self.mostrar_info_columnas)
        verdatos_btn.pack(pady=5)

        # Botón "Realizar limpieza"
        limpieza_btn = tk.Button(self.root, text="Realizar limpieza", width=20, command=self.abrir_ventana_limpieza)
        limpieza_btn.pack(pady=5)
    
    #CARGAR EL DATASET
    def cargar_dataset(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.dataframe = pd.read_csv(file_path)
            self.mostrar_columnas()
        else:
            messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")

    #MUESTRA LAS COLUMNAS
    def mostrar_columnas(self):
        if self.dataframe is not None:
            self.table.model.df = self.dataframe #se le asigna el dataframe a la tabla 
            self.table.redraw()#redibujar la table
        else:
           messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")
    
    #AL DAR CLIC A MOSTRAR INFO COLUMNAS MUESTRA UNA VENTANA CON LOS TIPOS DE DATOS
    def mostrar_info_columnas(self):
        if self.dataframe is not None:
            info_columnas = self.dataframe.dtypes.reset_index()
            ventana_info = tk.Toplevel()
            ventana_info.title("Información de Columnas")
            ventana_info.geometry("400x300")

            info_text = tk.Text(ventana_info, height=17, width=50, bg="white", bd=2, relief=tk.SOLID, font=("Arial", 10))
            info_text.pack()

            for index, row in info_columnas.iterrows():
                info_text.insert(tk.END, f"{row['index']} - {row[0]}\n")   
        else:
            messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")
    
    #LIMPIEZAAAAAAAAAAAAAAAAA
    def abrir_ventana_limpieza(self):
        if self.dataframe is not None:
            ventana_limpieza = tk.Toplevel()
            ventana_limpieza.title("Opciones de Limpieza de Datos")
            ventana_limpieza.geometry("400x300")

            # Botón para eliminar columnas
            eliminar_columnas_btn = tk.Button(ventana_limpieza, text="Eliminar Columnas", width=20, command=self.abrir_ventana_eliminar_columnas)
            eliminar_columnas_btn.pack(pady=10)

            # Botón para mapear valores
            mapear_valores_btn = tk.Button(ventana_limpieza, text="Mapear Valores", width=20, command=self.abrir_ventana_mapear_valores)
            mapear_valores_btn.pack(pady=10)

            # Botón para rellenar valores nulos
            rellenar_valores_nulos_btn = tk.Button(ventana_limpieza, text="Rellenar Valores Nulos", width=20, command=self.abrir_ventana_rellenar_valores_nulos)
            rellenar_valores_nulos_btn.pack(pady=10)

            # Botón para verificar valores nulos
            verificar_nulos_btn = tk.Button(ventana_limpieza, text="Verificar Valores Nulos", width=20, command=self.verificar_valores_nulos,bg="orange")
            verificar_nulos_btn.pack(pady=10)
        else:
            messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")

    # Abrir ventana para eliminar columna seleccionada
    def abrir_ventana_eliminar_columnas(self):
        if self.dataframe is not None:
            ventana_eliminar_columnas = tk.Toplevel()
            ventana_eliminar_columnas.title("Eliminar Columna")
            ventana_eliminar_columnas.geometry("300x150")

            label_instruccion = tk.Label(ventana_eliminar_columnas, text="Seleccione la columna a eliminar:", font=("Arial", 10))
            label_instruccion.pack(pady=5)

            columnas = list(self.dataframe.columns)
            combobox_eliminar = ttk.Combobox(ventana_eliminar_columnas, values=columnas, width=30)
            combobox_eliminar.pack(pady=5)

            # Botón para confirmar la eliminación de la columna seleccionada
            confirmar_eliminar_btn = tk.Button(ventana_eliminar_columnas, text="Eliminar", width=15,
                                               command=lambda: self.eliminar_columna_seleccionada(combobox_eliminar.get(), ventana_eliminar_columnas))
            confirmar_eliminar_btn.pack(pady=5)
        else:
            messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")

    # Eliminar columna seleccionada del DataFrame
    def eliminar_columna_seleccionada(self, columna_seleccionada, ventana):
        if self.dataframe is not None and columna_seleccionada:
            self.dataframe.drop(columns=[columna_seleccionada], inplace=True)
            messagebox.showinfo("Información", f"Columna '{columna_seleccionada}' eliminada correctamente.")
            # Actualiza la visualización de las columnas después de la eliminación
            self.mostrar_columnas()
            ventana.destroy()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una columna válida.")
    
    # Abrir ventana para mapear valores en una columna
    def abrir_ventana_mapear_valores(self):
        #EJEMPLO
        #"female": "Femenino",
        # "male": "Masculino"
        if self.dataframe is not None:
            ventana_mapear_valores = tk.Toplevel()
            ventana_mapear_valores.title("Mapear Valores")
            ventana_mapear_valores.geometry("300x300")

            label_columna = tk.Label(ventana_mapear_valores, text="Seleccione la columna:", font=("Arial", 10))
            label_columna.pack(pady=5)

            columnas = list(self.dataframe.columns)
            combobox_columnas = ttk.Combobox(ventana_mapear_valores, values=columnas, width=30)
            combobox_columnas.pack(pady=5)

            label_mapeo = tk.Label(ventana_mapear_valores, text="Definir mapeo (valor original: valor a cambiar):", font=("Arial", 10))
            label_mapeo.pack(pady=5)

            texto_mapeo = tk.Text(ventana_mapear_valores, height=5, width=40)
            texto_mapeo.pack()

            # Botón para confirmar el mapeo de valores
            confirmar_mapeo_btn = tk.Button(ventana_mapear_valores, text="Mapear", width=15,
                                            command=lambda: self.mapear_valores(combobox_columnas.get(), texto_mapeo.get("1.0", tk.END), ventana_mapear_valores))
            confirmar_mapeo_btn.pack(pady=5)
        else:
            messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")

    # Mapear valores en una columna del DataFrame
    def mapear_valores(self, columna, mapeo, ventana):
        if self.dataframe is not None and columna and mapeo.strip():
            try:
                diccionario_mapeo = eval("{" + mapeo + "}")
                self.dataframe[columna] = self.dataframe[columna].map(diccionario_mapeo)
                messagebox.showinfo("Información", "Valores mapeados correctamente.")
                # Actualiza
                self.mostrar_columnas()
                ventana.destroy()
            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al mapear valores: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un mapeo válido.")
            ventana.destroy()

   # Abrir ventana para rellenar valores nulos en una columna
    def abrir_ventana_rellenar_valores_nulos(self):
        if self.dataframe is not None:
            ventana_rellenar_valores_nulos = tk.Toplevel()
            ventana_rellenar_valores_nulos.title("Rellenar Valores Nulos")
            ventana_rellenar_valores_nulos.geometry("300x150")

            label_columna = tk.Label(ventana_rellenar_valores_nulos, text="Seleccione la columna:", font=("Arial", 10))
            label_columna.pack(pady=5)

            columnas = list(self.dataframe.columns)
            combobox_columnas = ttk.Combobox(ventana_rellenar_valores_nulos, values=columnas, width=30)
            combobox_columnas.pack(pady=5)

            label_valor = tk.Label(ventana_rellenar_valores_nulos, text="Ingrese el valor de relleno:", font=("Arial", 10))
            label_valor.pack(pady=5)

            entry_valor = tk.Entry(ventana_rellenar_valores_nulos)
            entry_valor.pack()

            # Botón para confirmar el relleno de valores nulos
            confirmar_rellenar_btn = tk.Button(ventana_rellenar_valores_nulos, text="Rellenar", width=15,
                                            command=lambda: self.rellenar_valores_nulos(combobox_columnas.get(), entry_valor.get(), ventana_rellenar_valores_nulos))
            confirmar_rellenar_btn.pack(pady=5)
        else:
            messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")

    # Rellenar valores nulos en una columna del DataFrame
    def rellenar_valores_nulos(self, columna, valor_relleno, ventana):
        if self.dataframe is not None and columna and valor_relleno.strip():
            try:
                self.dataframe[columna].fillna(valor_relleno, inplace=True)
                messagebox.showinfo("Información", "Valores nulos rellenados correctamente.")
                # Actualizar la visualización de las columnas después del relleno de valores nulos
                self.mostrar_columnas()
                ventana.destroy()
            except Exception as e:
                messagebox.showwarning("Advertencia", f"Error al rellenar valores nulos: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Ingrese un valor de relleno válido.")
            ventana.destroy()

     # Verificar la existencia de valores nulos en el DataFrame
    def verificar_valores_nulos(self):
        if self.dataframe is not None:
            hay_nulos = self.dataframe.isnull().values.any()
            if hay_nulos:
                messagebox.showinfo("Información", "Existen valores nulos en el DataFrame.")
            else:
                messagebox.showinfo("Información", "No hay valores nulos en el DataFrame.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, carga un dataset primero.")

    #VENTANA NUEVA PARA ELEGIR VARIABLES X E Y
    def abrir_ventana_siguiente(self):
        if self.dataframe is None:
            messagebox.showinfo("Alerta", "Seleccione un DataFrame válido primero.")
            return

        if self.ventana_columnas is not None:
            self.ventana_columnas.destroy()
            self.ventana_columnas = None

        if self.table_columnas is not None:
            self.table_columnas.destroy()
            self.table_columnas = None

        self.ventana_columnas = tk.Toplevel(self.root)
        self.ventana_columnas.title("Seleccionar Columnas X e Y")
        self.ventana_columnas.geometry("800x700")

        self.frame_columnas = tk.Frame(self.ventana_columnas)
        self.frame_columnas.pack(expand=True, fill="both")

        self.table_columnas = Table(self.frame_columnas, showtoolbar=False, showstatusbar=True)
        self.table_columnas.show()
        self.table_columnas.model.df = self.dataframe
        self.table_columnas.redraw()

        # Label para la selección de X
        label_X = tk.Label(self.ventana_columnas, text="Seleccionar Variables X", font=("Arial", 12, "bold"))
        label_X.pack(pady=5)

        # Listbox para elegir variables X
        self.listbox_X = tk.Listbox(self.ventana_columnas, selectmode=tk.MULTIPLE, width=50, height=6)
        for column in self.dataframe.columns:
            self.listbox_X.insert(tk.END, column)
        self.listbox_X.pack(pady=5)

        # Label para la selección de Y
        label_Y = tk.Label(self.ventana_columnas, text="Seleccionar Variable Y", font=("Arial", 12, "bold"))
        label_Y.pack(pady=5)

        # Combobox para elegir la variable Y
        self.combobox_Y = ttk.Combobox(self.ventana_columnas, values=self.dataframe.columns, width=50)
        self.combobox_Y.pack(pady=5)

        # Botón siguiente
        siguiente_btn = tk.Button(self.ventana_columnas, text="Siguiente", bg="orange", command=self.mostrar_variables_seleccionadas, width=20)
        siguiente_btn.pack(pady=5)
        siguiente_btn.place(x=610, y=650)

    def mostrar_variables_seleccionadas(self):
        variables_X = self.listbox_X.curselection()
        variable_Y = self.combobox_Y.get()

        if variables_X and variable_Y:
            selected_X = [self.listbox_X.get(var) for var in variables_X]

            ventana_modelos = tk.Toplevel(self.root)
            ventana_modelos.title("Modelos")
            ventana_modelos.geometry("780x650")

            # Mostrar variables seleccionadas para X e Y
            label_variable_X = tk.Label(ventana_modelos, text=f"VARIABLES DE X: {', '.join(selected_X)}", font=("Arial", 16, "bold"))
            label_variable_X.place(x=50, y=30)

            label_variable_Y = tk.Label(ventana_modelos, text=f"VARIABLE DE Y: {variable_Y}", font=("Arial", 16, "bold"))
            label_variable_Y.place(x=50, y=60)

            # Textos para los modelos
            modelo_predictivo_label = tk.Label(ventana_modelos, text="Modelo predictivo:", font=("Arial", 12, "bold"))
            modelo_predictivo_label.place(x=50, y=120)

            modelo_clasificatorio_label = tk.Label(ventana_modelos, text="Modelo clasificatorio:", font=("Arial", 12, "bold"))
            modelo_clasificatorio_label.place(x=50, y=190)

            # Botones para modelos predictivos y clasificatorios
            btn_linear_regression = tk.Button(ventana_modelos, text="LinearRegression", width=15)
            btn_linear_regression.place(x=50, y=150)

            btn_ridge = tk.Button(ventana_modelos, text="Ridge", width=15)
            btn_ridge.place(x=190, y=150)

            btn_lasso = tk.Button(ventana_modelos, text="Lasso", width=15)
            btn_lasso.place(x=330, y=150)

            # Botones para modelos clasificatorios
            btn_kneighbors = tk.Button(ventana_modelos, text="KNeighbors", width=15, command=self.entrenar_kneighbors)
            btn_kneighbors.place(x=50, y=220)

            btn_decision_tree = tk.Button(ventana_modelos, text="DecisionTree", width=15)
            btn_decision_tree.place(x=190, y=220)

            btn_random_forest = tk.Button(ventana_modelos, text="RandomForest", width=15)
            btn_random_forest.place(x=330, y=220)

        else:
            messagebox.showwarning("Advertencia", "Seleccione al menos una variable para X y una variable para Y.")
    
   # def llamar_modelos(self):
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()