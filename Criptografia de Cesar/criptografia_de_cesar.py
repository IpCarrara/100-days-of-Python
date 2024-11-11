# Criptografia de Cesar

# Importa o logo do arquivo art_logo.py e exibe-o
from art_logo import logo_dois  
print(logo_dois)

# Expande o alfabeto para incluir letras maiúsculas, minúsculas, números e caracteres especiais
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:",.<>?/~` '

# Função para criptografar ou descriptografar um texto usando o Ciframento de César
def cesar_cipher(text, shift, direction):
    # Se a direção for 2, inverte o sentido do deslocamento (para descriptografar)
    if direction == "2":  
        shift = -shift

    # Garante que o valor do deslocamento esteja dentro do tamanho do alfabeto
    shift = shift % len(alphabet)

    # Lista para armazenar os caracteres do texto criptografado ou descriptografado
    resultado = []
    
    # Para cada letra no texto, aplica o deslocamento se for um caractere do alfabeto
    for letra in text:
        if letra in alphabet:
            # Calcula o novo índice com o deslocamento (shift) e garante que ele esteja dentro do alfabeto
            new_index = (alphabet.index(letra) + shift) % len(alphabet)
            resultado.append(alphabet[new_index])
        else:
            # Se não for um caractere do alfabeto, mantém o caractere original (ex.: espaços ou pontuação)
            resultado.append(letra)  

    # Exibe o texto final após o criptografamento ou descriptografamento
    print("\nO texto criptografado é:")
    print(''.join(resultado))
    print("")

# Loop principal do programa para continuar rodando até o usuário decidir sair
while True:
    # Solicita ao usuário qual operação deseja realizar: criptografar, descriptografar ou sair
    direction = input("Digite:\n 1 - Criptografar\n 2 - Descriptografar\n 0 - Sair\n\n")
    
    # Se o usuário digitar 0, sai do loop e termina o programa
    if direction == "0":
        print("Saindo do programa...")
        print("")
        break  # Sai do loop e termina o programa

    print("")
    
    # Solicita a mensagem a ser criptografada ou descriptografada
    text = input("Digite a mensagem:\n")
    print("")
    
    # Solicita o número de casas a serem movidas no deslocamento (shift)
    shift = int(input("Digite o número de casas a serem movidas\n"))

    # Chama a função para realizar o criptografamento ou descriptografamento com os parâmetros fornecidos
    cesar_cipher(text, shift, direction)
