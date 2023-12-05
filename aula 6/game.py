from random import choice

item = ("pedra", "papel", "tesoura")

escolha = input("escolha entre: pedra, papel ou tesoura: ").lower()

computador = choice(item).lower()
print(computador)

if escolha == "pedra" and computador == "papel":
    print("você perdeu")
elif escolha == "pedra" and computador == "tesoura":
    print("você ganhou")
elif escolha == "pedra" and computador == "pedra":
    print("EMPATE")
elif escolha == "papel" and computador == "pedra":
    print("você ganhou")
elif escolha == "papel" and computador == "tesoura":
    print("você perdeu")
elif escolha == "papel" and computador == "papel":
    print("EMPATE")
elif escolha == "tesoura" and computador == "papel":
    print("você ganhou")
elif escolha == "tesoura" and computador == "pedra":
    print("você perdeu")
elif escolha == "tesoura" and computador == "tesoura":
    print("EMPATE")

     












