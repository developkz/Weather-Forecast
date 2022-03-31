
import requests

url_template = "https://wttr.in/{}"

cities = ["svo", "London", "Череповец"]
parameters = {'lang': 'ru'}

for city in cities:
    url = url_template.format(str(city))
    html_string = requests.get(url, params=parameters)
    html_string.raise_for_status()
    print(html_string.text)