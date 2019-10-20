import sys
import calculations
import re
import datetime

# Open file of games and format into dictionary
games = open(r"2019 Home Schedule.txt")
day = games.readline()
game_sched = dict()

while day:
    key = day[0:2] + day[3:5]
    game_sched[key] = (day[9:11] + day[12:14])
    day = games.readline()

games.close()

# Getting user input on date
date = None
while date != "exit":
    date = input("Date (MM/DD): ")
    if date.lower() == "exit":
        print("Bye! :)")
        break
    if not re.match(r"^[0-9]{2}[/][0-9]{2}", date):
        print("Invalid format")
        continue
    try:
        datetime.datetime(2019, int(date[0:2]), int(date[3:5]))
    except:
        print("Invalid date")
        continue
    date = date[0:2] + date[3:5]
    game_day = True if date in game_sched else False
    if not game_day:
        print("No Game: No change to schedule")
    else:
        start_time = game_sched[date]
        print("Game Day")
        print("Game Start Time: " + start_time[0:2] + ":" + start_time[2:4])
        date = datetime.datetime(2019, int(date[0:2]), int(date[2:4]))
        dow = date.weekday()
        numPass = "7,400"
        numTrain = "15"
        if dow in range (6):
            numTrain = "22"
            numPass = "10,500"
        print("Optimized Schedule: " + numTrain + " additional trains for " + numPass + " fans")
        calculations.calc_sched(date, start_time, dow)
        continue


