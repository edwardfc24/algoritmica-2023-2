from recognition import RecognitionFunctions

if __name__ == '__main__':
    recognition_functions = RecognitionFunctions()
    # Procedemos a capturar data
    #recognition_functions.take_photos('FlaviaNogales')
    #recognition_functions.fit()
    recognition_functions.predict(camera=1)