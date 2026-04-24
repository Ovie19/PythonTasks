minutes = int(input("Enter minutes: "))

remaining_minutes = minutes % 60
total_hours = minutes // 60
remaining_hours = total_hours % 24
total_days = total_hours // 24

print(f"{total_days} days, {remaining_hours} hours, {remaining_minutes} minutes");
