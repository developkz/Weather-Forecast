
import requests

url_template = "https://wttr.in/{}"

cities = ["svo", "London", "Череповец"]
parameters = {'lang': 'ru'}


for city in cities:
    url = url_template.format(str(city))
    string_data = requests.get(url, params=parameters)
    string_data.raise_for_status()
    print(string_data.text)