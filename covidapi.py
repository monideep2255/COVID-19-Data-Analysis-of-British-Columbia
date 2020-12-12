import requests
import csv
import json

def covid_real_time():

    #include try and except block here to showcase your defensive coding!

    url = 'https://covid19.mathdro.id/api/countries/Canada'
    response = requests.get(url)
    data = response.json() #dictionary
    
    confirmed = (data['confirmed']['value'])
    recovered = (data['recovered']['value'])
    deaths = (data['deaths']['value'])
    update = (data['lastUpdate'])

    print('The number of active cases in Canada are: ', confirmed)
    print('The number of recovered cases in Canada are: ', recovered)
    print('The number of deaths in Canada are: ', deaths)
    print('Latest Update: ', update)
       

covid_real_time()

