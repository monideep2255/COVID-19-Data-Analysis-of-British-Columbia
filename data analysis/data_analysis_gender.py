import csv
import matplotlib.pyplot as plt

def data_gender():

    with open('datasets/filtergender.csv','r') as csvfile:
        csvfilereader = csv.DictReader(csvfile)
        count1 = 0 
        count2 = 0
        
        for row in csvfilereader:
            for key,value in row.items():
                if value == 'M':
                    count1 += 1
                elif value == 'F':
                    count2 += 1             
        
        gender_brackets = ('M','F')
        gender_brackets = list(gender_brackets)
        covid_numbers = (count1,count2)
        covid_numbers = list(covid_numbers)
        print(gender_brackets)
        print(covid_numbers)

        #visualization with matplotlib
        fig, ax = plt.subplots()

        ax.bar(gender_brackets, covid_numbers)

        ax.set_title("Number of COVID-19 cases in BC according to gender")
        ax.set_ylabel('Number of COVID-19 cases')
        ax.set_xlabel('Gender')


        plt.savefig('images/gender_covid_dict.jpg')
        plt.show()

        #make a dictionary, use pandas and pyplot?         


data_gender()