import csv

def searchbygender():
    #function: search by gender
    #parameter: none
    #return: extract the data from one file and either print or write to another file

    #input from the user
    gender = input('Enter the gender(M/F):\n ')
    question = input('Do you want to print or write to a CSV file (enter p or c)?')

    try: #defensive coding
    
        with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.reader(csvfile)

            with open('datasets/specific_gender.csv','w') as new_file:
                csv_writer = csv.writer(new_file)

                for row in csvfilereader:
                    if gender == row[3]:
                    #user choice to either print or write to a file
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