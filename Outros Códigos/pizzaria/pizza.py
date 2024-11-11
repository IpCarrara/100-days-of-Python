print("Obrigado por escolher Python Pizza Deliveries!")
tamanho = input("Qual tamanho de pizza você deseja? P, M ou G")
adicionar_pepperoni = input("Você quer pepperoni? S ou N")
queijo_extra = input("Você quer queijo extra? S ou N")

conta = 0
if tamanho == "P":
    conta = 15
    if adicionar_pepperoni == "S":
        conta += 2
    if queijo_extra == "S":
        conta += 1
    print(f"Seu valor final é: R${conta}.")
elif tamanho == "M":
    conta = 20
    if adicionar_pepperoni == "S":
        conta += 3
    if queijo_extra == "S":
        conta += 1
    print(f"Seu valor final é: R${conta}.")
elif tamanho == "G":
    conta = 25
    if adicionar_pepperoni == "S":
        conta += 3
    if queijo_extra == "S":
        conta += 1
    print(f"Seu valor final é: R${conta}.")
else:
    print("ERRO")
