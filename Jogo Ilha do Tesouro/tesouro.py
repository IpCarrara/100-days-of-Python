print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo à Ilha do Tesouro")
print("Sua missão é encontrar o tesouro escondido\n")
print("Você é um aventureiro que ouviu falar de um tesouro lendário escondido em uma ilha misteriosa. Após semanas navegando, finalmente chega ao local. Diante de você, há uma praia deserta com uma trilha que leva para o interior da ilha, cercada por árvores altas e um ar de mistério.\n")

print("Você decide, escolha a opção 1 ou 2:\n")
print("1. Seguir a trilha pela floresta, acreditando que o tesouro está escondido no coração da ilha.")
print("2. Explorar a praia, imaginando que pode haver pistas perto da costa.")
primeira_escolha = input()

if primeira_escolha == "1":
    print("Você avança pela trilha e, depois de caminhar por um tempo, se depara com uma encruzilhada. À esquerda, o caminho é coberto por uma névoa espessa e assustadora. À direita, há uma ponte que parece velha e frágil, sobre um rio.\n")
    print("Você decide, escolha a opção 1 ou 2:\n")
    print("1. Seguir pela névoa, arriscando enfrentar o desconhecido.")
    print("2. Atravessar a ponte, acreditando que ela ainda pode ser segura.")
    segunda_escolha = input()
    if segunda_escolha == "1":
        print("A névoa fica cada vez mais densa, dificultando sua visão. De repente, você encontra uma pedra gigante com símbolos antigos esculpidos nela. No chão, há dois itens: uma chave dourada e um pergaminho envelhecido.\n")
        print("Você decide, escolha a opção 1 ou 2:\n")
        print("1. Pegar a chave dourada, acreditando que ela abre o caminho para o tesouro.")
        print("2. Pegar o pergaminho, pensando que pode conter instruções valiosas.")
        terceira_escolha = input()
        if terceira_escolha == "1":
            print("Após enfrentar os desafios, você finalmente encontra uma sala secreta, no coração da ilha. Usando a chave dourada ou o mapa como guia, você consegue abrir um cofre antigo. Dentro dele, o tesouro lendário brilha intensamente – uma coleção de joias, artefatos mágicos e riquezas incontáveis. Você se torna famoso como o aventureiro que desvendou o mistério da ilha perdida.")
        else:
            print("Ao abrir o pergaminho, você descobre que ele contém um antigo ensinamento dos primeiros habitantes da ilha. O tesouro físico pode existir, mas o verdadeiro prêmio é o conhecimento escondido no texto, que lhe concede sabedoria ancestral. Ao sair da ilha, você percebe que esse conhecimento lhe permitirá alcançar coisas muito maiores do que qualquer riqueza material.")
                
    else:
        print("Você atravessa a ponte cuidadosamente, e do outro lado encontra uma pequena cabana abandonada. Dentro, há um mapa desgastado e um colar dourado brilhante sobre a mesa.\n")
        print("Você decide, escolha a opção 1 ou 2:\n")
        print("1. Pegar o mapa, acreditando que ele mostrará o caminho para o tesouro.")
        print("2. Pegar o colar, pensando que ele pode ser a chave para o segredo do tesouro.")
        terceira_escolha = input()
        if terceira_escolha == "1":
             print("Após enfrentar os desafios, você finalmente encontra uma sala secreta, no coração da ilha. Usando a chave dourada ou o mapa como guia, você consegue abrir um cofre antigo. Dentro dele, o tesouro lendário brilha intensamente – uma coleção de joias, artefatos mágicos e riquezas incontáveis. Você se torna famoso como o aventureiro que desvendou o mistério da ilha perdida.")
        else:
            print("O colar ou medalhão que você encontrou não contém riqueza, mas possui um poder secreto. Ao sair da ilha, você descobre que o artefato lhe concede proteção ou habilidades mágicas sutis, o que muda sua vida de maneira inesperada. Embora o tesouro permaneça fora de alcance, você sai da aventura mais forte e mais sábio.")
else:
    print("Você caminha pela praia e, depois de um tempo, encontra uma entrada de caverna escondida entre as pedras. A caverna parece profunda e escura, mas você sente que pode ser o caminho para o tesouro.\n")
    print("Você decide, escolha a opção 1 ou 2:\n")
    print("1. Entrar na caverna, confiando no seu instinto.")
    print("2. Continuar explorando a praia, pensando que pode haver outras pistas.")
    segunda_escolha = input()
    if segunda_escolha == "1":
        print("Dentro da caverna, você encontra um baú misterioso coberto de poeira. Ao lado dele, há uma inscrição avisando sobre uma maldição que protege o tesouro.\n")
        print("Você decide, escolha a opção 1 ou 2:\n")
        print("1. Abrir o baú, ignorando o aviso da maldição.")
        print("2. Deixar o baú e continuar explorando a caverna, buscando uma saída segura.")
        terceira_escolha = input()
        if terceira_escolha == "1":
            print("Ignorando os avisos, você abre o baú. Um vento frio e sombrio enche a sala, e você sente uma força maligna se libertar. O baú estava amaldiçoado, e ao abrir, você libertou a entidade que protegia o tesouro. O mundo ao seu redor começa a desmoronar, e, sem ter tempo para fugir, você é consumido pela maldição. O tesouro continua perdido para sempre.")
        else:
            print("O artefato que você encontrou lhe concede habilidades mágicas sutis, mudando sua vida de forma inesperada. Embora o tesouro físico permaneça fora de alcance, você sai da aventura mais sábio.")
