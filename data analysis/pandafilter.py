import csv
import os

#used functions to make smaller modules for the data analysis part!
#smaller modules easier to handle and use
#efficient and easy for debugging
#instead of having three functions do the same thing, better to put it into a class

def makefiles():
    #function: make files
    #parameter: none
    #return: creates new file with specific columns

    try:


        with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, changed it from csv to dict!
            #problem with writing as a csv was that each character was converted into a 
            #string
            #making it very hard for future use

            with open('datasets/filterage.csv','w', newline='') as new_file:
                col = ['Covid_Cases','Age_Group']
                csv_writer = csv.DictWriter(new_file, fieldnames= col)

                csv_writer.writeheader() #ensures the new csv file will have titles

                for row in csvfilereader:
                    del row['Reported_Date'] #deleting rows not needed
                    del row['Sex']
                    del row['Place']
                    del row['Classification_Reported']
                    csv_writer.writerow(row)
    
    except PermissionError:
        print("You do not have permission to use that file")
    except OSError:
        print("Something happened while writing to the file", csvfile)
    except FileNotFoundError:
        print('File not found')
                

def makefiles_one():
    #function: make files
    #parameter: none
    #return: creates new file with specific columns

    try:


        with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, changed it from csv to dict!
            #dictionary is easier to read due to the key-value pairs

            with open('datasets/filtergender.csv','w', newline='') as new_file:
                col = ['Covid_Cases','Sex']
                csv_writer = csv.DictWriter(new_file, fieldnames= col)

                csv_writer.writeheader()

                for row in csvfilereader:
                    del row['Reported_Date']
                    del row['Age_Group']
                    del row['Place']
                    del row['Classification_Reported']
                    csv_writer.writerow(row)

    except PermissionError:
        print("You do not have permission to use that file")
    except OSError:
        print("Something happened while writing to the file", csvfile)
    except FileNotFoundError:
        print('File not found')

def makefiles_two():
    #function: make files
    #parameter: none
    #return: creates new file with specific columns

    try:


        with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, changed it from csv to dict!

            with open('datasets/filterplace.csv','w', newline='') as new_file:
                col = ['Covid_Cases','Place']
                csv_writer = csv.DictWriter(new_file, fieldnames= col)

                csv_writer.writeheader()

                for row in csvfilereader:
                    del row['Reported_Date']
                    del row['Age_Group']
                    del row['Sex']
                    del row['Classification_Reported']
                    csv_writer.writerow(row)

    except PermissionError:
        print("You do not have permission to use that file")
    except OSError:
        print("Something happened while writing to the file", csvfile)
    except FileNotFoundError:
        print('File not found')

def makefiles_three():
    #function: make files
    #parameter: none
    #return: creates new file with specific columns

    try:


        with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, change it from csv to dict!

            with open('datasets/filtertimeseries.csv','w', newline='') as new_file:
                col = ['Covid_Cases','Reported_Date']
                csv_writer = csv.DictWriter(new_file, fieldnames= col)

                csv_writer.writeheader()

                for row in csvfilereader:
                    del row['Place']
                    del row['Age_Group']
                    del row['Sex']
                    del row['Classification_Reported']
                    csv_writer.writerow(row)

    except PermissionError:
        print("You do not have permission to use that file")
    except OSError:
        print("Something happened while writing to the file", csvfile)
    except FileNotFoundError:
        print('File not found')



makefiles()
makefiles_one()
makefiles_two()
makefiles_three()
