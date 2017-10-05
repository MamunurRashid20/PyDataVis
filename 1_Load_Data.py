#Load data
import csv
file = open('yob1910.txt', 'rt', encoding='utf-8')
data = csv.reader(file)
table = [row for row in data]
print(table[:3])

