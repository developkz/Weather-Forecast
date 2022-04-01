import requests


locations = [
    'svo', 
    'London', 
    'Череповец'
]

parameters = {'lang': 'ru', 'T': '', 'n': ''}


for location in locations:
    url_template = 'https://wttr.in/{}'
    url = url_template.format(location)
    weather_response = requests.get(url, params=parameters)
    weather_response.raise_for_status()
    print(weather_response.text)
