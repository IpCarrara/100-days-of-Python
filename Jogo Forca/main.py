# Jogo de Forca

import random      # Possibilita utilizar o módulo aleatório
from lista_palavras import palavras
from hangman_art import stages, logo
import os          # Possibilita limpar o console depois de cada interação com o usuário

# Exibindo o logo
print(logo)

# Escolher a palavra aleatoriamente
palavra_correta = random.choice(palavras)

# Declarando variáveis
display = []
vidas = 6
letras_usadas = []

# Criando espaço para a palavra "_"
for letra in range(len(palavra_correta)):
    display += "_"
print("Qual a palavra?")
print(' '.join(display))
print(" ")

# Conferir se o input corresponde a uma letra da palavra
while palavra_correta != ''.join(display) and vidas > 0:
    inclui_letra = False
    # Pedir o input do usuário
    letra_usuario = input("Adivinhe uma letra: ").lower()
    print('')
    # Limpa o console depois de cada interação com o usuário
    os.system('cls')
    # Lógica para o usuário não repetir a mesma letra já usada
    if letras_usadas and letra_usuario in letras_usadas:
        print(f"Você já tentou a letra '{letra_usuario.upper()}'.\n")
        print(stages[vidas])
        print(' '.join(display))
        print('')
    else:
        # Lógica para conferir se a letra do usuário está na palavra
        for letra in range(len(palavra_correta)):
            if (palavra_correta[letra]) == letra_usuario:
                display[letra] = palavra_correta[letra]
                inclui_letra = True
        if inclui_letra == False:
            vidas -= 1
            print(f"\nNão tem a letra '{letra_usuario.upper()}' na palavra.\n")
            print(stages[vidas])
        else:
            print(stages[vidas])
        print(' '.join(display))
        print('')

    # Adicionar a letra às letras usadas
    letras_usadas.append(letra_usuario)

# Verificar se o jogador perdeu ou ganhou
if vidas == 0:
    print("\nVocê PERDEU!\n")
    print(f"A palavra correta é {palavra_correta.upper()}\n\n")
if palavra_correta == ''.join(display):
    print("\nVocê GANHOU!\n")
