ano = int(input("\nDigite um ano para saber se ele é Bisexto: "))

if ano % 400 == 0:  # Verificando primeiro se é divisível por 400
    print(f"\nO {ano} é Bissexto\n")
elif ano % 4 == 0 and ano % 100 != 0:  # Se for divisível por 4, mas não por 100
    print(f"\nO {ano} é Bissexto\n")
else:
    print(f"\nO {ano} não é Bissexto\n")