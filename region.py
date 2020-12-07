import csv

def searchbyregion():
    region = input('Enter the region in BC:\n ')
    csv_file =csv.reader(open('BCCase_Details.csv','r'))

    for row in csv_file:
        if region == row[2]:
            print(row)
        else:
            break
    
    csv_file.close()




