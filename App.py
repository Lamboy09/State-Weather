import requests, os

key = os.environ['test_key']

state = input('State Weather Checker: Enter Your State.')

def weather(state):
	
	Weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&{}".format(state, key))
	print("City:",Weather.json()['name'])
	print("Description:",Weather.json()['weather'][0]['description'])
	print("Humidty:", Weather.json()['main']['humidity'])
	print("---" * 43)

weather(state)

