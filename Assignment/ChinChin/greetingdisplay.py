hour = int(input("Enter the current hour (0 - 23): "))

if hour >= 5 and hour <= 11:
    print("Good Morning")
elif hour >= 12 and hour <= 17:
    print("Good Afternoon")
elif hour >= 18 and hour <= 21:
    print("Good Evening")
elif ((hour >= 22 and hour <= 23) or (hour >= 0 and hour <= 4)):
    print("Good Night")
else:
    print("Invalid response")