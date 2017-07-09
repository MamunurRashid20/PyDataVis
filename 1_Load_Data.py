#Load data
import csv
file = open('yob1910.txt','rb')
data = csv.reader(file)
table = [row for row in data]
print(table[:3])