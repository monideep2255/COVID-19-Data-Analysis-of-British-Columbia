import csv
import matplotlib.pyplot as plt
import os

#initially used pandas library to perform my data analysis
#this is my version and I used matplotlib for the graphs

def data_gender():
    #function: opening the filtered file
    #parameters: none
    #return: graph

    try:

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
            #preparaing lists for visualization, will be easier to plot
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

    except PermissionError:
        print("You do not have permission to use that file")
    except OSError:
        print("Something happened while writing to the file", csvfile)
    except FileNotFoundError:
        print('File not found')

data_gender()