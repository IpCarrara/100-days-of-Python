print("A Calculadora do Amor está calculando sua pontuação...")
nome1 = input("Qual é o seu nome? ")
nome2 = input("Qual é o nome da outra pessoa? ")

# Concatenando os nomes fornecidos e transformando tudo para letras minúsculas
nomes = nome1.lower() + nome2.lower()

# Declarando as palavras de referência
palavra_true = "true"
palavra_love = "love"
pontos_true = 0
pontos_love = 0

# Lógica para contar as letras de "true" nos nomes fornecidos
for letra in palavra_true:
    pontos = nomes.count(letra)
    pontos_true += pontos

# Lógica para contar as letras de "love" nos nomes fornecidos
for letra in palavra_love:
    pontos = nomes.count(letra)
    pontos_love += pontos

# Convertendo as pontuações para strings e concatenando
pontuacao_total_str = str(pontos_true) + str(pontos_love)

# Convertendo a pontuação concatenada de volta para inteiro
pontuacao_total_int = int(pontuacao_total_str)

# Lógica para apresentação do resultado ao usuário
if (pontuacao_total_int < 10) or (pontuacao_total_int > 90):
    print(f"Sua pontuação é {pontuacao_total_str}, vocês combinam como coca e mentos.")
elif (pontuacao_total_int > 40) and (pontuacao_total_int < 50):
    print(f"Sua pontuação é {pontuacao_total_str}, vocês estão bem juntos.")
else:
    print(f"Sua pontuação é {pontuacao_total_str}, Amor Perfeito!")
