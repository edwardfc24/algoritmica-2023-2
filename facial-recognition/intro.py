"""
1. Importamos las librerías necesarias para ejecutar OpenCV en nuestro computador
"""
import cv2

"""
2. Definir un capturador de imágenes, que trata de utilizar la cámara del dispositivo en el cuál se está trabajando. CV2 identifica las cámaras del dispositivo con un un
índice numérico, que al igual que los arreglos, inicia en 0 y aumenta en una unidad por cada cámara extra.
Podemos decir que la posición 0 es la cámara por defecto del dispositivo.
"""
NATIVE_CAMERA = 0
AUXILIAR_CAMERA = 1


if __name__ == '__main__':
    catcher = cv2.VideoCapture(NATIVE_CAMERA)
    while True:
        # El método read() nos devuelve el estado de la captura, seguido del frame capturado
        state, frame = catcher.read()
        # El siguiente método nos permite visualizar lo que el computador está viendo
        cv2.imshow('Hola OpenCV', frame)
        # Modificaciones de color en capa con la ayuda del método cvtColor
        gray_layer = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Escala de grises', gray_layer)
        hls_layer = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        cv2.imshow('HLS', hls_layer)
        # Para poder terminar la ejecución del programa de manera segura, se coloca la siguiente validación
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    """
    1. HAAR CASCADE CLASSIFIER: Basado en el reconocimiento de características según regiones
    Regiones en el rostro: https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/5_blog_image_6.png
    Aplicación en un rostro: https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/5_blog_image_7.png

    2. LBP CLASSIFIER: Basa su aplicación en un patrón llamado Local Binary Patern
    Recurso LBP bloques -> https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/5_blog_image_8.jpg
    Recurso LBP Explicación -> https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/5_blog_image_9.png
    Recurso LBP Histograma -> https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/5_blog_image_10.png
    Comparación entre modelos: https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/5_blog_image_12.png
    """
