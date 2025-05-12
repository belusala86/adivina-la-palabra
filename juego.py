import random

def jugar_adivina_la_palabra():
    print("¡Juego iniciado!")  # Verificar si esto aparece
    palabras = ["gato", "perro", "casa", "arbol", "libro", "juego"]
    seguir_jugando = True

    while seguir_jugando:
        palabra = random.choice(palabras)
        letras_adivinadas = set()
        letras_ingresadas = set()
        vidas = 6 #controlar que resta las vidas

        print("\n¡A jugar el juego de adivinar la palabra!")
        print("¡Tienes 6 vidas. ¡Buena suerte!")

        while vidas > 0:
            mostrar = [letra if letra in letras_adivinadas else "-" for letra in palabra]
            print("Palabra: " + " ".join(mostrar))
            print(f"Letras ingresadas: {', '.join(sorted(letras_ingresadas))}")
            print(f"Vidas restantes: {vidas}")
            letra = input("Ingresa una letra: ").lower()

            letras_ingresadas.add(letra)

            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                vidas -= 1

            palabra_oculta = "".join([c if c in letras_adivinadas else "-" for c in palabra])
            print(palabra_oculta)

            if "-" not in palabra_oculta:
                print("¡Felicidades, adivinaste la palabra!")
                break

        if vidas == 0:
            print(f"Perdiste. La palabra era: {palabra}")

        respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if respuesta != "s":
            seguir_jugando = False


jugar_adivina_la_palabra()