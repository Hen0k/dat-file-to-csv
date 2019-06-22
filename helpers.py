from datetime import timedelta
import csv

def to_decimal(ftime):
    """This function converts hours 
    that are in the for hh:mm:sec 
    into fractions of the day"""

    duration = timedelta(**dict(zip(['hours', 'minutes', 'seconds'],
                                    map(int, ftime.split(':')))))
    return duration.total_seconds()/(24*60*60.0)


def to_ftime(dec_time):
    """This function converts hours 
    that are in decimal forms(what fraction
    of the day they are to) to a fromated string
    like hh:mm:ss"""

    dec_time *= 24*60*60
    hours, remainder = divmod(dec_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


def write_to_csv(data, file_name, row_names):
    """This Function writes an array of dictionaries
    to a csv file using the csv modules DictWriter function"""

    f = open("csv/" + file_name + ".csv", "w")
    writer = csv.DictWriter(f, fieldnames=row_names)
    writer.writeheader()
    writer.writerows(data)
    f.close()

