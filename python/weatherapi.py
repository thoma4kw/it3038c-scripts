import json 

import requests 

print('Please enter your zip code:') 
zip = input() 

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=45225,us&appid=255a27a75cee9769c493b261d46a8fe1') 

data=r.json() 

print(data['weather'][0]['description']) 