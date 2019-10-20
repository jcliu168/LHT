# Takes constants and efficiency curve and adds together
# Recursively finds points of buses in minutes
import datetime
import constants
import math


def calc_sched(date, start_time):
    train_relative_times = []
    date = datetime.datetime(2019, int(date[0:2]), int(date[2:4]))
    dow = date.weekday()
    x = constants.OFFSET
    train = constants.OFFSET
    while x <= 240:
        if dow in range(6):
            val = 30 * math.exp(((x - 187) ^ 2) / 3400)
            if (int(start_time) + math.floor(x/60)*100 + x % 60) <= 730:
                const = 5.25
            else:
                const = 8.25
            train = round(const + val)
        elif dow == 6:
            val = 30 * math.exp((-1 * (x - 180) * (x - 193)) / 3280)
            if (int(start_time) + math.floor(x / 60) * 100 + x % 60) <= 630:
                const = 6
            else:
                const = 8
            train = round(const + val)
        else:
            val = 30 * math.exp((-1 * (x - 180) * (x - 193)) / 3280)
            if (int(start_time) + math.floor(x / 60) * 100 + x % 60) <= 800:
                const = 8
            else:
                const = 9.75
            train = round(const + val)
        train_relative_times.append(train)
        x += train
    for x in train_relative_times:
        trainhrs = math.floor(x / 60) * 100
        trainmin = (x % 60)
        train_time = int(start_time) + trainmin + trainhrs
        train_time = train_time % 1200  # Account for hours after midnight
        print(train_time)