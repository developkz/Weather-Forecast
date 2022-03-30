
import requests

url_template = "https://wttr.in/{}"
cities = ["svo", "London", "Череповец"]
parameters = {'lang': 'ru'}
for city in cities:
    # print(city.)
    url = url_template.format(str(city))
    print(url)
    html_string = requests.get(url, params=parameters)
    print(html_string.text)