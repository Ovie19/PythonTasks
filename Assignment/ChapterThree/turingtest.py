# Turing test

"""
Prompt user "what is your problem?"
Collect response from user

Prompt user "Have you had this problem before (yes or no) ?"
Collect answer from user

If answer is yes
    Display "Well, you have it again"

If answer is no
    Display "Well, you have it now"
"""

user_response = input("What is your problem? ")
user_answer = input("Have you had this problem before (yes or no)? ")

if user_answer == "yes":
    print("Well, you have it again")

if user_answer == "no":
    print("Well, you have it now")
