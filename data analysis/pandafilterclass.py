import csv
import os

class Files:
    #Class Files
    #Attributes: filename, column to filter, 4 rows to be deleted
    #method: making smaller files

    def __init__(self, filename, col, row1, row2, row3, row4):
        #constructor: create a new instance of file
        #parameter:
        #self: the current object
        #col: column to filter
        #row(1-4): rows to be deleted

        self.file = filename
        self.col = col
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4

    def makefiles(self):
        #method: write to a new file
        #parameter:
        #self: the current object
        
        try:


            with open('datasets/BCCase_Details.csv','r') as csvfile:

                csvfilereader = csv.DictReader(csvfile)
                #dictionary can help solve the problem, changed it from csv to dict!

                with open(self.file,'w', newline='') as new_file:
                    col = ['Covid_Cases',self.col]
                    csv_writer = csv.DictWriter(new_file, fieldnames= col)

                    csv_writer.writeheader()

                    for row in csvfilereader:
                        del row[self.row1]
                        del row[self.row2]
                        del row[self.row3]
                        del row[self.row4]
                        csv_writer.writerow(row)

        except PermissionError:
            print("You do not have permission to use that file")
        except OSError:
            print("Something happened while writing to the file", csvfile)
        except FileNotFoundError:
            print('File not found')


def main():
    age = Files('datasets/filterage1.csv','Age_Group','Reported_Date', 'Sex', 'Place', 'Classification_Reported')
    age.makefiles()
    gender = Files('datasets/filtergender1.csv','Sex','Reported_Date', 'Age_Group', 'Place', 'Classification_Reported')
    gender.makefiles()
    place = Files('datasets/filterplace1.csv','Place','Reported_Date', 'Sex', 'Age_Group', 'Classification_Reported')
    place.makefiles()
    timeseries = Files('datasets/filtertimeseries1.csv','Reported_Date','Place', 'Sex', 'Age_Group', 'Classification_Reported')
    timeseries.makefiles()
    
#special syntax to be able to call the class in the same module
if __name__ == '__main__': 
    main()
