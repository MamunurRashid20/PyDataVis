#Grouping the data based on sex
import csv
from itertools import groupby
file = open('yob1910.txt', 'rt', encoding='utf-8')
data = csv.reader(file)
table = [row for row in data]
for key,group in groupby(table, lambda x: x[1]):
    total = 0
    for item in group:
        total +=int(item[2])
    print(item[1], total)
