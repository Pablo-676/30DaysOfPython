"""Desafio 1: Jogo da Forca em Python
Objetivo:
Criar um jogo da forca clássico em Python, com funcionalidades básicas e jogabilidade simplificada.

Funcionalidades:

Palavra secreta: Escondida do jogador, pode ser carregada de um arquivo ou definida manualmente.
Tentativas: Número máximo de erros antes da derrota.
Feedback: Mostre as letras acertadas e incorretas durante o jogo.
Vitória/Derrota: Exiba mensagens informativas ao final do jogo."""


import pandas as pd

# Lê o arquivo CSV contendo uma lista de palavras e seleciona uma palavra aleatória
df = pd.read_csv('C:/Users/Pablo Vítor/Desktop/Scripts/30daysOfPython/palavras.csv')
word_to_guess = df.sample().iloc[0, 0]
word_to_guess = word_to_guess.lower()

# Inicializa o estado de jogo com 5 tentativas e uma lista vazia de letras usadas
num_attempts = 5
used_letters = []

# Exibe uma mensagem de boas-vindas e o comprimento da palavra
print(f"Bem vindo ao jogo da forca!\n"
      f"A palavra escolhida tem {len(word_to_guess)} letras.\n"
      f"Você tem {num_attempts} tentativas.\n")

# Inicializa a lista de opções com '_' para cada letra da palavra
options = ['_'] * len(word_to_guess)

# Loop principal do jogo
while num_attempts > 0 and '_' in options:
    # Solicita uma letra ao usuário
    user_letter = input("Digite uma letra: ").lower()

    # Verifica se a entrada é uma letra única
    if len(user_letter) == 1 and user_letter.isalpha():
        # Verifica se a letra já foi usada antes
        if user_letter not in used_letters:
            # Verifica se a letra está na palavra
            if user_letter in word_to_guess:
                # Atualiza a lista de opções com a letra correta
                for i, letter in enumerate(word_to_guess):
                    if letter == user_letter:
                        options[i] = letter
            else:
                # Decrementa o número de tentativas
                num_attempts -= 1

            # Adiciona a letra usada à lista de letras usadas
            used_letters.append(user_letter)

            # Exibe a lista de opções atualizada
            print(f"----------------- {''.join(options)} -----------------")

            # Verifica se o usuário venceu
            if '_' not in options:
                print("\nParabéns! Você venceu!")

    else:
        # Exibe uma mensagem de erro se a entrada não for uma letra única
        print("Digite apenas uma letra por vez.")

# Exibe uma mensagem de derrota se o usuário não adivinhou a palavra
if '_' in options:
    print(f"\n----------------- NÃO FOI DESSA VEZ! TENTE NOVAMENTE! ----------------- "
          f"----------------- A PALAVRA ERA '{word_to_guess}' -----------------")