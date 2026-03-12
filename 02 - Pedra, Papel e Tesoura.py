Jogo = print(input("Vamos jogar pedra, papel e tesoura? Você começa "))

Jogador = ("Pedra", "Papel", "Tesoura")
Computador = ("Pedra", "Papel", "Tesoura")

for computador in Jogador:
    if ("Pedra" == "Pedra") or ("Papel" == "Papel") or ("Tesoura" == "Tesoura"):
        print("Você empatou!")
    elif ("Pedra" != "Tesoura") or ("Papel" != "Pedra") or ("Tesoura" != "Papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
