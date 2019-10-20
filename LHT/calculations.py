# Takes constants and efficiency curve and adds together
# Recursively finds points of buses in minutes
import datetime
import math


def calc_sched(date, start_time):
    start_hrs = int(start_time[0:2])
    start_mins = int(start_time[2:4])
    start_time = int(start_time)
    date = datetime.datetime(2019, int(date[0:2]), int(date[2:4]))
    dow = date.weekday()
    time0day = "PM"
    currtime = 120
    while currtime <= 240:
        if dow in range(6):
            fanrate = 15 * math.exp(-((currtime - 187) * (currtime - 187)) / 3400)
            if (start_time + math.floor(currtime/60)*100 + currtime % 60) <= 730:
                regrate = 60 / 5.25
            else:
                regrate = 60 / 8.25
            totrate = fanrate + regrate
            traininterval = round(60 / totrate)
        elif dow == 6:
            fanrate = 10.2 * math.exp(-(currtime - 180) * (currtime - 193) / 3280)
            if (start_time + math.floor(currtime / 60) * 100 + currtime % 60) <= 630:
                regrate = 60 / 6
            else:
                regrate = 60 / 8
            totrate = fanrate + regrate
            traininterval = round(60 / totrate)
        else:
            fanrate = 10.2 * math.exp(-(currtime - 180) * (currtime - 193) / 3280)
            if (start_time + math.floor(currtime / 60) * 100 + currtime % 60) <= 800:
                regrate = 60 / 8
            else:
                regrate = 60 / 9.75
            totrate = fanrate + regrate
            traininterval = round(60 / totrate)
        currtime += traininterval
        realtime_hrs = math.floor(start_hrs + (currtime / 60))
        realtime_mins = math.floor(start_mins + (currtime % 60))

        if realtime_mins >= 60:
            realtime_hrs += 1
            realtime_mins = realtime_mins % 60

        tester_hrs = realtime_hrs
        realtime_hrs = realtime_hrs % 13  # Account for hours after midnight
        if tester_hrs >= 13:
            realtime_hrs += 1

        if tester_hrs >= 12:
            time0day = "AM"

        realtime_hrs = "0" + str(realtime_hrs) if realtime_hrs < 10 else str(realtime_hrs)
        realtime_mins = "0" + str(realtime_mins) if realtime_mins < 10 else str(realtime_mins)

        print("The game day train arrives at     <" + str(realtime_hrs) + ":" + str(realtime_mins) + time0day + ">")
