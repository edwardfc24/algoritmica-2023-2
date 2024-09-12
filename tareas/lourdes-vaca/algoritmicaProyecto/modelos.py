import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from pandastable import Table
# librerias modelos predictivos
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
# librerias modelos clasificatorios
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


from codigoProyecto import  VentanaPrincipal
class Modelos:
    #constructor
    
    
    #predictivo 
    def linear_modelo(self):
        # Obtener los índices de las variables seleccionadas en la Listbox para X
            indices_X = self.listbox_X.curselection()

        # Obtener el valor real de las variables seleccionadas en X
            selected_X = [self.listbox_X.get(index) for index in indices_X]

            variable_Y = self.combobox_Y.get()

            if selected_X and variable_Y:
                X = self.dataframe[selected_X]
                y = self.dataframe[variable_Y]

            # Dividir el conjunto de datos en entrenamiento y prueba
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Inicializar el clasificador KNeighbors
                linear_model = LinearRegression()

            # Entrenar el modelo
                linear_model.fit(X_train, y_train)

            # Realizar predicciones en el conjunto de prueba
                y_pred = linear_model.predict(X_test)

            # Calcular la precisión del modelo
                accuracy = accuracy_score(y_test, y_pred)

            # Mostrar precisión en una ventana emergente
                messagebox.showinfo("Precisión del Modelo", f"La precisión del modelo linearRegression es: {accuracy:.2f}")
            else:
                messagebox.showwarning("Advertencia", "Seleccione al menos una variable para X y una variable para Y.")
                
                
    def ridge_modelo(self):
        # Obtener los índices de las variables seleccionadas en la Listbox para X
        indices_X = self.listbox_X.curselection()

        # Obtener el valor real de las variables seleccionadas en X
        selected_X = [self.listbox_X.get(index) for index in indices_X]

        variable_Y = self.combobox_Y.get()

        if selected_X and variable_Y:
            X = self.dataframe[selected_X]
            y = self.dataframe[variable_Y]

            # Dividir el conjunto de datos en entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Inicializar el clasificador KNeighbors
            ridge_model = Ridge()

            # Entrenar el modelo
            ridge_model.fit(X_train, y_train)

            # Realizar predicciones en el conjunto de prueba
            y_pred = ridge_model.predict(X_test)

            # Calcular la precisión del modelo
            accuracy = accuracy_score(y_test, y_pred)

            # Mostrar precisión en una ventana emergente
            messagebox.showinfo("Precisión del Modelo", f"La precisión del modelo ridge es: {accuracy:.2f}")
        else:
            messagebox.showwarning("Advertencia", "Seleccione al menos una variable para X y una variable para Y.")
    
        def lasso_modelo(self):
        # Obtener los índices de las variables seleccionadas en la Listbox para X
            indices_X = self.listbox_X.curselection()

        # Obtener el valor real de las variables seleccionadas en X
            selected_X = [self.listbox_X.get(index) for index in indices_X]

            variable_Y = self.combobox_Y.get()

            if selected_X and variable_Y:
                X = self.dataframe[selected_X]
                y = self.dataframe[variable_Y]

            # Dividir el conjunto de datos en entrenamiento y prueba
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Inicializar el clasificador KNeighbors
                lasso_model = Lasso()

            # Entrenar el modelo
                lasso_model.fit(X_train, y_train)

            # Realizar predicciones en el conjunto de prueba
                y_pred = lasso_model.predict(X_test)

            # Calcular la precisión del modelo
                accuracy = accuracy_score(y_test, y_pred)

            # Mostrar precisión en una ventana emergente
                messagebox.showinfo("Precisión del Modelo", f"La precisión del modelo Lasso es: {accuracy:.2f}")
            else:
                messagebox.showwarning("Advertencia", "Seleccione al menos una variable para X y una variable para Y.")
    
    def kneighbors_modelo(self):
        # Obtener los índices de las variables seleccionadas en la Listbox para X
            indices_X = self.listbox_X.curselection()

        # Obtener el valor real de las variables seleccionadas en X
            selected_X = [self.listbox_X.get(index) for index in indices_X]

            variable_Y = self.combobox_Y.get()

            if selected_X and variable_Y:
                X = self.dataframe[selected_X]
                y = self.dataframe[variable_Y]

            # Dividir el conjunto de datos en entrenamiento y prueba
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Inicializar el clasificador KNeighbors
                knn = KNeighborsClassifier()

            # Entrenar el modelo
                knn.fit(X_train, y_train)

            # Realizar predicciones en el conjunto de prueba
                y_pred = knn.predict(X_test)

            # Calcular la precisión del modelo
                accuracy = accuracy_score(y_test, y_pred)

            # Mostrar precisión en una ventana emergente
                messagebox.showinfo("Precisión del Modelo", f"La precisión del modelo KNeighbors es: {accuracy:.2f}")
            else:
                messagebox.showwarning("Advertencia", "Seleccione al menos una variable para X y una variable para Y.")        
        
    def tree_modelo(self):
        # Obtener los índices de las variables seleccionadas en la Listbox para X
            indices_X = self.listbox_X.curselection()

        # Obtener el valor real de las variables seleccionadas en X
            selected_X = [self.listbox_X.get(index) for index in indices_X]

            variable_Y = self.combobox_Y.get()

            if selected_X and variable_Y:
                X = self.dataframe[selected_X]
                y = self.dataframe[variable_Y]

            # Dividir el conjunto de datos en entrenamiento y prueba
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Inicializar el clasificador KNeighbors
                tree_model = DecisionTreeClassifier()

            # Entrenar el modelo
                tree_model.fit(X_train, y_train)

            # Realizar predicciones en el conjunto de prueba
                y_pred = tree_model.predict(X_test)

            # Calcular la precisión del modelo
                accuracy = accuracy_score(y_test, y_pred)

            # Mostrar precisión en una ventana emergente
                messagebox.showinfo("Precisión del Modelo", f"La precisión del modelo TreeClasifier es: {accuracy:.2f}")
            else:
                messagebox.showwarning("Advertencia", "Seleccione al menos una variable para X y una variable para Y.")
                
    def forest_modelo(self):
        # Obtener los índices de las variables seleccionadas en la Listbox para X
            indices_X = self.listbox_X.curselection()

        # Obtener el valor real de las variables seleccionadas en X
            selected_X = [self.listbox_X.get(index) for index in indices_X]

            variable_Y = self.combobox_Y.get()

            if selected_X and variable_Y:
                X = self.dataframe[selected_X]
                y = self.dataframe[variable_Y]

            # Dividir el conjunto de datos en entrenamiento y prueba
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            # Inicializar el clasificador KNeighbors
                forest_model = KNeighborsClassifier()

            # Entrenar el modelo
                forest_model.fit(X_train, y_train)

            # Realizar predicciones en el conjunto de prueba
                y_pred = forest_model.predict(X_test)

            # Calcular la precisión del modelo
                accuracy = accuracy_score(y_test, y_pred)

            # Mostrar precisión en una ventana emergente
                messagebox.showinfo("Precisión del Modelo", f"La precisión del modelo RandomForest es: {accuracy:.2f}")
            else:
                messagebox.showwarning("Advertencia", "Seleccione al menos una variable para X y una variable para Y.")    
            
    #def predicciones:
    #def preparar_salida: