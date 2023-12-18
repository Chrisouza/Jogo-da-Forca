import os
from palavraforca import palavra

DEBUG = False

if __name__ == "__main__":
    letras_usuario = []
    chances = 3
    ganhou = False

    while True:
        os.system("clear")

        if DEBUG:
            print(palavra)

        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print(f"\nVocê tem {chances} chances")

        tentativa = input("Escolha uma letra para adivinhar: ")
        letras_usuario.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():
            chances -= 1

        ganhou = True
        for letra in palavra:
            if letra.lower() not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f"Parabéns você venceu a palavra era: {palavra}")
    else:
        print(f"Que pena você perdeu a palavra era: {palavra}")
