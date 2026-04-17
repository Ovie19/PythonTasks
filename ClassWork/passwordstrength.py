"""
Collect password from user
Initialize the length of user's password into password_length
if password_length is lesser than 8
    Display very weak
Else if password_length is equal to 8
    Display weak
Else if password_length is between 8 and 16
    Display strong
Else
    Display very strong
"""

password = input("Enter your password: ")
password_length = len(password)

if password_length < 8:
    print("Very weak")
elif password_length == 8:
    print("Weak")
elif password_length <= 16:
    print("Strong")
else:
    print("Very strong")
