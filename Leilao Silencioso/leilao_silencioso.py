# Leilão Silencioso

import os
from art import logo

# Para limpar a tela, use: os.system('cls')

# Variável para controlar o loop
continuar = True

# Criando a lista de compradores
compradores = []

while continuar:
    # Exibindo o logo e solicitando as informações do usuário
    print(logo)
    print("Bem-vindo ao Leilão Silencioso.\n")
    
    nome = input("Qual é o seu nome? ")
    valor = float(input("Qual é o valor do seu lance? R$"))
    
    print("Há mais alguém para dar lance?")
    print("Digite 1 para SIM e 2 para NÃO.")
    
    proximo = int(input())

    # Criando o dicionário de cada comprador
    comprador = {
        "nome": nome,
        "valor": valor,
    }

    # Adicionando o comprador à lista
    compradores.append(comprador)

    # Condicional para continuar o leilão
    if proximo == 2:
        continuar = False
        # Verificando quem fez o maior lance
        maior_valor = 0
        maior_comprador = ""
        for pessoa in compradores:
            if pessoa["valor"] > maior_valor:
                maior_valor = pessoa["valor"]
                maior_comprador = pessoa["nome"]
        
        # Exibindo o resultado com duas casas decimais
        print(f"O ganhador foi {maior_comprador} que deu um lance de R${maior_valor:.2f}\n\n")
    else:
        # Limpando a tela para o próximo lance
        os.system('cls')
