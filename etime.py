#!/usr/bin/env python

import csv

#constants
ID = 0
DATE_TIME = 1
STATUS = 3
CHECK_IN = 0
CHECK_OUT = 1


f = open("data.dat", "r")
dat = f.readlines()

datdic = {}

for d in dat:
	dlst = d.split("\t")
	idnum = int(dlst[ID].replace(" ", ""))
	date, time = dlst[DATE_TIME].split(" ")
	stat = dlst[STATUS]
	if datdic.has_key(idnum):
		if datdic[idnum].has_key(date):
			datdic[idnum][date][time] = stat
		else:
			datdic[idnum] = {date : {time : stat}}
	else:
		datdic[idnum] = {date : {time : stat}}


print datdic
