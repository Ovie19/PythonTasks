"""
Collect name from user

while name is not empty
    Initialize count to zero
    Initialize total_score to zero
    Collect score from user
    While score is not equal to -1
        Add score to total_score
        Increase count by 1
        Collect score from user

    Compute average as total_score divided by count
    Display name and average
    Collect name from user
"""



name = input("Enter your name: ")

while name:
    count = 0
    total_score = 0
    score = int(input("Enter score or -1 to exit: "))
    while score != -1:
        total_score += score
        count += 1
        score = int(input("Enter score or -1 to exit: "))
    average = total_score / count
    print(f"{name}. Average: {average}\n")
    name = input("Enter your name: ")