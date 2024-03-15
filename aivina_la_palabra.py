import random

def obtener_palabra_aleatoria():
    palabras = ["python", "programacion", "desafio", "computadora", "inteligencia", "algoritmo", "openai", "gpt"]
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jugar_juego():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = 7
    
    print("¡Bienvenido al juego de adivinanzas de palabras!")
    print("Adivina la palabra secreta.")
    print("Tienes 7 intentos para adivinar la palabra.")
    print("La palabra tiene", len(palabra_secreta), "letras.")

    while intentos_restantes > 0:
        palabra_oculta = mostrar_palabra_oculta(palabra_secreta, letras_adivinadas)
        print("Palabra:", palabra_oculta)
        print("Intentos restantes:", intentos_restantes)

        intento = input("Ingresa una letra o intenta adivinar la palabra completa: ").lower()
        
        if len(intento) == 1:
            if intento in letras_adivinadas:
                print("Ya has intentado esta letra. ¡Intenta con otra!")
            elif intento in palabra_secreta:
                print("¡Bien hecho! La letra está en la palabra.")
                letras_adivinadas.append(intento)
            else:
                print("La letra no está en la palabra. ¡Intenta de nuevo!")
                intentos_restantes -= 1
        elif len(intento) == len(palabra_secreta) and intento.isalpha():
            if intento == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra!")
                break
            else:
                print("Esa no es la palabra. ¡Intenta de nuevo!")
                intentos_restantes -= 1
        else:
            print("Entrada inválida. Por favor, ingresa una letra o intenta adivinar la palabra completa.")

    if intentos_restantes == 0:
        print("¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)

if "_main_":
    jugar_juego()