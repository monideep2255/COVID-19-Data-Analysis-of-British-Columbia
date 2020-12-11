import csv

def searchbyregion():
    region = input('Enter the region in BC (Out of Canada, Vancouver Coastal, Interior, Fraser, Northern, Vancouver Island):\n ')
    question = input('Do you want to print or write to a CSV file (enter p or c)?')

    with open('BCCase_Details.csv','r') as csvfile:
        csvfilereader = csv.reader(csvfile)
        
        
        with open('specific_regions.csv','w') as new_file:
            csv_writer = csv.writer(new_file)

            for row in csvfilereader:
                if region == row[2]:
                    if question == 'p':
                        print(row)
                    else:
                        csv_writer.writerow(row)
                    

    





