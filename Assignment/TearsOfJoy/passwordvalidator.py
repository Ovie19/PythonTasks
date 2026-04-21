"""
Initialize correct_password to "python123"
Collect password from user
Initialize count to one

while user password is same as correct_password
    if count equal 3
        Display "Locked out"
        break out of loop
    if user password is same as correct_password
        Display "Wrong password"

    Collect password from user
    Initialize count to one
Else
    Display "Access Granted"

"""

correct_password = "python123"

user_password = input("Enter password: ")
count = 1

while correct_password != user_password:
    if count == 3:
        print("Locked out")
        break

    if correct_password != user_password:
        print("Password: wrong")
    user_password = input("Enter password: ")
    count += 1
else:
    print("Access Granted")