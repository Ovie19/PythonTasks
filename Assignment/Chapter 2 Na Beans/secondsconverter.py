total_seconds = int(input("Enter number of seconds: "))

remaining_seconds = total_seconds % 60
total_minutes = total_seconds // 60
remaining_minutes = total_minutes % 60
total_hours = total_minutes // 60

print(total_hours, "hour",  remaining_minutes, "minute", remaining_seconds, "second")
