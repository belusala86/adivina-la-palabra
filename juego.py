# import random

# def jugar_adivina_la_palabra():
#     print("¡Juego iniciado!")  # Verificar si esto aparece
#     palabras = ["gato", "perro", "casa", "arbol", "libro", "juego"]
#     seguir_jugando = True

#     while seguir_jugando:
#         palabra = random.choice(palabras)
#         letras_adivinadas = set()
#         letras_ingresadas = set()
#         vidas = 6 #controlar que resta las vidas

#         print("\n¡A jugar el juego de adivinar la palabra!")
#         print("¡Tienes 6 vidas. ¡Buena suerte!")

#         while vidas > 0:
#             mostrar = [letra if letra in letras_adivinadas else "-" for letra in palabra]
#             print("Palabra: " + " ".join(mostrar))
#             print(f"Letras ingresadas: {', '.join(sorted(letras_ingresadas))}")
#             print(f"Vidas restantes: {vidas}")
#             letra = input("Ingresa una letra: ").lower()

#             letras_ingresadas.add(letra)

#             if letra in palabra:
#                 letras_adivinadas.add(letra)
#             else:
#                 vidas -= 1

#             palabra_oculta = "".join([c if c in letras_adivinadas else "-" for c in palabra])
#             print(palabra_oculta)

#             if "-" not in palabra_oculta:
#                 print("¡Felicidades, adivinaste la palabra!")
#                 break

#         if vidas == 0:
#             print(f"Perdiste. La palabra era: {palabra}")

#         respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
#         if respuesta != "s":
#             seguir_jugando = False


# jugar_adivina_la_palabra()# trabajo-grupal.py

import random #Se importa el módulo random para poder elegir una palabra aleatoria de una lista.

# Se define una lista de palabras posibles que el juego puede usar aleatoriamente.
palabras = ["manzana", "bicicleta", "guitarra", "elefante", "montaña", "pelota"]

#Se define la función principal del juego
def jugar(): 
    # Este bloque intenta abrir el archivo integrantes.txt y mostrar su contenido al inicio del juego.
    try:
        with open("integrantes.txt", "r", encoding="utf-8") as archivo:
            print("\n⭐⭐⭐INTEGRANTES DEL GRUPO⭐⭐⭐:")
            print(archivo.read())
            #Si no se encuentra el archivo, se muestra un mensaje de advertencia
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'integrantes.txt'.")

    palabra = random.choice(palabras)#Se elige una palabra aleatoria de la lista para que sea la palabra a adivinar.
    letras_adivinadas = [] #lista de letras correctas que el jugador ha adivinado
    letras_incorrectas = [] #lista de letras incorrectas que el jugador intentó.
    vidas = 6 #el número de intentos incorrectos permitidos (6).
    jugando = True #controla si el juego sigue activo
    
    
    #Mensaje inicial para el jugador. Se le dice cuántas letras tiene la palabra.
    print("\n🎮 ¡Bienvenidos al juego Adivina la palabra!")
    print(f"\nLa palabra tiene {len(palabra)} letras. Podés ingresar una letra o arriesgar la palabra completa.\n")
    
    #Inicia un bucle que se repite mientras jugando sea True
    while jugando:
        # Mostrar el estado actual de la palabra
        #Este bloque arma una cadena con guiones y letras adivinadas
        mostrar = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                mostrar += letra + " "
            else:
                mostrar += "_ "

        #Muestra el estado actual de la palabra, las vidas que quedan y las letras fallidas
        print("\nPalabra:", mostrar.strip())
        print("Vidas restantes:", vidas)
        print("Letras incorrectas:", ", ".join(letras_incorrectas))

        #Se pide al jugador que ingrese una letra o toda la palabra. 
        # Se convierte a minúscula con .lower() para evitar errores de mayúsculas
        entrada = input("➡️ Ingresá una letra o la palabra completa (o escribí 'salir' para rendirte): ").lower()

        # Opción para rendirse.Si el jugador escribe salir, se rinde. 
        # Se termina el juego y se muestra la palabra correcta
        if entrada == "salir":
            print(f"\n🫡 Te diste por vencido. La palabra era: {palabra}")
            break

        # Si arriesga la palabra completa
        # si acierta gana el juego si no pierde 2 vidas y pierde el juego
        if len(entrada) > 1:
            if entrada == palabra:
                print(f"\n🎉 ¡Increíble! Adivinaste la palabra completa: {palabra}")
                break
            else:
                print("❌ Esa no es la palabra. Perdés 2 vidas.")
                vidas -= 2
                if vidas <= 0:
                    print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra}")
                    break
                continue

        # Valida que la entrada sea una sola letra del abecedario.
        if len(entrada) != 1:
            print("⚠️ Solo podés ingresar **una letra** o arriesgar toda la palabra.")
            continue
        if not entrada.isalpha():
            print("⚠️ Solo se permiten letras.")
            continue
        if entrada in letras_adivinadas or entrada in letras_incorrectas:
            print("❗ Ya usaste esa letra. Probá con otra.")
            continue

        # Comprobación de la letra
        #Si la letra está en la palabra, se agrega a las letras adivinadas
        # si no está, se descuenta una vida y se guarda como incorrecta.
        if entrada in palabra:
            print("✅ ¡Bien! La letra está en la palabra.")
            letras_adivinadas.append(entrada)
        else:
            print("❌ Esa letra no está.")
            letras_incorrectas.append(entrada)
            vidas -= 1

        # ¿Ganó?--->Verifica si todas las letras de la palabra han sido adivinadas. Si sí, el jugador gana
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\n🎉 ¡Felicidades! Adivinaste la palabra: {palabra}")
            break

        # ¿Perdió?---->Si el jugador ya no tiene vidas, pierde el juego.
        if vidas <= 0:
            print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra}")
            break

    # ¿Volver a jugar?--->Al terminar una partida, se pregunta si quiere volver a jugar. 
    # Si dice que sí, se vuelve a llamar a jugar()
    respuesta = input("\n¿Querés jugar otra vez? (s/n): ").lower()
    if respuesta == "s":
        jugar()
    else:
        print("👋 Gracias por jugar. ¡Nos vemos!")
        
#Esta línea permite que el juego se ejecute cuando abrís el archivo directamente
# if __name__ == "__main__":
jugar()