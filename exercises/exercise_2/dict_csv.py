# Python program to convert
# JSON file to CSV


import json
import csv


# Opening JSON file and loading the data
# into the variable data
with open('exercises/exercise_2/data.json') as json_file:
    data = json.load(json_file)

student_data = data

# now we will open a file for writing
data_file = open('exercises/exercise_2/data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for student in student_data:
    if count == 0:

        # Writing headers of CSV file
        header = student.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(student.values())

data_file.close()
