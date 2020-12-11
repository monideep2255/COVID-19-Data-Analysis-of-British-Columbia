import csv

def searchbydate():
    date = input('Enter the specific date(DD/MM/YY):\n ')
    question = input('Do you want to print or write to a CSV file (enter p or c)?')

    with open('BCCase_Details.csv','r') as csvfile:
        csvfilereader = csv.reader(csvfile)
        
        
        with open('specific_date.csv','w') as new_file:
            csv_writer = csv.writer(new_file)

            for row in csvfilereader:
                if date == row[1]:
                    if question == 'p':
                        print(row)
                    else:
                        csv_writer.writerow(row)

   