import csv

class Files:
    #comments

    def __init__(self, filename, row):
        self.file = filename
        self.row = int(row)

    def makefiles(self):
        #function
        #parameter
        #return

        with open('datasets/BCCase_Details.csv','r') as csvfile:
                csvfilereader = csv.reader(csvfile)

                with open(self.file,'w') as new_file:
                    csv_writer = csv.writer(new_file, delimiter =' ')

                    for row in csvfilereader:
                        csv_writer.writerow(row[self.row])


def main():
    age = Files('datasets/filterage1.csv', 4)
    age.makefiles()
    gender = Files('datasets/filtergender1.csv', 3)
    gender.makefiles()
    place = Files('datasets/filterplace1.csv', 2)
    place.makefiles()

if __name__ == '__main__':
    main()
