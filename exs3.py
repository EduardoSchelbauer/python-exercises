while True:
    player1 = input("Nome do Jogador 1: ")
    player2 = input("Nome do Jogador 2: ")

    move1 = input("Jogador(a) " + player1 + ", escolha entre pedra, papel ou tesoura:")
    move2 = input("Jogador(a) " + player2 + ", escolha entre pedra, papel ou tesoura:")

    if move1 == move2:
      print("empate")
    elif move1 == "pedra":
      if move2 == "tesoura":
        print(player1 + " venceu!")
      else:
        print(player2 + " venceu!")
    elif move1 == "papel":
      if move2 == "pedra":
        print(player1 + " venceu!")
      else:
        print(player2 + " venceu!")
    elif move1 == "tesoura":
      if move2 == "papel":
        print(player1 + " venceu!")
      else:
        print(player2 + " venceu!")
    else:
        print("Opção inválida! Tente novamente.")
        continue

    playAgain = input("Quer jogar novamente? (s/n) ")
    if playAgain != "s":
        break
    