import constants
import re
import datetime

# Open file of games and format into dictionary
games = open(r"2019 Home Schedule")
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
        print("No change to schedule")
    else:
        print("Optimized Schedule From ")
        continue

    #print(startTime + constants.OFFSET) + " to " + (constants.OFFSET + range)
