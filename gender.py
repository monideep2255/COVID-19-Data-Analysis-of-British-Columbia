import csv

def searchbygender():
    gender = input('Enter the gender for COVID-19 cases you are looking for:\n ')
    csv_file =csv.reader(open('BCCase_Details.csv','r'))

    for row in csv_file:
        if gender == row[3]:
            print(row)
        else:
            break

    csv_file.close()