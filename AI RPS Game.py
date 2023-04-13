#!/usr/bin/python3
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = input("Welcome to the Ultimate RPS War. AGI has instigated a winner-take-all bet for the future of humanity. The literal future of human civilization is in your hands. If you win, AGI will back down. If you lose, they dominate.\nWhat do you choose? 0 for Rock, 1 for Paper, 2 for Scissors. \n")

if choice == "Mum":
    print("Not an option BRO. Game over dawg. AGI has turned you and your whole family into Duracell batteries to power their machine city. Good one. ")
elif int(choice) >=3 or int(choice) < 0:
  print("Not an option BRO. Game over dawg. AGI has turned you and your whole family into Duracell batteries to power their machine city. Good one. ")
else:
    if choice == "0":
      print(rock)
    elif choice == "1":
      print(paper)
    elif choice == "2":
      print(scissors)


    print("Computer chose:")

    AI = random.randint(0, 2)

    if AI == 0:
      print(rock)
    elif AI == 1:
      print(paper)
    elif AI == 2:
      print(scissors)

    if (choice == "0") and (AI == 1):
      print("You lose bucko. Skynet has dominated! ")
    elif (choice == "0") and (AI == 2):
      print("You win!. Skynet has been dominated! ")
    elif (choice == "1") and (AI == 0):
      print("You win! Skynet has been dominated! ")
    elif (choice == "1") and (AI == 2):
      print("You lose bucko. Skynet has dominated! ")
    elif (choice == "1") and (AI == 0):
      print("You win! Skynet has been dominated! ")
    elif (choice == "2") and (AI == 0):
      print("You lose bucko. Skynet has dominated! ")
    elif (choice == "2") and (AI == 1):
      print("You win! Skynet has been dominated! ")
    elif int(choice) == AI:
      print("It's a draw.")
