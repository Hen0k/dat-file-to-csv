import csv
import helpers

#constants
ID = 0
DATE_TIME = 1
STATUS = 3
CHECK_IN = 0
CHECK_OUT = 1

f = open('./files/may.dat', 'r')
lines = f.readlines()

array, chin, chout = [], [], []
dates = {}

for line in lines:
    divByTab = line.split("\t")
    empid = int(divByTab[ID].replace(" ", ""))
    date, time = divByTab[DATE_TIME].split(" ")
    pun_stat = int(divByTab[STATUS])
    
    if len(array) == 0:
        #print 1
        if pun_stat == CHECK_IN:
            array.append( { date :  { empid : { 'checkin' : [ time ], 'checkout' :  [ 'none' ] } } } )

        elif pun_stat == CHECK_OUT:     # Useless, i know
            array.append( { date :  { empid : { 'checkin' : [ 'none' ], 'checkout' :  [ time ] } } } )

    else:
        for day in array:
            if date in day:
                if empid in day[date]:
                    if pun_stat == CHECK_IN:
                        if (len(day[date][empid]['checkin']) > 0) and day[date][empid]['checkin'][-1] != 'none': 
                            # check in without a checkout is passed
                            continue
                        
                        else:
                            array[array.index(day)][date][empid]['checkin'].append(time)
                            array[array.index(day)][date][empid]['checkout'].append('none')
                    
                    else:
                        if (len(day[date][empid]['checkout']) > 0) and day[date][empid]['checkout'][-1] != 'none':
                            # checkout withou a checkin is passed
                            continue
                        
                        else:
                            array[array.index(day)][date][empid]['checkin'].append('none')
                            array[array.index(day)][date][empid]['checkout'].append(time)
                
                else:
                    if pun_stat == CHECK_IN:
                        array[array.index(day)][date][empid] = { 'checkin' : [ time ], 'checkout' :  [ 'none' ] }
                    else:
                        continue
 
            else:
                if pun_stat == CHECK_IN:
                    array[array.index(day)][date] = { empid : { 'checkin' : [ time ], 'checkout' :  [ 'none' ] } }
                else:
                    continue



ids = []
for dict in array:
    dates = dict.keys()

for dict in array:
    for date in dates:
        ids.append(list(set(dict[date].keys())))

print (len(dates))


print (len(ids))
dates = tuple(dates)
ids = tuple(ids)
for_csv = []

for dict in array:
    for date, ii in zip(dates, ids):
        for i in ii:
            to_a = {
                        'employeeID' : i,
                        'date' : date,
                        'in1' : '',
                        'out1' : '',
                        'in2' : '',
                        'out2' : '',
                        'in3' : '',
                        'out3' : '',
                        'in4' : '',
                        'out4' : '',
                        'in5' : '',
                        'out5' : '',
                        'hoursWorked_str' : '',
                        'Raw_hours' : 0
                    }

            if len(tuple(dict[date][i]['checkin'])) != len(tuple(dict[date][i]['checkout'])):
                continue
            else:
                in_time = dict[date][i]['checkin']
                out_time = dict[date][i]['checkout']
                length = len(dict[date][i]['cicheckinn'])
                if length>0 and len(in_time) > 0:
                    runningSum = 0
                    for l, i, k in zip(range(length), range(0, length, 2), range(1, length, 2)):
                        to_a['in' + str((l+1))] = in_time[i]
                        to_a['out' + str(l+1)] = out_time[k]

                        runningSum += helpers.to_decimal(out_time[k]) - helpers.to_decimal(in_time[i])
                    to_a['Raw_hours'] = runningSum
                    to_a['hoursWorked_str'] = helpers.to_ftime(runningSum)
                # Writing to array
                for_csv.append(to_a)

print(len(for_csv))
print(for_csv)


row_names = ["employeeID", "date", "in1", "out1", "in2", "out2",
             "in3", "out3", "in4", "out4", "in5", "out5", 'hoursWorked_str',
             'Raw_hours']
helpers.write_to_csv(for_csv, 'may', row_names)
