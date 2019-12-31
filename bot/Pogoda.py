import pyowm

owm = pyowm.OWM('d41a733192602688c50263e6365382f5', language="ru")

place = input("Повелитель, в каком городе интересует погода?")

observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]

print("Повелитель, в городе " + place + " сейчас " + w.get_detailed_status())
print("А температура " + str(temp))
