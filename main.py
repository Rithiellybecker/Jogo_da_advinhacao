import random

def jogar():
    print("Bem-vindo ao Jogo da Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limite_tentativas = 5

    while tentativas < limite_tentativas:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        if chute < 1 or chute > 100:
            print("O número deve estar entre 1 e 100.")
        elif chute < numero_secreto:
            print(f"{chute}")
            print("Muito baixo. Tente novamente!")
        elif chute > numero_secreto:
            print(f"{chute}")
            print("Muito alto. Tente novamente!")
        else:
            print("Parabéns, você acertou!")
            break
        tentativas += 1

    if tentativas == limite_tentativas and chute != numero_secreto:
        print(f"Acabaram as tentativas. O número era {numero_secreto}")

if __name__ == "__main__":
    jogar()