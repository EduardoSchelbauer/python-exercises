import random

number = random.randint(1, 9)

while True:
  guess = input("Adivinhe o número selecionado: ")

  guess = int(guess)
  if number > guess:
    print("Tentativa maior que o número!")
  elif number < guess:
    print("Tentativa menor que o número!")
  else:
    print("Parabéns, você acertou!")

  if guess == "sair" or guess == number:
    break