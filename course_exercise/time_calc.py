def add_time(start, duration, days=None):
    days_of_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_of_week_index = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5,
                          'sunday': 6}

    duration_tuple = duration.partition(':')
    duration_hour = int(duration_tuple[0])
    duration_minute = int(duration_tuple[2])

    start_tuple = start.partition(':')
    start_minute_tuple = start_tuple[2].partition(' ')
    start_minute = int(start_minute_tuple[0])
    start_hour = int(start_tuple[0])
    am_or_pm = start_minute_tuple[2]
    am_pm_flip = {'AM': "PM", 'PM': 'AM'}

    amount_of_days = int(duration_hour / 24)

    end_minute = start_minute + duration_minute
    if end_minute >= 60:
        start_hour += 1
        end_minute = end_minute % 60
    end_hour = (start_hour + duration_hour) % 12
    am_pm_flip_amount = int((start_hour + duration_hour) / 12)

    if end_minute > 9:
        end_minute = end_minute
    else:
        end_minute = '0' + str(end_minute)

    if end_hour == 0:
        end_hour = 12
    else:
        end_hour = end_hour

    if am_or_pm == 'PM' and start_hour + (duration_hour % 12) >= 12:
        amount_of_days += 1

    if am_pm_flip_amount % 2 == 1:
        am_or_pm = am_pm_flip[am_or_pm]
    else:
        am_or_pm = am_or_pm

    returnTime = str(end_hour) + ':' + str(end_minute) + ' ' + am_or_pm
    if days:
        days = days.lower()
        index = int(days_of_week_index[days] + amount_of_days) % 7
        new_day = days_of_week_array[index]
        returnTime += ', ' + new_day

    if amount_of_days == 1:
        return returnTime + ' (next day)'
    elif amount_of_days > 1:
        return returnTime + f' ({amount_of_days} days later)'
    return returnTime


print(add_time("11:40 PM", "0:25"))
