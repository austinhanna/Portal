import requests
city = input("Which City do you want to pull weather from? ")
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=40460bd21017b5384bdfcbf78da21cc8"
data = requests.get(url)
read = data.json()
print("City Name: "+read['name'])
print("Temperature: "+str(read['main']['temp']-273.15))
print("Humidity: ")
print("Description: ")
