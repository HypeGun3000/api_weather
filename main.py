import requests

req = requests.get('https://wttr.in/london?nTqm')
print(req.text)

req = requests.get('https://wttr.in/svo?nTqm')
print(req.text)

req = requests.get('https://wttr.in/Череповец?nTqm&lang=ru')
print(req.text)
