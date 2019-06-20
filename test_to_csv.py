import csv

f = open("sample.csv", "w")
writer = csv.DictWriter(
    f, fieldnames=["fruit", "count"])
writer.writeheader()
writer.writerows(
    [{"fruit": "apple", "count": "1"},
    {"fruit": "banana", "count": "2"},
    {"fruit": "orange", "count": "1"}])
f.close()