import requests, json, time

def summarise_forecast(city):
	r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q='+city+'&units=imperial&cnt=14')
	data = json.loads(r.text)

	max_weather=[]
	min_weather=[]
	main_weather={}

	for day in data['list']:
		max_weather.append(day['temp']['max'])
		min_weather.append(day['temp']['min'])

		date = time.strftime('%Y-%m-%d', time.localtime(day['dt']))

		try:
			main_weather[day['weather'][0]['main']].append(date)
		except:
			main_weather[day['weather'][0]['main']] = [date]

	weather = {
		'city':city,
		'max':max(max_weather),
		'min':min(min_weather),
		'forecasts':main_weather,
		}
	
	return weather