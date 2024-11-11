# Definindo as representações de Pedra, Papel e Tesoura
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Importando o módulo para gerar números aleatórios
import random

# Solicitando ao usuário que escolha uma opção
escolha_usuario = int(input("\nEscolha:\n 1 = Pedra\n 2 = Papel\n 3 = Tesoura\n\n"))

# Verificando se a escolha do usuário é válida (entre 1 e 3)
if escolha_usuario in range(1, 4):
    # Lista contendo as opções de jogo
    lista_opcoes = [pedra, papel, tesoura]
    
    # Gerando a escolha do computador (número aleatório entre 1 e 3)
    escolha_computador = random.randint(1, 3)
    
    # Exibindo a escolha do usuário e a escolha do computador
    print(f"\nUsuário:{lista_opcoes[escolha_usuario - 1]}")
    print(f"\nComputador:{lista_opcoes[escolha_computador - 1]}")
    
    # Lógica do jogo para determinar o vencedor
    if escolha_usuario == escolha_computador:
        print("EMPATE\n")
    elif (escolha_usuario == 1 and escolha_computador == 2) or \
         (escolha_usuario == 2 and escolha_computador == 3) or \
         (escolha_usuario == 3 and escolha_computador == 1):
        print("VOCÊ PERDEU!\n")
    else:
        print("VOCÊ GANHOU!!!\n")
else:
    # Caso o usuário insira uma opção inválida
    print("Digite um número válido.")
