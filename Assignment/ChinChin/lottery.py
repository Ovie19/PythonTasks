import random

lottery_number = random.randrange(100)
user_lucky_number = int(input("Enter your lucky number (0 - 99): "))

first_lottery_digit = lottery_number % 10;
second_lottery_digit = lottery_number / 10;

first_user_lottery_digit = user_lucky_number % 10;
second_user_lottery_digit = user_lucky_number / 10;

print("The lottery number is", lottery_number);
if lottery_number == user_lucky_number:
    print("Congratulations!!!\nYou have won $10000");
elif first_lottery_digit + second_lottery_digit == first_user_lottery_digit + second_user_lottery_digit:
    print("Congratulations!!!\nYou have won $3000");
elif first_lottery_digit == first_user_lottery_digit or first_lottery_digit == second_user_lottery_digit or second_lottery_digit == first_user_lottery_digit or second_lottery_digit == second_user_lottery_digit:
    print("Congratulations!!!\nYou have won $1000");
else:
    print("Try again!!!");
