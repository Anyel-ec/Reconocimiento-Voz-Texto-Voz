import speech_recognition as sr
import pyttsx3

# Inicializamos el reconocedor de voz
r = sr.Recognizer()

# Inicializamos el motor de texto a voz
engine = pyttsx3.init()

# Función para obtener la entrada de voz del usuario
def obtener_entrada():
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
    return r.recognize_google(audio, language='es-ES')    

# Función principal del asistente de voz
def asistente_de_voz():
    while True:
        print("¿En qué puedo ayudarte?")
        entrada = obtener_entrada()

        if "saludos" in entrada:
            print("¡Hola!")
            engine.say("¡Hola!")
            engine.runAndWait()
        
        elif "despedir" in entrada:
            print("Hasta luego")
            engine.say("Hasta luego")
            engine.runAndWait()
        elif "contar" in entrada:
            print("1, 2, 3, 4, 5")
            engine.say("1, 2, 3, 4, 5")
            engine.runAndWait()
        elif "salir" in entrada:
            print("Adiós")
            engine.say("Adiós")
            engine.runAndWait()
            exit()
        else:
            print("No entendí la opción")
            engine.say("No entendí la opción")
            engine.runAndWait()
       

# Ejecutamos el asistente de voz
asistente_de_voz()
