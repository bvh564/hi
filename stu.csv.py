import csv
fields=['name','group','age']
rows=[['siri','msds','18'],
['rani','mscs','20]]
filename='students.csv'
with open('students.csv','w') as csvfile:
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields)
	csv.writerows(rows)