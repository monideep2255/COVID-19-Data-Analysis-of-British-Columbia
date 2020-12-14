import csv

def searchbyregion():
    #function: search by age
    #parameter: none
    #return: extract the data from one file and either print or write to another file

    #input from the user
    region = input('Enter the region in BC (Out of Canada, Vancouver Coastal, Interior, Fraser, Northern, Vancouver Island):\n ')
    question = input('Do you want to print or write to a CSV file (enter p or c)?')

    try: #defensive coding

        with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.reader(csvfile)

            with open('datasets/specific_regions.csv','w') as new_file:
                csv_writer = csv.writer(new_file)

                for row in csvfilereader:
                    if region == row[2]:
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
                    

    





