import forecastio
api_key = "359bff8fcf2d1cb89382a17e32b79906"
lat = 51.5033640
lng = -0.1276250
forecast = forecastio.load_forecast(api_key, lat, lng)
byHour = forecast.hourly()
print (byHour.summary)
print (byHour.icon)
for hourlyData in byHour.data:
    print(hourlyData.temperature)
