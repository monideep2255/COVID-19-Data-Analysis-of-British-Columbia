import csv

def betweendate():
    start = input('Enter the start date for COVID-19 cases you are looking for:\n ')
    end = input('Enter the end date for COVID-19 cases you are looking for:\n ')

    csv_file =csv.reader(open('BCCase_Details.csv','r'))

    for row in csv_file:
        
        if dates == row[1]:
            print(row)

#write the pseudocode!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!