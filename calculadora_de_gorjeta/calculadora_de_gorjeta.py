# Calculadora de Gorjeta

# Solicita o valor da conta, a porcentagem da gorjeta e o número de pessoas
print("\nCalculadora de Gorjeta\n")
valor_conta = input("Qual é o valor da conta? R$ ")
por_gorjeta = input("Qual é a porcentagem da gorjeta? ")
quantas_pessoas = input("Quantas pessoas dividirão a conta? ")

# Calcula o valor da gorjeta e o total da conta com a gorjeta incluída
porcentagem = float(por_gorjeta) / 100
valor_gorjeta = float(valor_conta) * porcentagem
valor_total_com_gorjeta = float(valor_conta) + valor_gorjeta
total_a_pagar_p_pessoa = valor_total_com_gorjeta / int(quantas_pessoas)

# Exibe o valor que cada pessoa deve pagar
print(f"\nO valor por pessoa com gorjeta é: R${round(total_a_pagar_p_pessoa, 2)}\n")
