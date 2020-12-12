import csv

#used functions to make smaller files for the data analysis part!

#DEF MAKE INTO CLASSES: BOTH THE FILTER PROCESS AND THE PLOTTING PROCESS THINK AND DESIGN

def makefiles():
    #function
    #parameter
    #return

    with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, change it from csv to dict!
            #problem with writing as a csv was that each character was converted into a 
            #string
            #making it very hard for future use

            with open('datasets/filterage.csv','w', newline='') as new_file:
                col = ['Covid_Cases','Age_Group']
                csv_writer = csv.DictWriter(new_file, fieldnames= col)

                csv_writer.writeheader()

                for row in csvfilereader:
                    del row['Reported_Date']
                    del row['Sex']
                    del row['Place']
                    del row['Classification_Reported']
                    csv_writer.writerow(row)
                

def makefiles_one():
    #function
    #parameter
    #return

     with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, change it from csv to dict!

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

def makefiles_two():
    #function
    #parameter
    #return

     with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, change it from csv to dict!

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

def makefiles_three():
    #function
    #parameter
    #return

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



makefiles()
makefiles_one()
makefiles_two()
makefiles_three()
