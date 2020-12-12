import csv

def searchbyage():
    age = input('Enter the age group (0-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99):\n ')
    question = input('Do you want to print or write to a CSV file (enter p or c)?')

    with open('datasets/BCCase_Details.csv','r') as csvfile:
        csvfilereader = csv.reader(csvfile)
        
        
        with open('datasets/specific_age.csv','w') as new_file:
            csv_writer = csv.writer(new_file)

            for row in csvfilereader:
                if age == row[4]:
                    if question == 'p':
                        print(row)
                    else:
                        csv_writer.writerow(row)