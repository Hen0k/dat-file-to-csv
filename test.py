import csv
import helpers
"""json = [
    {
        day1: [
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
            
            ]
    },
    {
        day2: [
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
                {id:1, chin1: 'something', ch2: "something"}
            
            ]

    }
]"""

"""json = [
    {
        day1: {
                1:
                 {
                    chin1: 
                        ['something'], 
                    ch2:
                        ["something"] 
                } ,
                2: { chin1: ['something'], ch2: ["something"] } ,
                3: { chin1: ['something'], ch2: ["something"] } ,

            
            }
    },....."""
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
            #print 1.1
            #array.append( { date :  { empid : { 'checkin' : chin.append(time), 'checkout' : chout.append('') } } } )
            array.append( { date :  { empid : { 'checkin' : [ time ], 'checkout' :  [ 'none' ] } } } )
            #print array
        elif pun_stat == CHECK_OUT:     # Useless, i know
            #print 2.1
            #array.append( { date :  { empid : { 'checkin' : chin.append(''), 'checkout' : chout.append(time) } } } )
            array.append( { date :  { empid : { 'checkin' : [ 'none' ], 'checkout' :  [ time ] } } } )
            #print array
    else:
        #print 2
        for day in array:
            if date in day:
            # if day.has_key(date):
                # the date exists
                if empid in day[date]:
                # if day[date].has_key(empid):
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
                        """if (len(day[date][empid]['checkin']) > 0) and (day[date][empid]['checkin'][-1] != 'none'):
                            continue
                        else:"""
                        array[array.index(day)][date][empid] = { 'checkin' : [ time ], 'checkout' :  [ 'none' ] }
                    else:
                        continue
                        """if (len(day[date][empid]['checkout']) > 0) and day[date][empid]['checkout'][-1] != 'none':
                            continue
                        else:
                            array[array.index(day)][date][empid] = { 'checkin' : [ 'none' ], 'checkout' :  [ time ] }"""
            else:
                if pun_stat == CHECK_IN:
                    """if (len(day[date][empid]['checkin']) > 0) and day[date][empid]['checkin'][-1] != 'none':
                            continue
                    else:"""
                    array[array.index(day)][date] = { empid : { 'checkin' : [ time ], 'checkout' :  [ 'none' ] } }
                else:
                    continue
                    """if (len(day[date][empid]['checkout']) > 0) and day[date][empid]['checkout'][-1] != 'none':
                            continue
                    else:
                        array[array.index(day)][date] = { empid : { 'checkin' : [ 'none' ], 'checkout' :  [ time ] } }"""





ids = []
for dict in array:
    dates = dict.keys()
    #ids.append()
for dict in array:
    for date in dates:
        ids.append(list(set(dict[date].keys())))

print (len(dates))
#print (dates)

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
            ### I may be wrong here
            cin = 'checkin'
            cout = 'checkout'
            #a = len(dict[date][i])
            #b = len(tuple(dict[date][i]['checkout']))
            if len(tuple(dict[date][i][cin])) != len(tuple(dict[date][i][cout])):
            #if len(dict[date][i]['checkin']) != len(dict[date][i]['checkout']):
                continue
            else:
                # in_time = list(set(dict[date][i][cin])).remove('none')
                in_time = dict[date][i][cin]#.remove('none')
                #print (in_time)
                # out_time = list(set(dict[date][i][cout])).remove('none')
                out_time = dict[date][i][cout]#.remove('none')
                length = len(dict[date][i][cin])
                if length>0 and len(in_time) > 0:
                    runningSum = 0
                    for l, i, k in zip(range(length), range(0, length, 2), range(1, length, 2)):
                        to_a['in' + str((l+1))] = in_time[i]
                        to_a['out' + str(l+1)] = out_time[k]

                        runningSum += helpers.to_decimal(out_time[k]) - helpers.to_decimal(in_time[i])
                    to_a['Raw_hours'] = runningSum
                    to_a['hoursWorked_str'] = helpers.to_ftime(runningSum)
                """for in_time, out_time in zip(dict[date][i]['CHECKINS'], dict[date][i]['CHECKOUTS']):
                    in_time = list(set(in_time)).remove('none')
                    out_time = list(set(out_time)).remove('none')"""
                    # start writing
                for_csv.append(to_a)







"""if len(array) > 0:
        print ('Working')
        for ele in array:
            #print ('Working')
            if ele.has_key(date):
                # do something
                for dic in ele[date]:
                    if dic['id'] == empid:
                        if pun_stat == CHECK_IN:
                            ele[date]['id']['CHECKINS'].append(time)
                        else:
                            ele[date]['id']['CHECKOUTS'].append(time)
                    else:
                        #something else
                        dic['id'] = empid
                        if pun_stat == CHECK_IN:
                            ele[date].['id']['CHECKINS'].append(time)
                        else:
                            ele[date]['id']['CHECKOUTS'].append(time)
            
            else:
                if pun_stat == CHECK_IN:     # Useless, i know
                    array.append(  { date: [ { 'id': empid, 'CHECK_INS': [time], 'CHECK_OUTS': [] } ] }  )
    
    else:
        #print ('Working')
        if pun_stat == str(CHECK_IN):
            print ('Working')
            array.append(  { date : [ { 'id': empid, 'CHECK_INS': [time], 'CHECK_OUTS': [] } ] }  )"""

#print ((array[0]['2019-03-29'][1]))#['2019-03-01']))
#print len(array[0]['2019-05-02'][28])
#print (array[0]['2019-05-01'][1044])
print(len(for_csv))
print(for_csv)


row_names = ["employeeID", "date", "in1", "out1", "in2", "out2",
             "in3", "out3", "in4", "out4", "in5", "out5", 'hoursWorked_str',
             'Raw_hours']
helpers.write_to_csv(for_csv, 'may', row_names)
