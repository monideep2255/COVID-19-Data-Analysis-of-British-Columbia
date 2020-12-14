import csv
import os

def searchbyage():
    #function: search by age
    #parameter: none
    #return: extract the data from one file and either print or write to another file

    #input from the user
    age = input('Enter the age group (0-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99):\n ')
    question = input('Do you want to print or write to a CSV file (enter p or c)?')

    try: #defensive coding

        with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.reader(csvfile)

            with open('datasets/specific_age.csv','w') as new_file:
                csv_writer = csv.writer(new_file)

                for row in csvfilereader:
                    if age == row[4]:
                    #user gets the choice to either print or create a new file
                        if question == 'p':
                            print(row)
                        else:
                            csv_writer.writerow(row)

    except PermissionError:
        print("You do not have permission to use that file")
    except OSError:
        print("Something happened while writing to the file", csvfile)
    except FileNotFoundError:
        print('File not found')
