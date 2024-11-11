# Gerador de Senhas

# Importando a biblioteca random para gerar escolhas aleatórias
import random

# Listas de caracteres possíveis para a senha
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Exibindo mensagem inicial para o usuário
print("\nBem-vindo ao Gerador de Senhas PyPassword!\n")

# Solicitando ao usuário a quantidade de letras, números e símbolos que ele deseja na senha
nr_letras = int(input("Quantas letras você gostaria em sua senha? "))
nr_simbolos = int(input("Quantos símbolos você gostaria? "))
nr_numeros = int(input("Quantos números você gostaria? "))


# Lista para armazenar os componentes da senha
senha = []

# Adicionando letras aleatórias na senha
for letra in range(1, nr_letras + 1):
    senha.append(random.choice(letras))  # Escolhendo aleatoriamente uma letra da lista

# Adicionando símbolos aleatórios na senha
for simbolo in range(1, nr_simbolos + 1):
    simbolo = random.randint(0, len(simbolos) - 1)  # Escolhendo aleatoriamente um símbolo
    senha.append(simbolos[simbolo])

# Adicionando números aleatórios na senha
for numero in range(1, nr_numeros + 1):
    numero = random.randint(0, len(numeros) - 1)  # Escolhendo aleatoriamente um número
    senha.append(numeros[numero])


# Embaralhando a ordem dos caracteres na lista da senha
random.shuffle(senha)

# Exibindo a senha final com os caracteres em ordem aleatória
print(f"\nNova senha: {''.join(senha)}\n")
