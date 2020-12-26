# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:43:20 2020

@author: user
"""
# This function adds a duration time to a starting time and returns the result.
def add_time(start, duration, day = None):
    # Split and parse the input strings.
    [start_time, end_time] = start.split()
    [start_hour, start_minute] = [int(x) for x in start_time.split(':')]
    [duration_hour, duration_minute] = [int(x) for x in duration.split(':')]
    new_minute = start_minute + duration_minute
    duration_days = 0
    
    # Perform time calculations.
    if new_minute >= 60:
        new_hour = 1
        new_minute -= 60
    else:
        new_hour = 0
    if new_minute < 10:
        new_minute = str(new_minute).zfill(2)
    new_hour = start_hour + duration_hour + new_hour

    if new_hour >= 12 and new_hour < 24 and end_time == 'PM':
        new_hour %= 12
        duration_days += 1
        
    if duration_hour >= 24 :
        duration_days = round(new_hour / 24)
        #duration_day = f'({round(new_hour / 24)} days later)'
    elif end_time == 'PM' and (12 - start_hour) < duration_hour or (24 - start_hour) < duration_hour:
        duration_day = '(Next day)'
    if ((duration_hour % 12) + start_hour) >= 11:
        if end_time == 'AM':
            end_time = 'PM'
        else: end_time = 'AM' 
    new_hour = (new_hour % 12) or 12

    if day == None:
        if duration_days > 1:
            if end_time == 'PM':
                new_time = f'{new_hour}:{new_minute} PM ({duration_days} days later)'
            else:
                new_time = f'{new_hour}:{new_minute} AM ({duration_days} days later)'
        elif duration_days == 1:
            if end_time == 'PM':
                new_time = f'{new_hour}:{new_minute} PM (next day)'
            else:
                new_time = f'{new_hour}:{new_minute} AM (next day)'
        else:
            if end_time == 'PM':
                new_time = f'{new_hour}:{new_minute} PM'
            else:
                new_time = f'{new_hour}:{new_minute} AM'
    else:
        days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
        day = days[(days.index(day.capitalize()) + 1 + duration_days)%7 - 1]
        if duration_days > 1:
            if end_time == 'PM':
                new_time = f'{new_hour}:{new_minute} PM, {day} ({duration_days} days later)'
            else:
                new_time = f'{new_hour}:{new_minute} AM, {day} ({duration_days} days later)'
        elif duration_days == 1:
            if end_time == 'PM':
                new_time = f'{new_hour}:{new_minute} PM, {day} (next day)'
            else:
                new_time = f'{new_hour}:{new_minute} AM, {day} (next day)'
        else:
            if end_time == 'PM':
                new_time = f'{new_hour}:{new_minute} PM, {day}'
            else:
                new_time = f'{new_hour}:{new_minute} AM, {day}'
                
    print(new_time)    
    return new_time

add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 PM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("5:01 AM", "0:00")
add_time("3:30 PM", "2:12", "Monday")
add_time("2:59 PM", "24:00", "Saturday")
add_time("11:59 PM", "24:05", "Wednesday")
add_time("8:16 PM", "466:02", "Tuesday")

         
        
    
    
