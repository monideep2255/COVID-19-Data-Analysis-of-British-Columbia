import csv

def data_age():

    with open('filterage.csv','r') as csvfile:
        csvfilereader = csv.DictReader(csvfile)
         
        for row in csvfilereader:
            #row =[col.strip() for col in row]
            row['A g e _ G r o u p'] #stuck here!!!!!!!!!!!!!!!
            
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def data_gender():
    with open('filtergender.csv','r') as csvfile:
        csvfilereader = csv.reader(csvfile)
            
        for row in csvfilereader:
            row =[col.strip() for col in row]

            print(row)

def data_place():
    with open('filterplace.csv','r') as csvfile:
        csvfilereader = csv.reader(csvfile)
            
        for row in csvfilereader:
            row =[col.strip() for col in row]

            print(row)

data_age()
#data_gender()
#data_place()