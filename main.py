import os
from palavraforca import palavra


if __name__ == "__main__":
    letras_usuario = []
    chances = 4
    ganhou = False

    while True:
        os.system("clear")
        print(palavra)
        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print(f"\nVoce tem {chances} chances")

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
        print(f"Parabens voce venceu a palara: {palavra}")
    else:
        print(f"Que pena voce perdeu a palara era: {palavra}")
