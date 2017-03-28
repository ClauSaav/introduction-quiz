import json
import requests

url = 'http://localhost:9200/beeva/clau/1'

with open('/home/administradorcito/introduction-quiz/introduction_quiz.json') as mio:
	carga = json.load(mio)
print (carga)

read = requests.post(url, json = carga)
print(read.text)
