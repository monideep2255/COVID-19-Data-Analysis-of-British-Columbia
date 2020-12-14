import requests #library that allows interaction with API(Application Programming Interface)
import csv
import json

def covid_real_time():
    #function: covid_real_time
    #parameters: none
    #return: prints out the upto date COVID-19 Canada statistics
       
    #API: access point to a frequently updated database
    #better than a spreadsheet as it is frequently updated

    url = 'https://covid19.mathdro.id/api/countries/Canada'
    
    try: #defensive coding (asking forgiveness)
        
        response = requests.get(url)

    except HTTPError: #raising API specific error
        print('Unable to connect to API')
        
    try:
        #json format is the standard accepted format for reading API's
        #works similar to a python dictionary (key-value pairs)
        #makes it way easier to use API
        data = response.json() 

    except json.decoder.JSONDecodeError:
        print('Error extracting json data from API. Loading file...')
        with open('datasets/coronavirus_COVID-19_cases.csv') as csvfile:
            data = csv.reader(csvfile)
    
    else:
        print('Successfully extracted data from API')
    
    finally: #the error messages will show up in the terminal window/shell
        confirmed = (data['confirmed']['value']) #API data accessed similar to a dictionary
        recovered = (data['recovered']['value'])
        deaths = (data['deaths']['value'])
        update = (data['lastUpdate'])

        print('The number of active cases in Canada are: ', confirmed)
        print('The number of recovered cases in Canada are: ', recovered)
        print('The number of deaths in Canada are: ', deaths)
        print('Latest Update: ', update)
       

covid_real_time()

