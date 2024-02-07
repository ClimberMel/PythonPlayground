"""
Please write a program for recording the amount of time the user has spent in front of a television, 
computer or mobile device screen over a specific period of time.

The program should work as follows:

Sample output
Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
Please type in screen time in minutes on each day (TV computer mobile):
Screen time 24.06.2020: 60 120 0
Screen time 25.06.2020: 0 0 0
Screen time 26.06.2020: 180 0 0
Screen time 27.06.2020: 25 240 15
Screen time 28.06.2020: 45 90 5
Data stored in file late_june.txt

The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, representing minutes.

With the above input, the program should store the data in a file named late_june.txt. The contents should look like this:

Sample data
Time period: 24.06.2020-28.06.2020
Total minutes: 780
Average minutes: 156.0
24.06.2020: 60/120/0
25.06.2020: 0/0/0
26.06.2020: 180/0/0
27.06.2020: 25/240/15
28.06.2020: 45/90/5"""

from datetime import datetime, timedelta

startDt = datetime.now()
filename = "late_june.txt"
print(f"Filename: {filename}")
print(f"Starting date: {startDt.strftime('%d.%m.%Y')}")

days = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile):")
data = []
for day in range(days):
    dt = startDt + timedelta(days=day)
    dtStr = dt.strftime("%d.%m.%Y")
    st = input(f"Screen time {dtStr}: ")
    screen_time = list(map(int, st.split()))
    data.append(screen_time)

# Write to file
with open(filename, 'w') as f:
    f.write(f"Time period: {startDt.strftime('%d.%m.%Y')}-{(startDt + timedelta(days=days-1)).strftime('%d.%m.%Y')}\n")
    total_minutes = 0
    for i in range(days):
        daily_total = sum(data[i])
        total_minutes += daily_total
    average_minutes = total_minutes / days
    f.write(f"Total minutes: {total_minutes}\n")
    f.write(f"Average minutes: {average_minutes}\n")
    for i in range(days):
        f.write(f"{(startDt + timedelta(days=i)).strftime('%d.%m.%Y')}: {'/'.join(map(str, data[i]))}\n")

print(f"Data stored in file {filename}")