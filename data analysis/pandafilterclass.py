import csv

class Files:
    #comments

    def __init__(self, filename, col, row1, row2, row3, row4):
        self.file = filename
        self.col = col
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4

    def makefiles(self):
        #function
        #parameter
        #return

        with open('datasets/BCCase_Details.csv','r') as csvfile:

            csvfilereader = csv.DictReader(csvfile)
            #dictionary can help solve the problem, change it from csv to dict!

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


def main():
    age = Files('datasets/filterage1.csv','Age_Group','Reported_Date', 'Sex', 'Place', 'Classification_Reported')
    age.makefiles()
    gender = Files('datasets/filtergender1.csv','Sex','Reported_Date', 'Age_Group', 'Place', 'Classification_Reported')
    gender.makefiles()
    place = Files('datasets/filterplace1.csv','Place','Reported_Date', 'Sex', 'Age_Group', 'Classification_Reported')
    place.makefiles()
    timeseries = Files('datasets/filtertimeseries1.csv','Reported_Date','Place', 'Sex', 'Age_Group', 'Classification_Reported')
    timeseries.makefiles()

if __name__ == '__main__':
    main()
