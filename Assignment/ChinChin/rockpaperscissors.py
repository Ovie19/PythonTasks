import random

computer_pick = random.randrange(3)

print("0. Scissors\n1. Rock\n2. Paper")
user_choice= int(input("Enter your choice: "))

if computer_pick == 0:
    if user_choice == 0:
        print("Computer picks Scissors")
        print("Draw!")
    elif user_choice == 1:
        print("Computer picks Scissors")
        print("You win!")
    elif user_choice == 2:
        print("Computer picks Scissors")
        print("Computer wins!")
elif computer_pick == 1:
    if user_choice == 0:
        print("Computer picks Rock")
        print("Computer wins!")
    elif user_choice == 1:
        print("Computer picks Rock")
        print("Draw!")
    elif user_choice == 2:
        print("Computer picks Rock")
        print("You win!")
else:
    if user_choice == 0:
        print("Computer picks Paper")
        print("You win!");
    elif user_choice == 1:
        print("Computer picks Paper")
        print("Computer wins!")
    elif user_choice == 2:
        print("Computer picks Paper")
        print("Draw!")
