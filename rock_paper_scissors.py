import random

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

#Write your code below this line 👇
choices = [rock, paper, scissors]
user_prompt = int(input(f"choose 1 for rock, 2 for paper, 3 for scissors\n"))
user_choice = choices[user_prompt -1]
print(f"You choose {user_choice}")

print("The computer chooses...")
computer_choice = random.choice([rock, paper, scissors])
print(computer_choice)

if user_choice == rock and computer_choice == paper:
  print("You loose - Paper wraps rock")
elif user_choice == paper and computer_choice  == scissors:
  print("You loose - Scissor cuts paper")
elif user_choice == scissors and computer_choice == rock:
  print("You loose - Rock crushes scissors")
elif user_choice == computer_choice:
  print("It's a draw")
else:
  print("You win!")
