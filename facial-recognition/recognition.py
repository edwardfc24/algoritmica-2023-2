import cv2
import os
from PIL import Image
import numpy as np
import pickle as pc


class RecognitionFunctions:

    def __init__(self):
        self.IMAGE_DIR = 'images\\'
        self.NATIVE_CAMERA = 0
        self.AUXILIAR_CAMERA = 1

    def take_photos(self, folder_name, quantity=300, camera=0):
        catcher = cv2.VideoCapture(camera)
        # Ahora creamos la carpeta contenedora de las fotografias
        folder_path = self.IMAGE_DIR + folder_name
        os.mkdir(folder_path)
        counter = 1
        while True:
            # Obtenemos el  cuadro para almacenarlo
            state, frame = catcher.read()
            # Convertimos la imagen a escala de grises
            gray_layer = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Genero un nombre para el archivo
            filename = f'photo-{counter}.png'
            # Guardo el archivo
            cv2.imwrite(folder_path + '/' + filename, gray_layer)
            # Este paso es opcional, mostrar lo que ve la pc
            cv2.imshow('Capturando datos de entrenamiento', frame)
            counter += 1
            if counter > quantity:
                break
        cv2.destroyAllWindows()

    def fit(self):
        # Primero es inicializar nuestra Red Neuronal Clasificatoria
        cascade_classifier = cv2.CascadeClassifier(
            'cascades/haarcascade_frontalface_alt2.xml')
        # Inicializar un agente de reconocimiento
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        # Ahora trabajamos con la data proveniente de la imagen
        x_data = []
        y_data = []
        labels = {}  # {'EduardoFlores': 0, ....., 'JuanitoPerez':25}
        index = -1
        # Debemos obtener la información de la imagen
        for root, folders, files in os.walk(self.IMAGE_DIR):
            for image in files:
                if image.endswith('jpg') or image.endswith('png') or image.endswith('gif'):
                    # Obtenemos la imagen a procesar
                    # images/EduardoFlores/photo-1.png
                    path = os.path.join(root, image)
                    # Estandarizar los nombres
                    label = os.path.basename(root).replace(' ', '').upper()
                    if label not in labels:
                        index += 1
                        labels[label] = index
                    # Cargar la imagen para obtener un arreglo multidimensional numérico
                    # Convierto a escala aplicando el factor LUMA
                    image_bin = Image.open(path).convert('L')
                    image_resized = image_bin.resize((500, 500), Image.BICUBIC)
                    # Obtenemos el valor numérico de la imgarn convertida
                    image_np = np.array(image_resized, 'uint8')
                    # De estos valores numéricos, obtendremos x_data
                    face_detector = cascade_classifier.detectMultiScale(
                        image_np)
                    for x, y, width, height in face_detector:
                        # Definimos la región de interés
                        roi = image_np[y: y + height, x: x + width]
                        # Una vez tenemos nuestra región de interés, guardamos en x_data
                        x_data.append(roi)
                        # Almaceno el valor de y
                        y_data.append(index)
        # Serializamos la data para facilitar el entrenamiento posterior
        with open('pickles/face-labels.pickle', 'wb') as file:
            pc.dump(labels, file)
        # Guardamos los datos de entrenamiento en training
        recognizer.train(x_data, np.array(y_data))
        recognizer.save('training/face-training.yml')

    def predict(self, camera=0):
        # Primero es inicializar nuestra Red Neuronal Clasificatoria
        cascade_classifier = cv2.CascadeClassifier(
            'cascades/haarcascade_frontalface_alt2.xml')
        # Inicializar un agente de reconocimiento
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        # La lectura de los datos del agente de reconocimiento
        recognizer.read('training/face-training.yml')
        # Una vez recupero los datos, recuperamos las etiquetas
        labels = {}
        with open('pickles/face-labels.pickle', 'rb') as file:
            labels_deseriallized = pc.load(file)
            labels = {value: key for key, value in labels_deseriallized.items()}
        # Habilitamos el capturador
        catcher = cv2.VideoCapture(camera)
        font = cv2.FONT_HERSHEY_PLAIN
        color = (255, 0, 0)
        stroke = 1
        # while True:
        #     state, frame = catcher.read()
        #     # Convertimos a escalas
        #     gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #     # Recorremos los valores que nos devuelve el recognizer
        #     face_detector = cascade_classifier.detectMultiScale(gray_scale)
        #     for x, y, width, height in face_detector:
        #         roi = gray_scale[y: y + height, x: x + width]
        #         label, score = recognizer.predict(roi)
        #         if score >= 80 and score <= 100:
        #             name = labels[label]
        #             cv2.putText(frame, name, (x, y), font, stroke, color)
        #         cv2.rectangle(frame, (x, y), ((x + width), (y + height)), color, stroke)
        #     cv2.imshow('Detector de Algoritmica', frame)
        #     # Nos aseguramos de que podamos salir
        #     if cv2.waitKey(20) & 0xFF == ord('q'):
        #         break
        # cv2.destroyAllWindows()
        frame = cv2.imread('images\HanielHuayta\photo-1.png')
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        while True:
            # Recorremos los valores que nos devuelve el recognizer
            face_detector = cascade_classifier.detectMultiScale(gray_scale)
            for x, y, width, height in face_detector:
                roi = gray_scale[y: y + height, x: x + width]
                label, score = recognizer.predict(roi)
                if score >= 80 and score <= 100:
                    name = labels[label]
                    cv2.putText(frame, name, (x, y), font, stroke, color)
                cv2.rectangle(frame, (x, y), ((x + width), (y + height)), color, stroke)
            cv2.imshow('Detector de Algoritmica', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
