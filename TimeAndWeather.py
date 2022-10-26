import requests
import json
from pprint import pprint
import datetime
import sys


apiWeather = '0ccef92205ec3f8d935db746408d8245'

def weatherData(query):
   
    res = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + query +
                       '&APPID=' + apiWeather + '&units=metric')
    return res.json()

def printWeather(result):
    weather = str(result['weather'][0]['main'])
    temperature = str(result['main']['temp'])
    print('Weather:  ' + weather)
    print('Temperature:  ' + temperature +'°C')


now = datetime.datetime.now()
print('The Date is:  ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year))
print('The Time is:  ' + str(now.hour) + ':' + str(now.minute))

cityWeather = 'Bangkok'
printWeather(weatherData(cityWeather))

input()
sys.exit()







