import csv
import matplotlib.pyplot as plt

def data_age():

    with open('datasets/filterage.csv','r') as csvfile:
        csvfilereader = csv.DictReader(csvfile)
        count1 = 0 
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        count8 = 0
        count9 = 0
        
        for row in csvfilereader:
            for key,value in row.items():
                if value == '0-19':
                    count1 += 1
                elif value == '20-29':
                    count2 += 1
                elif value == '30-39':
                    count3 += 1
                elif value == '40-49':
                    count4 += 1
                elif value == '50-59':
                    count5 += 1
                elif value == '60-69':
                    count6 += 1
                elif value == '70-79':
                    count7 += 1
                elif value == '80-89':
                    count8 += 1
                elif value == '90-99':
                    count9 += 1              
        
        age_brackets = ('0-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99')
        age_brackets = list(age_brackets)
        covid_numbers = (count1,count2,count3,count4,count5,count6,count7,count8,count9)
        covid_numbers = list(covid_numbers)
        print(age_brackets)
        print(covid_numbers)

        #visualization with matplotlib
        fig, ax = plt.subplots()

        ax.bar(age_brackets, covid_numbers)

        ax.set_title("Number of COVID-19 cases in BC in different age groups")
        ax.set_ylabel('Number of COVID-19 cases')
        ax.set_xlabel('Different age groups in BC')


        plt.savefig('images/age_covid_dict.jpg')
        plt.show()
   #make a dictionary, use pandas and pyplot?         


data_age()
