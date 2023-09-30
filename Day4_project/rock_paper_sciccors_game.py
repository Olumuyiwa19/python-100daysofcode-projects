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
game_images = [rock, paper, scissors]

player_choice = int(input("Here you go. Go ahead and make your choice. Type 0 for Rock, 1 for Paper, and 2 for scissors \n"))

if player_choice >= 3 or player_choice < 0:
  print("You have made an invalid choice. Choose between 0,1,2 to continue.")
else:
  opponent_choice = random.randint(0,2)
  print("\nYou chose:")
  print(game_images [player_choice])
  print("\nOpponent chose:")
  print(game_images [opponent_choice])

  if player_choice == opponent_choice:
    print("\nIt's a draw!\n")
  elif (
        (player_choice == 0 and opponent_choice == 2) or
        (player_choice == 1 and opponent_choice == 0) or
        (player_choice == 2 and opponent_choice == 1)
    ):
    print("\nYou win!\n")
  elif (
        (opponent_choice > player_choice) or
        (opponent_choice == 0 and player_choice == 2)
    ):
    print("\nYou lose!\n")

print("Thanks for playing!")