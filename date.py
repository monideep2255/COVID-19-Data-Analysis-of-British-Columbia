import csv

def searchbydate():
    date= input('Enter the date for COVID-19 cases you are looking for:\n ')
    csv_file =csv.reader(open('BCCase_Details.csv','r'))

    for row in csv_file:
        if date == row[1]:
            print(row)
        else:
            break

    csv_file.close()