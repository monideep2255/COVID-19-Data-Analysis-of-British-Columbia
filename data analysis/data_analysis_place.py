import csv
import matplotlib.pyplot as plt
# choose not to make a class since it was messing with the plot structures!
def data_place():

    with open('datasets/filterplace.csv','r') as csvfile:
        csvfilereader = csv.DictReader(csvfile)
        count1 = 0 
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        
        for row in csvfilereader:
            for key,value in row.items():
                if value == 'Out of Canada':
                    count1 += 1
                elif value == 'Vancouver Coastal':
                    count2 += 1
                elif value == 'Interior':
                    count3 += 1
                elif value == 'Fraser':
                    count4 += 1
                elif value == 'Northern':
                    count5 += 1
                elif value == 'Vancouver Island':
                    count6 += 1          
        
        place_brackets = ('Out of Canada','Vancouver Coastal','Interior','Fraser','Northern','Vancouver Island')
        place_brackets = list(place_brackets)
        covid_numbers = (count1,count2,count3,count4,count5,count6)
        covid_numbers = list(covid_numbers)
        print(place_brackets)
        print(covid_numbers)

        #visualization with matplotlib, using a tuple
        fig, ax = plt.subplots(figsize=(6.4,6.8))

        ax.bar(place_brackets, covid_numbers)

        ax.set_title("Number of COVID-19 cases in BC according to different regions")
        ax.set_ylabel('Number of COVID-19 cases')
        ax.set_xlabel('Regions in British Columbia')
        ax.set_xticklabels(place_brackets, rotation=15, horizontalalignment='right')


        plt.savefig('images/place_covid_dict.jpg')
        plt.show()
   #make a dictionary, use pandas and pyplot? 


data_place()