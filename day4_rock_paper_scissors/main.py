import random

# game rule -
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock
# source - https://wrpsa.com/the-official-rules-of-rock-paper-scissors/

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

print("Welcome to Rock paper scissors game !! \n")
print(rock+'\n'+paper+'\n'+scissors+'\n')
choice = int(input("what do you choose ? Type 0 for Rock, 1 for paper and 2 for scissor \n"))
if choice == 0:
    print(f"you have chosen  {rock}")
elif choice == 1:
    print(f"you have chosen  {paper}")
else :
    print(f"you have chosen {scissors}")

computer_choice = random.randrange(0,3)
print("computer's choice is -- > \n" )
if computer_choice == 0:
    print(f"computer have chosen  {rock}")
elif computer_choice == 1:
    print(f"computer have chosen  {paper}")
else :
    print(f"computer have chosen  {scissors}")
if computer_choice == choice :
    print("Game is drawn")
elif (computer_choice == 0 and choice == 2) or (computer_choice == 1 and choice == 0) or (computer_choice == 2 and choice == 1):
    print("You Lost")
else:
    print("Hurrey !! You WON")

