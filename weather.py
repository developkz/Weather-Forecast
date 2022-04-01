import requests


locations = [
    'svo', 
    'London', 
    'Череповец'
]

parameters = {'lang': 'ru'}


for location in locations:
    url_template = 'https://wttr.in/{0}{1}'
    url = url_template.format(location, '?Tn')
    # print(url)
    weather_request = requests.get(url, params=parameters)
    weather_request.raise_for_status()
    print(weather_request.text)
