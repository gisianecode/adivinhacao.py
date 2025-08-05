import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.\n")

    while True:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute < 1 or chute > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if chute < numero_secreto:
                print("O número é maior.")
            elif chute > numero_secreto:
                print("O número é menor.")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
        except ValueError:
            print("Digite um n
