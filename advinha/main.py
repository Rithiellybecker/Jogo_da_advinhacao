import random

def jogar():
   
    print("Bem-vindo ao Jogo da Adivinhação! ")
    print("Tente adivinhar o número secreto entre 1 e 100. Você tem 5 tentativas para acertar o número.")
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
            continue
        
        tentativas += 1
        
        if chute < numero_secreto:
            print(f"{chute}")
            print("Muito baixo. Tente novamente!")
        elif chute > numero_secreto:
            print(f"{chute}")
            print("Muito alto. Tente novamente!")
        else:
            print("Parabéns, você acertou!")
            break

    else:
        print(f"Acabaram as tentativas. O número era {numero_secreto}")

while True:
    jogar()
    resposta = input("Deseja jogar novamente? (s/n): ").lower()
    if resposta != 's':
        print("Obrigado por jogar! Até a próxima.")
        break

if __name__ == "__main__":
    jogar()