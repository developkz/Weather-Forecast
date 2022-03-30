import requests

url = "https://wttr.in//san%20francisco?nTqu&lang=en"
html_string = requests.get(url)
print(html_string.text)