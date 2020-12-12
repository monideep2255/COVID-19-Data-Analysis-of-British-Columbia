import csv

#used functions to make smaller files for the data analysis part!

#DEF MAKE INTO CLASSES: BOTH THE FILTER PROCESS AND THE PLOTTING PROCESS THINK AND DESIGN

def makefiles():
    #function
    #parameter
    #return

    with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.reader(csvfile)
            
            #for row in csvfilereader:
                #print(row)
                #a = row[4].count('20-29')
                #print(a)
            with open('datasets/filterage.csv','w') as new_file:
                csv_writer = csv.writer(new_file, delimiter=' ')

                for row in csvfilereader:
                    csv_writer.writerow(row[4])
                #look into the count option

def makefiles_one():
    #function
    #parameter
    #return

    with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.reader(csvfile)

            with open('datasets/filtergender.csv','w') as new_file:
                csv_writer = csv.writer(new_file, delimiter =' ')

                for row in csvfilereader:
                    csv_writer.writerow(row[3])

def makefiles_two():
    #function
    #parameter
    #return

    with open('datasets/BCCase_Details.csv','r') as csvfile:
            csvfilereader = csv.reader(csvfile)

            with open('datasets/filterplace.csv','w') as new_file:
                csv_writer = csv.writer(new_file, delimiter =' ')

                for row in csvfilereader:
                    csv_writer.writerow(row[2])




makefiles()
makefiles_one()
makefiles_two()
