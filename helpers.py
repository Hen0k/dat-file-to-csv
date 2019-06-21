import math
def to_decimal(ftime):
    """This function converts hours 
    that are in the for hh:mm:sec 
    into fractions of the day"""

    hours, minutes, seconds = ftime.split(":")
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    hours = hours/24.0
    #print (hours)
    minutes = minutes/(24 * 60.0)
    #print (minutes)
    seconds = seconds / (24*60*60.0)
    totalInDec = hours+minutes+seconds

    return totalInDec    

print (to_decimal("10:47:00"))

def to_ftime(dec_time):
    """This function converts hours 
    that are in decimal forms(what fraction
    of the day they are to) to a fromated string
    like hh:mm:ss"""
    temp = dec_time * 24
    hours = math.floor(temp)
    tempm = (temp - hours) * 60
    minutes = math.floor(tempm)
    temps = (tempm - minutes) * 60
    seconds = math.floor(temps)

    return ( str(int(hours)).zfill(2) + ":" + str(int(minutes)).zfill(2) + ":" + str(int(seconds)).zfill(2) )

print (to_ftime(0.44930555555555557))
print (to_ftime(0.189583))