def convert_time(hour,minutes,period):
    if period == "am" and hour==12 :
        hour=0
    elif period =="pm" and hour<12 :
        hour+=12
    print(f"{hour:02d}{minutes}")
    return f"{hour:02d}{minutes}"

convert_time(12,45,"pm")

