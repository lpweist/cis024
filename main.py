# -------- START: don't modify anything below this line ------
import json

with open('.lesson/data.json') as f:
  data = json.load(f)
# -------- END: don't modify anything above this line ------

# the dictionary you need to process is in `data` variable
# data is the weather forecast for the next 5 days in 3 hour interval
# However, the raw JSON file is not really human readable
# So, what you need to do is to process it, and summarize it into something like this:
"""
City Name: <string>
Country Name: <string>
Average temperature (use temp, not feels_like): <float, keep two digits after decimal>
Average humidity when wind speed is greater than 1: <float>
All distinct weather descriptions: <string separated by comma>
Minimum temperature(in Fahrenheit, data is in Kelvin): <float, same, two digits>
Timestamp for mininum temperature: <string>
Maxinum temperature: <float, two digits>
Timestamp for maximum temperature: <string>
"""
# Your final answer should be exactly this (All distinct weather descriptions can be in any order!):
"""
City Name: San Jose
Country Name: US
Average Temperature: 68.69
Average humidity when wind speed is greater than 1: 50.94
All distinct weather descriptions: scattered clouds, few clouds, overcast clouds, broken clouds, clear sky
Minimum temperature: 57.83
Timestamp for mininum temperature: 2023-09-18 12:00:00
Maximum temperature: 90.03
Timestamp for maximum temperature: 2023-09-15 21:00:00
"""

# EXTRA POINTS:
# print out dates of the coolest and the hottest day (not a certain hour of a day!)
# and the average temperature of the coolest and hottest day

# -------- Your program starts here! -----------
# You can use `print(data)` to see what it actually looks like
# hint: you can copy and paste the data to some online JSON formater website (like https://jsonformatter.org/) to get a better understanding of how the whole data is like

onlylist = data["list"]
cityloc = data["city"]["name"]
countryname = data["city"]["country"]
counts = data["cnt"]
dt1 = onlylist[1]["dt"]
temps = []
humidity = []
descr = []
maxtemp = 10
maxtemptime = []
mintemp = 1000
mintemptime = []
times = []

i = 0
#newlist = sorted(listcontents)
while i <= (counts - 1):
  #pull temps (and timestamps for max and min purposes)
  dt1 = onlylist[i]["main"]["temp"]
  temps.append(1.8 * ((dt1) - 273.15) + 32)
  ts1 = onlylist[i]["dt_txt"]
  times.append(ts1)

  #pull humidity when wind speed is > 1
  if onlylist[i]["wind"]["speed"] > 1:
    h1 = onlylist[i]["main"]["humidity"]
    humidity.append(h1)

  #pull weather descriptions
  dr1 = onlylist[i]["weather"][0]["description"]
  descr.append(dr1)

  #sort temps
  if temps[i] < mintemp:
    mintemp = temps[i]
    mintemptime = times[i]
  if temps[i] > maxtemp:
    maxtemp = temps[i]
    maxtemptime = times[i]
  i += 1

print("City Name:", cityloc)
print("Country Name:", countryname)
print("Average temperature:", round(sum(temps) / len(temps), 2))
print("Average humidity when wind speed is greater than 1:",
      round(sum(humidity) / len(humidity), 2))
print("All distinct weather descriptions:", ', '.join(set(descr)))
print("Minimum temperature:", round(mintemp, 2))
print("Timestamp for minimum temperature:", mintemptime)
print("Maximum temperature:", round(maxtemp, 2))
print("Timestamp for maximum temperature:", maxtemptime)
